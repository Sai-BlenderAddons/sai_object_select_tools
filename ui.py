# coding=UTF-8
# dont direct regist example class. 

import bpy
from bpy.types import Operator, AddonPreferences, Panel, PropertyGroup
from bpy.props import StringProperty, BoolProperty, IntProperty, CollectionProperty, BoolVectorProperty, PointerProperty, EnumProperty

class SAI_SELECT_PT_main(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SaiTools"
    bl_label = "Select Tools"
    # bl_options = {"DEFAULT_CLOSED"}   
    def draw(self,context):
        pass

class SAI_SELECT_PT_settings(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Settings"
    bl_parent_id = "SAI_SELECT_PT_main"
    bl_options = {'DEFAULT_CLOSED'}  

    def draw(self,context):
        sai_properties = context.scene.SAI_SELECT_properties

        layout = self.layout
        layout.use_property_split = False
        col = layout.column()
        row = col.row(align=True)
        row.prop(sai_properties, "precise", )
        row = col.row(align=True)
        row.label(text="Select Mode:")
        row = col.row(align=True)
        row.prop(sai_properties, "select_expand", expand=True,)
        
class SAI_SELECT_PT_object_mode(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Select Similar Object"
    bl_category = "SaiTools"
    # bl_parent_id = "SAI_SELECT_PT_main"
    def draw(self,context):
        pass

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT'}

class SAI_SELECT_PT_by_dimensions(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "By Dimensions"
    bl_parent_id = "SAI_SELECT_PT_object_mode"
    # bl_options = {'DRAW_BOX', 'HIDE_HEADER','DEFAULT_CLOSED'}  

    def draw(self,context):
        ob = context.object
        sai_properties = context.scene.SAI_SELECT_properties

        layout = self.layout
        layout.use_property_split = False
        
        col = layout.column()
        col.use_property_decorate = False
        row = col.row(align=True)
        row.label(text="Dimensions:")
        row = col.row(align=True)
        row.prop(ob, "dimensions", text="")
        row = col.row(align=True)
        row.label(text="Threshold:")
        row = col.row(align=True)
        row.prop(sai_properties, "dimensions_threshold", text="")
        row = col.row(align=True)
        row.operator('sai_select.by_dimensions')


class SAI_SELECT_PT_by_mesh_count(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "By Mesh Count"
    bl_parent_id = "SAI_SELECT_PT_object_mode"
    # bl_options = {'DRAW_BOX', 'HIDE_HEADER','DEFAULT_CLOSED'}  

    def draw(self,context):
        sai_properties = context.scene.SAI_SELECT_properties

        layout = self.layout
        # layout.use_property_split = False
        
        col = layout.column()
        col.use_property_decorate = False
        row = col.row(align=True)
        row.operator('sai_select.same_vertices_count')
        row = col.row(align=False)
        row.prop(sai_properties, "mesh_vertex_threshold",)

class SAI_SELECT_PT_by_location(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "By Location"
    bl_parent_id = "SAI_SELECT_PT_object_mode"
    # bl_options = {'DRAW_BOX', 'HIDE_HEADER','DEFAULT_CLOSED'}  

    def draw(self,context):
        sai_properties = context.scene.SAI_SELECT_properties

        layout = self.layout
        # layout.use_property_split = False
        
        col = layout.column()
        col.use_property_decorate = False
        row = col.row(align=True)
        row.operator('sai_select.same_vertices_count')
        row = col.row(align=False)
        row.prop(sai_properties, "mesh_vertex_threshold",)


classes = (
    SAI_SELECT_PT_main,
    SAI_SELECT_PT_settings,
    SAI_SELECT_PT_object_mode,
    SAI_SELECT_PT_by_dimensions,
    SAI_SELECT_PT_by_mesh_count,
    SAI_SELECT_PT_by_location,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
