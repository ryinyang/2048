from grid import Grid

class GridStack:
	stk = []
	size = None

	def __init__(self, size=10):
		self.stk = [None for i in range(size)]
		self.size = size

	def __str__(self):
		return str(self.stk)

	def __repr(self):
		return self.__str__()

	def push(self, item):
		if len(self.stk) >= self.size:
			del self.stk[0]
		self.stk.append(item)

	def pop(self):
		if self.stk:
			return self.stk.pop()
		else:
			return None

	def top(self):
		if self.stk:
			return self.stk[len(self.stk)-1]
		else:
			return None