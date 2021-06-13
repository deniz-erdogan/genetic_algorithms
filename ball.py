"""
Ball Class
"""
from random import Random
import math
import pygame
from CONSTANTS import *
from genes import Genes
from myvector import myvector

RADIUS = 10

class Ball:
	def __init__(self):
		self.genes = Genes(1000)
		self.pos = myvector(70, HEIGHT/2)
		self.vel = myvector(0, 0)
		self.acc = myvector(0, 0)

		self.dead = False
		self.reached_goal = False
		self.is_best = False
		self.fitness = 0

		self.color = (255, 0, 102)
		self.fitness = 0



	def draw(self, WIN):
		if self.is_best:
			pygame.draw.circle(WIN, BEST_BALL, (self.pos.x, self.pos.y), RADIUS)
		else:
			pygame.draw.circle(WIN, self.color, (self.pos.x, self.pos.y), RADIUS)


	def move(self):
		if self.genes.step < self.genes.size:
			acc = self.genes.vectors[self.genes.step]
			self.genes.step += 1
			self.vel.add(acc)
			self.vel.limitVelocity(4)
			self.pos.add(self.vel)
		else:
			self.dead = True

	def update(self):
		if (not self.reached_goal) and (not self.dead):
			self.move()
		if not self.is_inside():
			self.dead = True
		elif self.calculateDistancetoGoal() < 10:
			self.reached_goal = True



	def is_inside(self) -> bool:
		if self.pos.x < 0 or self.pos.x > WIDHT or self.pos.y < 0 or self.pos.y > HEIGHT:
			return False
		return True

	def calculateDistancetoGoal(self):
		return math.dist([self.pos.x, self.pos.y], [GOAL_X, GOAL_Y])
	
	def calculateFitness(self):
		if self.reached_goal:
			self.fitness = 1/15 + 10000/(self.genes.step * self.genes.step)
		else:
			dist = self.calculateDistancetoGoal()
			self.fitness = 1/(dist**2)

	def haveBaby(self):
		baby = Ball()
		baby.genes = self.genes.copy()
		return baby
