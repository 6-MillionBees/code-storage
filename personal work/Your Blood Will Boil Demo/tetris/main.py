# Arden Boettcher
# 1/28/25
# Tetris

import pygame as pg
import grid_class
import player_class

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))

GREY = (120, 120, 120)
BLACK = (0, 0, 0)

def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  player = player_class.Player(grid)

  alive = True
  while alive:
    break


def start_menu():
  running = True
  start_button = pg.Rect()
  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
        break



    screen.fill(GREY)
    pg.display.flip()

    clock.tick(60)

def main():
  start_menu()



if __name__ == "__main__":
  main()