#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""project_template.py: A template for python projects.

The Zen of Python, by Tim Peters:
=================================
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

Personal Suggestions:
=====================
At indentation steps extra linebreaks are omitted.
Avoid any complexity at "if __name__ == '__main__':".
Avoid other styles like "import <lib>".
Default shebang is #!/usr/bin/env python.
Don't hack. Design.
Follow the code style of the given project - if it's worth it.
If explicit is too ugly, implicit is better.
If flat is too ugly, nested is better.
Line wrapping after 120 columns.
Name your files like lower_case.py.
Put a class specific main() - if appropriate.
Use braces at ('').join(list).
Use forward slashes for file paths.
Use single quotes by default.
Use the r-prefix (raw) for file paths under windows, instead of manual escape.
Use the x.y.z (major, minor, build) scheme for versioning.
Use, but don't overuse, regex, os.linesep and f-strings.
Watch encoding, target UTF-8 as a default.
"""

__author__ = 'Pat Smith'
__copyright__ = 'Copyright 2099, ProjectName'
__credits__ = ['Sir Toby', 'Anton Placeholder']
__license__ = 'GPL - Put in ./LICENSE directory.'
__version__ = '1.0.1'
__maintainer__ = 'Pat Smith'
__email__ = 'pat.smith@rando.org'
__status__ = 'Development'

import os.path
import sys


class ExampleClass:
    """
    This is a Section Title
    =======================
    Lorem Ipsum.

    This is a Subsection Title
    --------------------------
    Lorem Ipsum.
    """
    def __init__(self):
        """OneLine DocString."""
        # == Section (major) ========================================================================================= #
        self.hello_world = 'Hello World!'
        # -- Section (minor) ----------------------------------------------------------------------------------------- #
        self.cwd = os.path.getctime(r'C:/Windows/system32.dll')

    def print_hello(self):
        """OneLine DocString."""
        print(self.hello_world)
    
    def main(self):
        """OneLine DocString."""
        self.print_hello()
        
    @staticmethod
    def exit():
        print('Good bye!')
        sys.exit(0)


if __name__ == '__main__':
    example = ExampleClass()  # inline comments, placed after two spaces, are not real sentences (just hints)
    example.main()  # Todo: This should be a real sentence, since it is a work instruction!

    ExampleClass.exit()
