#!/usr/bin/env python

"""project_template.py:    A template for python (3) projects.

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

Personal Zen Additions, by ErnestoHoro (git):

Follow the code style of the given project - if anyhow reasonable.
Use comment section blocks with a length of 120 chars to structure blocks of code.
Wrap lines at 120 chars of the current block with a total maximum of 160 chars.
Without indentation wrap lines at 120 chars.
Use linebreaks only for major logical or complex blocks.
At indentation steps extra linebreaks are omitted.
If explicit is too ugly, implicit is better.
If flat is too ugly, nested is better.
Avoid other styles like "import <lib>".
Use single quotes by default, except for docstrings because there they might represent actual spoken language.
Stick to an OOP style.
Avoid any more complexity than basic instantiation, argument parsing, logging- or gui-initialization at "if __name__ ==
'__main__':".
Don't put another useless main().
Always use the r (raw) prefix for file paths under windows, instead of manual escape.
Use os.linesep if appropriate.
Use regex, if appropriate, instead of stacked (e.g.) replace or strip.
Use braces at ('').join(list).
Put #!/usr/bin/env python on top.
Name your files *.py independent of your os-environment.
Encode your application files (!) by default in UTF-8.
Use x.y.z (major, minor, build) scheme for versioning.
Explain the basics of individual code formatting in the 1st docstring section.
"""

__author__ = 'Pat Smith'
__copyright__ = 'Copyright 2099, ProjectName'
__credits__ = ['Sir Toby', 'Anton Placeholder']
__license__ = 'GPL - Put in ./LICENSE directory.'
__version__ = '1.0.1'
__maintainer__ = 'Pat Smith'
__email__ = 'pat.smith@rando.org'
__status__ = 'Production'

import os.path
import sys


class ExampleClass:
    """This line should be used already.
    This is a Section Title
    =======================

    This is a Subsection Title
    --------------------------
    This paragraph is in the subsection.
    """

    def __init__(self):
        """OneLine DocString."""
        self.hello_world = 'Hello World!'
        self.cwd = os.path.getctime(r'C:\Windows\system32.dll')

    def print_hello(self):
        """OneLine DocString."""
        print(self.hello_world)

    @staticmethod
    def exit():
        print('Good bye!')
        sys.exit(0)


if __name__ == '__main__':
    example = ExampleClass()  # inline comments, placed after two spaces, are not real sentences (just hints)
    example.print_hello()  # Todo: This should be a real sentence, since it is a work instruction!

    ExampleClass.exit()
