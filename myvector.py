import math
class myvector:
	def __init__(self,x,y):
	    self.x = x
	    self.y = y

	def add(self, otherVector):
		self.x += otherVector.x
		self.y += otherVector.y


	def getMagnitude(self):
		return math.sqrt(self.x**2 + self.y**2)

	def limitVelocity(self, limit: int):
		mag = self.getMagnitude()
		if mag > limit:
			self.x *= (limit/mag)
			self.y *= (limit/mag)