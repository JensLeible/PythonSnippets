#!/usr/bin/env python

class AddNumber():

    def __init__(self, number):
        self.number = number

    def add_number(self):
        print('Adding number ' + str(self.number))

    def print_random(self):
        print('Random.')


class AddString(object):

    def __init__(self, string):
        self.number = object.__init__(self)
        self.string = string

    def add_number(self):
        print('Adding another number ' + str(self.string))


if __name__ == '__main__':

    add_string = AddString(30)
    add_string.add_number()
    # add_string.print_random()
