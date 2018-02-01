#!/usr/bin/env python

"""
project_template.py:    A template for python (3) projects.

The Zen of Python, by Tim Peters:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

__author__ = "Pat Smith"
__copyright__ = "Copyright 2099, ProjectName"
__credits__ = ["Sir Toby", "Anton Placeholder"]
__license__ = "GPL - Put in ./LICENSE directory."
__version__ = "1.0.1"
__maintainer__ = "Pat Smith"
__email__ = "pat.smith@rando.org"
__status__ = "Production"

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
