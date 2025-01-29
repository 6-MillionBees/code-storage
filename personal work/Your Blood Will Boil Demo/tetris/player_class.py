import pygame as pg
import blocks
from random import randint
from grid_class import Grid

class Player:
  def __init__(self, grid: Grid, scheme):
    self.current_block = None
    self.heldblock = None
    self.grid = grid
    self.score = 0
    self.rects = []

    self.world = []
    self.colorscheme = scheme

    self.newblock()

  def newblock(self):
    x = randint(1, 7)
    if x == 1:
      self.current_block = blocks.Square()
    else:
      self.current_block = blocks.Square()

    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0], self.grid.pos[1] + cordnate[1] * self.grid.sq_size[1]), self.grid.sq_size) for cordnate in self.current_block.cords]

  def movedown(self):
    self.current_block.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.current_block.cords]
    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0], self.grid.pos[1] + cordnate[1]), self.grid.sq_size) for cordnate in self.current_block.cords]

  def display(self):
    pass