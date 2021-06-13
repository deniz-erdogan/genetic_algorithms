from math import trunc
from ball import *
import random
class Population:
	def __init__(self, size) -> None:
		self.size = size
		self.balls = [Ball()]*size

		for i in range(self.size):
			self.balls[i] = Ball()			

		self.generation = 1
		self.bestball = 0
		self.minstep = 500
		self.fitnessSum = 0


	def show(self, WIN):
		for ball in self.balls:
			ball.draw(WIN)

		self.balls[0].draw(WIN)
	

	def update(self):
		for ball in self.balls:
			if ball.genes.step > self.minstep:
				ball.dead = True
			else:
				ball.update()

	
	def calculateFitness(self):
		for ball in self.balls:
			ball.calculateFitness()


	def populationDead(self):
		for ball in self.balls:
			if not ball.dead and not ball.reached_goal:
				return False
		return True


	def findBestBall(self):
		maxFitness = 0
		maxIndex = 0
		for index, ball in enumerate(self.balls):
			if ball.fitness > maxFitness:
				maxFitness = ball.fitness
				maxIndex = index
		
		self.bestball = maxIndex

		if self.balls[maxIndex].reached_goal:
			self.minstep = self.balls[maxIndex].genes.step
			print(f"minstep = {self.minstep}")


	def sumFitness(self):
		self.fitnessSum = 0
		for ball in self.balls:
			self.fitnessSum += ball.fitness


	def selectParent(self):
		num = random.uniform(0.0, self.fitnessSum)
		accumulator = 0

		for ball in self.balls:
			accumulator += ball.fitness
			if accumulator > num:
				return ball
		
		return None

	def naturalSelection(self):
		self.findBestBall()
		self.sumFitness()
		newgen = [None]*self.size

		newgen[0] = self.balls[self.bestball].haveBaby()
		newgen[0].is_best = True

		for i in range(1, self.size):
			parent = self.selectParent()
			newgen[i] = parent.haveBaby()
		
		self.balls = newgen.copy()
		self.generation += 1


	def mutate(self):
		for ball in self.balls:
			ball.genes.mutate()

	