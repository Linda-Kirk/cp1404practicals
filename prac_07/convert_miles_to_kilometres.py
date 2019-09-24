"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Linda Kirk'

MILES_TO_KILOMETRES_FACTOR = 1.60934


class MilesConvertApp(App):
    """ MilesConvertApp is a Kivy App for converting miles to kilometres"""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_calculation(self, value):
        value = self.validate_input(value)
        result = value * MILES_TO_KILOMETRES_FACTOR
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        new_value = self.validate_input(self.root.ids.input_number.text)
        new_value += increment
        self.root.ids.input_number.text = str(new_value)

    def validate_input(self, input_number):
        try:
            return float(input_number)
        except ValueError:
            return 0


MilesConvertApp().run()
