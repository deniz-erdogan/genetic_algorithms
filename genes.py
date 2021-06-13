import random
import math 
from myvector import myvector
from CONSTANTS import MUTATION_RATE


class Genes:
	def __init__(self, size):
		self.size = size
		self.vectors = [myvector(0,0)]*size
		self.randomize()
		self.step = 0

	
	
	
	def randomize(self):
		for i in range(self.size):
			angle = random.uniform(0, 2*math.pi)
			self.vectors[i] = myvector(math.cos(angle), math.sin(angle))

	def copy(self):
		copied = Genes(self.size)
		for index, gene in enumerate(self.vectors):
			copied.vectors[index] = gene
		
		return copied


	def mutate(self):
		for i in range(self.size):
			num = random.random()
			if num < MUTATION_RATE:
				angle = random.uniform(0, 2*math.pi)
				self.vectors[i] = myvector(math.cos(angle), math.sin(angle))


