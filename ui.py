# coding=UTF-8
# dont direct regist example class. 

import bpy
from bpy.types import Operator, AddonPreferences, Panel, PropertyGroup
from bpy.props import StringProperty, BoolProperty, IntProperty, CollectionProperty, BoolVectorProperty, PointerProperty, EnumProperty

class EXAMPLE_PT_main_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Example"
    bl_label = "Example Main"
    # bl_options = {"DEFAULT_CLOSED"}   
    def draw(self,context):
        pass

class EXAMPLE_PT_child(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Example"
    bl_label = "Example child"
    bl_parent_id = "EXAMPLE_PT_main_panel"
    # bl_options = {"DEFAULT_CLOSED"}   
    def draw(self,context):
        layout = self.layout
        row = layout.row(align = True)
        #layout.label('Mesh Tools')


classes = (
    EXAMPLE_PT_main_panel,
    EXAMPLE_PT_child,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
