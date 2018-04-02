
class GridStack:

	def __init__(self, size=10):
		"""
		Creates the stack object with default size 10

		:size: number of grids to save
		"""

		self.stk = []
		self.size = size

	def __str__(self):
		return str(self.stk)

	def __repr__(self):
		return self.__str__()

	def push(self, item):
		"""
		Adds a grid to the top of stack.

		:item: 2d array of values on grid
		"""
		if len(self.stk) >= self.size:
			del self.stk[0]
		self.stk.append(item)

	def pop(self):
		"""
		Removes top of stack and returns it

		:return: 2d array of grid
		"""

		if self.stk:
			return self.stk.pop()
		else:
			return None

	def top(self):
		"""
		Peeks at the top of the stack without removing

		:return: most recent 2d array
		"""

		if self.stk:
			return self.stk[-1]
		else:
			return None