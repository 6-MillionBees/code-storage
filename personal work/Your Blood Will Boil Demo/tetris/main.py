# Arden Boettcher
# 1/28/25
# Tetris

import pygame as pg
import grid_class
import player_class

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))

MOVEDOWN = pg.event.Event(90)

GREY = (120, 120, 120)
BLACK = (0, 0, 0)
YELLOW = (254, 248, 76)
BLUE = (81, 225, 252)
RED = (233, 61, 30)
GREEN = (121, 174, 61)
ORANGE = (121, 174, 61)
DEEP_BLUE = (39, 85, 214)
PINK = (241, 110, 185)

colors = {
  "o": YELLOW,
  "i": BLUE,
  "s": RED,
  "z": GREEN,
  "l": ORANGE,
  "j": DEEP_BLUE,
  "t": PINK
}


def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  player = player_class.Player(grid, colors)

  pg.time.set_timer(MOVEDOWN, 1000)

  alive = True
  while alive:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        quit()
      if event.type == MOVEDOWN:
        player.movedown()
    screen.fill(GREY)
    grid.display(screen)
    pg.display.flip()


def start_menu():
  running = True
  # start_button = pg.Rect()
  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
        break
      if event.type == pg.MOUSEBUTTONDOWN:
        game_loop()



    screen.fill(GREY)
    pg.display.flip()

    clock.tick(60)

def main():
  start_menu()



if __name__ == "__main__":
  main()