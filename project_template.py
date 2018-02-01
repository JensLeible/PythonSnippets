#!/usr/bin/env python

import sys


class ExampleClass:
    """
    This is a Section Title
    =======================

    This is a Subsection Title
    --------------------------
    This paragraph is in the subsection.
    """

    def __init__(self):
        """OneLine DocString."""
        self.hello_world = 'Hello World!'

    def print_hello(self):
        """OneLine DocString."""
        print(self.hello_world)

    @staticmethod
    def exit():
        print('Good bye!')
        sys.exit(0)


if __name__ == '__main__':

    example = ExampleClass()
    example.print_hello()

    ExampleClass.exit()  # calling a staticmethod
