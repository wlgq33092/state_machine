#! /usr/bin/env python

import transitions

class Transition(object):
    def __init__(self, transit, name = ''):
        self.transit = transit
        self.name = name


class State(object):
    def __init__(self, name, final = False):
        self.name = name
        self.transition_dict = {}
        self.final = final

    def add_transition(self, transition, state):
        self.transition_dict[transition] = state

    def set_final(self):
        self.final = True

class StateMachine(object):
    def __init__(self, start_state):
        self.start_state = start_state
        self.cur_state = start_state

    def transit(self, input):
        self.cur_state = self.start_state
        while True:
            move = 0
            if self.cur_state.final:
                print "transit final: name is " + self.cur_state.name
                break
            transition_dict = self.cur_state.transition_dict
            for trans in transition_dict.keys():
                if trans.transit(input):
                    self.cur_state = transition_dict[trans]
                    print "cur_state name is " + self.cur_state.name
                    move = 1
                    break
            if move is 0:
                print "input check failed. input is " + input.word
                break

class StateMachineBuilder(object):
    def __init__(self):
        pass


class Pattern(object):
    def __init__(self):
        pass

    def parse_pattern(self, input):
        pass

def Main():
    print 'hello, state machine!'
    cur_is = transitions.cur_is
    ta = Transition(lambda input: cur_is('a', input), 'is a')
    tb = Transition(lambda input: cur_is('b', input), 'is b')
    tc = Transition(lambda input: cur_is('c', input), 'is c')

    s0 = State('0')
    s1 = State('a')
    s2 = State('aa')
    s3 = State('ab')
    s4 = State('ac')
    s5 = State('aac', True)
    s6 = State('abb')
    s7 = State('acc', True)
    s8 = State('aca', True)
    s9 = State('abbc', True)

    s0.add_transition(ta, s1)

    s1.add_transition(ta, s2)
    s1.add_transition(tb, s3)
    s1.add_transition(tc, s4)

    s2.add_transition(tc, s5)
    s3.add_transition(tb, s6)
    s4.add_transition(tc, s7)
    s4.add_transition(ta, s8)
    s6.add_transition(tc, s9)

    sm = StateMachine(s0)
    sm.transit(transitions.Input('aac'))
    sm.transit(transitions.Input('abc'))
    sm.transit(transitions.Input('abbc'))
    sm.transit(transitions.Input('aca'))

if __name__ == '__main__':
    Main()
