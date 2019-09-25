"""
Kivy example for CP1404
Dynamically create buttons based on content of list
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - list of names
        self.names = ['Linda', 'Russell', 'Peter', 'Anita']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets List Display"
        self.root = Builder.load_file('display_names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_item)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_item(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance that was clicked
        """
        name = instance.text
        # update status text
        self.status_text = "You have clicked on {}".format(name)


DynamicWidgetsApp().run()
