# dont direct regist example class. 


import bpy
import os, json
from bpy_extras.io_utils import ExportHelper, ImportHelper
from . import actions


class EXAMPLE_OT_exporter_helper(bpy.types.Operator, ExportHelper):
    bl_idname = "example.exporter_helper"
    bl_label = "ExporterHelper Example"
    bl_description = "ExportHelper Example"

    filename_ext = ".json"

    filter_glob: bpy.props.StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )  

    filepath = bpy.props.StringProperty(
        default="",
    )
    # type: bpy.props.EnumProperty(
    #     name="Example Enum",
    #     description="Choose between two items",
    #     items=(
    #         ('OPT_A', "First Option", "Description one"),
    #         ('OPT_B', "Second Option", "Description two"),
    #     ),
    #     default='OPT_A',
    # )

    def execute(self,context):
        objects = bpy.data.objects
        mat_dict = {}

        for obj in objects:
            material_slots = obj.material_slots
            if len(material_slots) > 0:
                materials = [material.name for material in material_slots]
                mat_dict[obj.name] = materials

        data_file = open(self.filepath, "w")
        json.dump(mat_dict, data_file, ensure_ascii=False, indent=4)
        data_file.close()
        context.scene.AUTOPBR_properties.material_data_file = self.filepath
        
        self.report({'INFO'}, str(mat_dict) )
        return {'FINISHED'}

class EXAMPLE_OT_importer_helper(bpy.types.Operator, ImportHelper):
    bl_idname = "example.importer"
    bl_label = "ImportHelper Example"
    bl_description = "ImportHelper Example"

    filename_ext = ".blend"

    filter_glob: bpy.props.StringProperty(
        default="*.blend",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )  

    filepath = bpy.props.StringProperty(
        default="",
    )

    def execute(self,context):
        self.load_material()
            # self.report({'INFO'}, str(data_to.materials))
        # self.report({'INFO'}, str(data_from) )
        return {'FINISHED'}

    def materials_dict(self):
        with bpy.data.libraries.load(self.filepath, link=False) as (data_from, data_to):
             for attr in dir(data_to.objects):
                self.report({'INFO'}, str(attr) )

    def load_material(self):
        scene_materials = bpy.data.materials
        with bpy.data.libraries.load(self.filepath, link=False) as (data_from, data_to):
            for material in data_from.materials:
                if material in scene_materials:
                    scene_materials.remove(scene_materials[material])
                    message = "Update material: %s from file" % (material)
                    self.report({'INFO'}, message )
                    
            data_to.materials = data_from.materials

        return {'FINISHED'}

class EXAMPLE_OT_complex(bpy.types.Operator):
    bl_idname = "example.complex_operator"
    bl_label = "Operator Example complex"
    bl_description = "Operator Example complex"

    def execute(self, context):
        fuzz_search = context.scene.AUTOPBR_properties.fuzzy_search

        if fuzz_search:
            self.fuzz_assign()
        else:
            self.precise_assign()
        
        return {'FINISHED'}

    def load_data(self):
        material_dict = {}
        file_path = bpy.context.scene.AUTOPBR_properties.material_data_file
        if os.path.exists(file_path):
            data_file = open(file_path, "r")
            material_dict = json.load(data_file)
            data_file.close()

        return material_dict

    def fuzz_assign(self):
        material_dict = self.load_data()
        objects = bpy.data.objects

        for obj in objects:
            for key in material_dict.keys():
                if obj.name.find(key) > -1:
                    obj.data.materials.clear()
                    materials_name = material_dict[key]
                    for name in materials_name:
                        material = bpy.data.materials[name]
                        obj.data.materials.append(material)

                    message = "Re-Assigned %s material" % (obj.name)
                    self.report({'INFO'}, (message) )

        return {'FINISHED'}

    def precise_assign(self):
        material_dict = self.load_data()
        objects = bpy.data.objects

        matched_objs = [obj for obj in objects if obj.name in material_dict]
        for obj in matched_objs:
            obj.data.materials.clear()
            materials_name = material_dict[obj.name]
            for name in materials_name:
                material = bpy.data.materials[name]
                obj.data.materials.append(material)
            
            message = "Re-Assigned %s material" % (obj.name)
            self.report({'INFO'}, (message) )

        return {'FINISHED'}


class EXAMPLE_OT_simple(bpy.types.Operator):
    bl_idname = "example.simple_operator"
    bl_label = "Operator Example simple"
    bl_description = "Operator Example simple"

    def execute(self, context):
        autopbr_properties = bpy.context.scene.AUTOPBR_properties
        mAssigntype = autopbr_properties.assigntype

        materials = actions.collect_materials(mAssigntype)
        for material in materials:
            result = actions.assign_pbr_maps(material)
        # message = "process material %s" % (material.name)
        # self.report({'INFO'}, (message) )
        # assign_pbr_map()

        return {'FINISHED'}
 

class EXAMPLE_OT_button_actions(bpy.types.Operator):
    """ Actions """
    bl_label ="AutoPBRMapper Operator"
    bl_idname = "Operator Example button actions"
    bl_options = {"REGISTER", "UNDO"}

    button : bpy.props.StringProperty(default="")
    texturepath : bpy.props.StringProperty(default="")

    def execute(self, context):
        button=self.button
        try:
            ## ObjectOperator
            if button=="AssignMaterial": 
                actions.assign_pbr_maps()
            elif button == 'Apply Name':
                actions.data_rename()
            elif button == 'Find Replace':
                actions.find_replace()
            else:
                print ('Not defined !')
        except Exception as e:
            print ('Execute Error:',e)
        
        return {"FINISHED"}



classes = (
    # EXAMPLE_OT_simple,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
