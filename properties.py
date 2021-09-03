# coding=UTF-8
# dont direct regist example class. 

import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty, FloatVectorProperty
from . import actions


def update_dimensions_threshold(self, context):
    actions.select_object_by_dimemsions(threshold=self.dimensions_threshold)

def update_distance_threshold(self, context): 
    actions.select_object_by_distance(threshold=self.distance_threshold)

def update_vertices_threshold(self, context): 
    actions.select_object_by_vertices(threshold=self.vertices_threshold)

def update_edges_threshold(self, context): 
    actions.select_object_by_edges(threshold=self.edges_threshold)

def update_polygons_threshold(self, context): 
    actions.select_object_by_polygons(threshold=self.polygons_threshold)

def update_area_threshold(self, context): 
    actions.select_object_by_area(threshold=self.area_threshold)

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

    lock_dimensions : BoolProperty(
        name="lock dimensions",
        description="lock dimensions",
        default = True
    ) 
    dimensions_threshold: FloatVectorProperty(
        default=(0.000, 0.000, 0.000),
        subtype='XYZ_LENGTH',
        unit='LENGTH',
        min=0,
        precision=3,
        step=1,
        options={'HIDDEN'},
        name=' ',
        update=update_dimensions_threshold,
    )
    distance_threshold: FloatVectorProperty(
        default=(0.000, 0.000, 0.000),
        subtype='XYZ_LENGTH',
        unit='LENGTH',
        min=0,
        precision=3,
        step=1,
        options={'HIDDEN'},
        name=' ',
        update=update_distance_threshold,
    )


    vertices_threshold: IntProperty(
        default=0,
        min=0,
        step=1,
        options={'HIDDEN'},
        name='vertices threshold',
        update=update_vertices_threshold,
    )
    edges_threshold: IntProperty(
        default=0,
        min=0,
        step=1,
        options={'HIDDEN'},
        name='edges threshold',
        update=update_edges_threshold,
    )
    polygons_threshold: IntProperty(
        default=0,
        min=0,
        step=1,
        options={'HIDDEN'},
        name='polygons threshold',
        update=update_polygons_threshold,
    )
    area_threshold: FloatProperty(
        default=0,
        min=0,
        precision=3,
        step=1,
        options={'HIDDEN'},
        update=update_area_threshold,
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
