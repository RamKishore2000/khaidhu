from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout

# Define the main screen layout in KV language
KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: "10dp"
    spacing: "10dp"
    
    MDLabel:
        id: label
        text: "Hello, KivyMD!"
        halign: "center"
        theme_text_color: "Secondary"
        
    MDRaisedButton:
        text: "Change Text"
        size_hint: None, None
        size: "200dp", "50dp"
        pos_hint: {"center_x": 0.5}
        on_press: app.change_text()
'''

class Ram(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_text(self):
        # Change the text of the label when the button is pressed
        label = self.root.ids.label
        label.text = "Text Changed!"

# Run the app
if __name__ == "__main__":
    Ram().run()
