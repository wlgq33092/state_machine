#! /usr/bin/env python

class Input(object):
    def __init__(self, word):
        self.word = word
        self.pos = 0
        pass

    def next(self):
        self.pos += 1

    def current(self):
        return self.word[self.pos]


def cur_is(c, input):
    if c == input.current():
        input.next()
        return True
    return False

def is_a(input):
    return cur_is('a', input)

def is_b(input):
    return cur_is('b', input)
