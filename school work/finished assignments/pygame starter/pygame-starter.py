# Arden Boettcher
# 1/31/25
# Pygame Starter

import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SECOND = pygame.event.custom_type()

time = 0

font = pygame.font.Font(None, 50)
drywall = pygame.image.load("school work/finished assignments/pygame starter/drywall.jpg")
drywall = pygame.transform.scale(drywall, (WIDTH, HEIGHT))
pygame.time.set_timer(SECOND, 1000)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Watching Dry Paint") # This is not a typo the paint is already dry
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == SECOND:
      time += 1

  screen.fill(WHITE)
  screen.blit(drywall, (0, 0))
  screen.blit(font.render(str(time), False, BLACK), (25, 550))
  pygame.display.update()

  clock.tick(FPS)

pygame.quit()
sys.exit()