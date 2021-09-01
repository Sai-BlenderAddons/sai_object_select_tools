# dont direct regist example class. 


import bpy
import mathutils
import os, json
from bpy_extras.io_utils import ExportHelper, ImportHelper
from . import actions


def round_vector(vector):
    precision = bpy.context.scene.SAI_SELECT_properties.precise
    x = round(vector[0], precision)
    y = round(vector[1], precision)
    z = round(vector[2], precision)
    new_vector = mathutils.Vector((x, y, z))
    
    return new_vector


class SAI_SELECT_OT_by_dimensions(bpy.types.Operator):
    bl_idname = "sai_select.by_dimensions"
    bl_label = "select by dimensions"
    bl_description = "select object by dimensions"


    def execute(self, context):
        result = actions.select_object_by_dimemsions_ot()

        self.report({'INFO'}, str(result) )
        return {"FINISHED"}


class SAI_SELECT_OT_same_vertices_count(bpy.types.Operator):
    bl_idname = "sai_select.same_vertices_count"
    bl_label = "select same vertices count"
    bl_description = "select same vertices count object"


    def execute(self, context):
        result = actions.select_object_by_vertex_count_ot()

        self.report({'INFO'}, str(result) )
        return {"FINISHED"}




classes = (
    SAI_SELECT_OT_by_dimensions,
    SAI_SELECT_OT_same_vertices_count,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
