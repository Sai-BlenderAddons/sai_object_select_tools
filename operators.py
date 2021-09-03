# dont direct regist example class. 


import bpy
import mathutils
import os, json
from bpy_extras.io_utils import ExportHelper, ImportHelper
from . import actions


class SAI_SELECT_OT_same_dimensions(bpy.types.Operator):
    bl_idname = "sai_select.same_dimensions"
    bl_label = "select same dimensions"
    bl_description = "select same dimensions"


    def execute(self, context):
        sai_properties = bpy.context.scene.SAI_SELECT_properties
        select_mode=sai_properties.select_expand
        result = actions.select_object_by_dimemsions(select_mode=select_mode)

        self.report({'INFO'}, str(result) )
        return {"FINISHED"}

class SAI_SELECT_OT_same_vertices_count(bpy.types.Operator):
    bl_idname = "sai_select.same_vertices_count"
    bl_label = "Same vertices count"
    bl_description = "select same vertices count object"

    def execute(self, context):
        sai_properties = bpy.context.scene.SAI_SELECT_properties
        select_mode=sai_properties.select_expand
        result = actions.select_object_by_vertices(select_mode=select_mode)
        # self.report({'INFO'}, str(result) )
        return {"FINISHED"}

class SAI_SELECT_OT_same_edges_count(bpy.types.Operator):
    bl_idname = "sai_select.same_edges_count"
    bl_label = "Same edges count"
    bl_description = "select same edges count object"

    def execute(self, context):
        sai_properties = bpy.context.scene.SAI_SELECT_properties
        select_mode=sai_properties.select_expand
        result = actions.select_object_by_edges(select_mode=select_mode)

        # self.report({'INFO'}, str(result) )
        return {"FINISHED"}

class SAI_SELECT_OT_same_polygons_count(bpy.types.Operator):
    bl_idname = "sai_select.same_polygons_count"
    bl_label = "Same polygons count"
    bl_description = "select same polygons count object"

    def execute(self, context):
        sai_properties = bpy.context.scene.SAI_SELECT_properties
        select_mode=sai_properties.select_expand
        result = actions.select_object_by_polygons(select_mode=select_mode)

        # self.report({'INFO'}, str(result) )
        return {"FINISHED"}

class SAI_SELECT_OT_same_polygons_area(bpy.types.Operator):
    bl_idname = "sai_select.same_polygons_area"
    bl_label = "Same polygons area"
    bl_description = "select same polygons area object"

    def execute(self, context):
        sai_properties = bpy.context.scene.SAI_SELECT_properties
        select_mode=sai_properties.select_expand
        result = actions.select_object_by_area(select_mode=select_mode)

        self.report({'INFO'}, str(result) )
        return {"FINISHED"}

classes = (
    SAI_SELECT_OT_same_dimensions,
    SAI_SELECT_OT_same_vertices_count,
    SAI_SELECT_OT_same_edges_count,
    SAI_SELECT_OT_same_polygons_count,
    SAI_SELECT_OT_same_polygons_area,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
