import bpy
import os
import re

from mathutils import Vector

def get_objects():
    objects = None
    value = bpy.context.scene.AUTOPBR_properties.objects_collection
    if value == 'ALL':
        objects = bpy.context.scene.objects
    elif value == 'SELECTION':
        objects = bpy.context.selected_objects
    
    return objects
