"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Linda Kirk'


class MilesConvertApp(App):
    """ MilesConvertApp is a Kivy App for converting miles to kilometres"""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root


MilesConvertApp().run()
