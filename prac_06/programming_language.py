"""CP1404 Practical - Programming Language class."""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines if the type is Dynamic and returns True"""
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.language, self.typing,
                                                                           self.reflection,
                                                                           self.year)
