# coding=UTF-8
# dont direct regist example class. 

import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty, FloatVectorProperty
from . import actions


def update_dimensions_threshold(self, context):
    result = actions.select_object_by_dimemsions()


def update_mesh_vertex_threshold(self, context):
    actions.select_object_by_vertex_count()


class SAI_SELECT_properties(bpy.types.PropertyGroup):
    precise: IntProperty(
        default=3,
        name='Precise',
        options={'HIDDEN'},
    )
    select_expand:EnumProperty(
        items=[
            ('EXPAND', 'Expand', 'retain corrent selection'),
            ('MATCH ONLY', 'Match Only', 'select only matched')
        ],
        default='EXPAND',
        name='expand',
        options={'HIDDEN'},
    )
    compare: EnumProperty(
        items=[
            ('>', '>', '>'),
            ('=', '=', '='),
            ('<', '<', '<'),
        ],
        default='=',
        name='compare',
        options={'HIDDEN'},
    )

    dimensions_difference: FloatVectorProperty(
        default=(0.000000, 0.000000, 0.000000),
        min=0,
        precision=6,
        step=1,
        options={'HIDDEN'},
        unit='LENGTH',
        update=update_dimensions_threshold,
    )
    dimensions_threshold: FloatProperty(
        default=0,
        min=0,
        precision=3,
        step=1,
        options={'HIDDEN'},
        update=update_dimensions_threshold,
    )

    mesh_vertex_threshold: IntProperty(
        default=0,
        step=1,
        options={'HIDDEN'},
        update=update_mesh_vertex_threshold,
        name='vertex threshold',
    )



classes = (
    SAI_SELECT_properties,
    # EXAMPLE_properties,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # bpy.types.Scene.EXAMPLE_properties = bpy.props.PointerProperty(type=EXAMPLE_properties)
    bpy.types.Scene.SAI_SELECT_properties = bpy.props.PointerProperty(type=SAI_SELECT_properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # del bpy.types.Scene.EXAMPLE_properties
    del bpy.types.Scene.SAI_SELECT_properties

if __name__ == '__main__':
    register()
