# coding=UTF-8
# dont direct regist example class. 

import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty

class EXAMPLE_properties(bpy.types.PropertyGroup):

    filepath : StringProperty(
        default = "//texture",
        subtype="DIR_PATH",
        name = "Texture Folder"
    )
    prefix : StringProperty(
        default = "",
        name = "Prefix",
    )
    filename_ext : EnumProperty(
        items = [
            ('.png','.png','*.png'),
            ('.jpg','.jpg','*.jpg')
            
        ],
        name = 'File Extension'
    )
    materialtype : EnumProperty(
        items = [
            ('Principle','Principle','Principle for cycles or Eevee'),
            ('gltf','gltf','gltf for babylon js')
        
        ],
        name = 'Material Type'
    )
    name_target: EnumProperty(
    name="",
    description="get name from data",
    items=[("OBJECT", "Object", "Object Name"),
            ("DATA", "Data", "Data Name"),
            ("MATERIAL", "Material", "Material Name"),
            ],
    default='MATERIAL',
    )
    case_sensitive : BoolProperty(
        name="Case Sensitive",
        description="Case Sensitive",
        default = True
    ) 
    material_data_file : StringProperty(
        default = "/temp/data.json",
        subtype="FILE_PATH",
        name = "mapping file"
    )

classes = (
    # EXAMPLE_properties,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # bpy.types.Scene.EXAMPLE_properties = bpy.props.PointerProperty(type=EXAMPLE_properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # del bpy.types.Scene.EXAMPLE_properties

if __name__ == '__main__':
    register()
