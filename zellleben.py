import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zellleben")

clock = pygame.time.Clock()

while True:
	clock.tick(60)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill((0,128,128))
	pygame.display.flip()
