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


def select_object_by_dimemsions(select_mode='MATCH ONLY', threshold=Vector((0, 0, 0))):
    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    selected_object = [obj for obj in objects if obj.select_get() == True]


    for object in objects:
        x = abs(object.dimensions[0]-bpy.context.object.dimensions[0])
        y = abs(object.dimensions[1]-bpy.context.object.dimensions[1])
        z = abs(object.dimensions[2]-bpy.context.object.dimensions[2])

        if x <= threshold[0] and y <= threshold[1] and z <= threshold[2]:
            object.select_set(True) 
        else:
            object.select_set(False)

    if select_mode == 'EXPAND':
        [object.select_set(True) for object in selected_object]

    return {"FINISHED"}

def select_object_by_distance(threshold=Vector((0, 0, 0))):
    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']

    for object in objects:
        x = abs(object.location[0]-bpy.context.object.location[0])
        y = abs(object.location[1]-bpy.context.object.location[1])
        z = abs(object.location[2]-bpy.context.object.location[2])

        if x <= threshold[0] and y <= threshold[1] and z <= threshold[2]:
            object.select_set(True) 
        else:
            object.select_set(False)

    return {"FINISHED"}

def select_object_by_vertices(select_mode='MATCH ONLY', threshold=0):
    
    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    count = len(bpy.context.object.data.vertices)
    selected_object = [obj for obj in objects if obj.select_get() == True]

    for object in objects:
        if abs(len(object.data.vertices) - count) <= threshold:
            object.select_set(True) 
        else:
            object.select_set(False)

    if select_mode == 'EXPAND':
        [object.select_set(True) for object in selected_object]

    return select_mode


def select_object_by_edges(select_mode='MATCH ONLY', threshold=0):
    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    count = len(bpy.context.object.data.edges)
    selected_object = [obj for obj in objects if obj.select_get() == True]

    for object in objects:
        if abs(len(object.data.edges) - count) <= threshold:
            object.select_set(True) 
        else:
            object.select_set(False)

    if select_mode == 'EXPAND':
        [object.select_set(True) for object in selected_object]

    return select_mode

def select_object_by_polygons(select_mode='MATCH ONLY', threshold=0):
    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    count = len(bpy.context.object.data.polygons)
    selected_object = [obj for obj in objects if obj.select_get() == True]

    for object in objects:
        if abs(len(object.data.polygons) - count) <= threshold:
            object.select_set(True) 
        else:
            object.select_set(False)

    if select_mode == 'EXPAND':
        [object.select_set(True) for object in selected_object]

    return select_mode


def select_object_by_area(select_mode='MATCH ONLY', threshold=0):
    
    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    selected_object = [obj for obj in objects if obj.select_get() == True]
    count = round(sum([poly.area for poly in bpy.context.object.data.polygons]), 9)

    for object in objects:
        area_size = round(sum([poly.area for poly in object.data.polygons]), 9)
        if abs(area_size - count) <= threshold:
            object.select_set(True) 
        else:
            object.select_set(False)

    if select_mode == 'EXPAND':
        [obj.select_set(True) for obj in selected_object]

    return count

def sort_object_by_vertices_count(is_reverse=False):

    objects = [obj for obj in bpy.context.visible_objects if obj.type == 'MESH']
    objects.sort(reverse=is_reverse, key = lambda object: len(object.data.vertices))

    return objects