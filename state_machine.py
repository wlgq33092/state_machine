#! /usr/bin/env python

class State(object):
	def __init__(self, name):
		self.name = name
		self.transition_dict = {}

	def add_transition(self):
		pass



class StateMachine(object):
	def __init__(self, start_state):
		self.start_state = start_state
		self.cur_state = start_state

	def create_state(self):
		pass

class StateMachineBuilder(object):
	def __init__(self):
		pass

class Transition(object):
	def __init__(self):
		pass


class Pattern(object):
	def __init__(self):
		pass

	def parse_pattern(self, input):
		pass
