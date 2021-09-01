import bpy
import os
import re
import mathutils
from mathutils import Vector


def round_vector(vector):
    precision = bpy.context.scene.SAI_SELECT_properties.precise
    x = round(vector[0], precision)
    y = round(vector[1], precision)
    z = round(vector[2], precision)
    new_vector = mathutils.Vector((x, y, z))
    
    return new_vector


def select_object_by_dimemsions():
    sai_properties = bpy.context.scene.SAI_SELECT_properties
    dimensions_threshold = sai_properties.dimensions_threshold
    

    objects = bpy.context.visible_objects

    active_dimensions = round_vector(bpy.context.object.dimensions)
    compare_vector = mathutils.Vector((dimensions_threshold,dimensions_threshold,dimensions_threshold))
    
    for object in objects:
        result = (round_vector(object.dimensions) - active_dimensions) 
        if  result <= compare_vector:
            object.select_set(True)
        else:
            object.select_set(False)

def select_object_by_dimemsions_ot():
    sai_properties = bpy.context.scene.SAI_SELECT_properties
    select_mode = sai_properties.select_expand

    objects = bpy.context.visible_objects
    selected_object = [obj for obj in objects if obj.select_get() == True]

    if select_mode == 'MATCH ONLY':
        select_object_by_dimemsions()
    elif select_mode == 'EXPAND':
        select_object_by_dimemsions()
        [obj.select_set(True) for obj in selected_object]


    return select_mode


def select_object_by_vertex_count():
    sai_properties = bpy.context.scene.SAI_SELECT_properties
    threshold = sai_properties.mesh_vertex_threshold

    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    active_count = len(bpy.context.object.data.vertices)
    same_object = [obj.select_set(True) for obj in objects if len(obj.data.vertices) == active_count]
    bigger_objects = [obj for obj in objects if len(obj.data.vertices) > active_count]
    smaller_objects = [obj for obj in objects if len(obj.data.vertices) > active_count]

    if threshold > 0:
        for obj in bigger_objects:
            if len(obj.data.vertices) <= (active_count + threshold):
                obj.select_set(True)
            else:
                obj.select_set(False)

    if threshold < 0:
        for obj in smaller_objects:
            if (len(obj.data.vertices)-threshold) >= active_count:
                obj.select_set(True)
            else:
                obj.select_set(False)

    # elif threshold < 0:
    #     for obj in smaller_objects:
    #         different = len(obj.data.vertices) - active_count
    #         if different >= threshold:
    #             obj.select_set(True)
    #         else:
    #             obj.select_set(False)


    # for object in objects:
    #     v_count = len(object.data.vertices)
    #     if  v_count == active_count:
    #         object.select_set(True)
    
    #     if threshold > 0:
    #         if v_count > active_count:
    #             if (v_count-threshold) <= 0:
    #                 object.select_set(True)
    #     else:
    #         object.select_set(False)

    return active_count


def select_object_by_vertex_count_ot():
    sai_properties = bpy.context.scene.SAI_SELECT_properties
    select_mode = sai_properties.select_expand
    
    objects = bpy.context.visible_objects
    selected_object = [obj for obj in objects if obj.select_get() == True]


    if select_mode == 'MATCH ONLY':
        select_object_by_vertex_count()
    elif select_mode == 'EXPAND':
        select_object_by_vertex_count()
        [obj.select_set(True) for obj in selected_object]


    return select_mode
