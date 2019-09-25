"""
Kivy example for CP1404
Dynamically create buttons based on content of list
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #     """Construct main app."""
        self.names = ['Linda', 'Russell', 'Peter', 'Anita']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets List Display"
        self.root = Builder.load_file('display_names2.kv')
        self.create_label()
        return self.root

    def create_label(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
