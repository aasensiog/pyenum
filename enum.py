from collections import namedtuple

class CustomNamedTuple(namedtuple('Enumeration', 'id short desc')):
	def __eq__(self, other):
		if self.id:
			return self.id == other
		return self == other

class Enum(object):
	@classmethod
	def choices(self):
		d = self.__dict__
		return tuple([(d[x].id, d[x].desc) for x in [y for y in d if not y.startswith('__')]])

	@classmethod
	def valid_values(self):
		d = self.__dict__
		return [d[x].id for x in [y for y in d if not y.startswith('__')]]

	@classmethod
	def is_valid(self, value):
		return value in self.valid_values()
