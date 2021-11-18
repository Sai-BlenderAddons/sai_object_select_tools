# dont direct regist example class. 

import bpy

class EXAMPLE_preferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    # bl_idname = get_addon_name()


    tab_menu: bpy.props.EnumProperty(
        name="Tab", description="", 
        items=[
            ('Info', "Info", "", "INFO", 0),
            ('Link', "Link", "", "URL", 1)], 
        default='Info')

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.prop(self,"tab_menu",expand=True)

        if self.tab_menu == "Info":
            layout.use_property_split = True
            layout.label(text = "Update : 20210831")

        elif self.tab_menu == "Link":
            row = layout.row()
            row.label(text="Link:",icon="NONE")
            row.operator( "wm.url_open", text="Moonshine VFX", icon="URL").url = "https://www.moonshine.tw"

            row = layout.row()
            row.label(text="",icon="NONE")
            row.operator( "wm.url_open", text="Developer Github", icon="URL").url = "https://github.com/SaiZyca" 

classes = (
    EXAMPLE_preferences,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    

if __name__ == '__main__':
    register()
