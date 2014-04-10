
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
"""
USAGE:

class Color(Enum):
	RED = CustomNamedTuple('R', 'Red', 'Red color')
	BLUE = CustomNamedTuple('B', 'Blue', 'Blue color')

if __name__ == '__main__':

	print 'B' in [Color.BLUE, Color.BLUE.id] 	# True
	print 'R' == Color.RED 						# True
	print 'G' in (Color.BLUE,) 					# False
	print 'B' in (Color.BLUE.id,) 			    # True

	print 'Convert to Model choices (tuple of tuples):'
	print Color.choices()
"""
