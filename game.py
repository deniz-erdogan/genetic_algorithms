from population import Population
import pygame
from ball import Ball
from CONSTANTS import *
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Genetic Algorithm Game")
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)


FPS = 120
population = Population(100)
font = pygame.font.SysFont(None, 100)

def writeGenCount(gen):
	txt = font.render(f"Generation: {gen}", True, BLACK)
	WIN.blit(txt, (WIDHT/2, 40))
def draw_window():
	WIN.fill(WHITE)
	pygame.draw.rect(WIN, GOAL_COLOR, (GOAL_X, GOAL_Y, 20, 20))

	if population.populationDead():
		population.calculateFitness()
		population.naturalSelection()
		population.mutate()
	else:
		population.update()
		population.show(WIN)

	writeGenCount(population.generation)
	pygame.display.update()

def main():
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window()
	pygame.quit()

if __name__ == "__main__":
	main()