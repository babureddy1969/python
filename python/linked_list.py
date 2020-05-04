
class LinkedList:
	def __init__(self):
		self._l = []
		self._currentPosition = 0
	def insert(self,n,pos = None):
		if self._l == []:
			self._l.append(n)
		else :
			if pos == None:
				self._l.insert(pos,n)

	def remove(self,n,pos = None):
		if n in self._l:
			self._l.remove(n)

	def first(self):
		if len(self._l)>0:
			return self._l[0]
		return None
		
	def last(self):
		if len(self._l)>0:
			return self._l[len(self._l)-1]
		return None
		
	def next(self):
		if len(self._l)-1 > self._currentPosition:
			self._currentPosition += 1
			return self._l[self._currentPosition]
		return None
	def prev(self):
		if len(self._l)-1 > self._currentPosition:
			self._currentPosition -= 1
			return self._l[self._currentPosition]
		return None
ll = LinkedList()
ll.insert('a')
print(ll._l)

