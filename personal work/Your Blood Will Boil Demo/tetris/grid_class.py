import pygame as pg

BLACK = (0, 0, 0)

class Grid:
  def __init__(self, columns:int, rows:int, square_size:tuple, pos:tuple = (0, 0)):
    self.columns = columns
    self.rows = rows
    self.sq_size = square_size
    self.pos = pos

    self.size = (self.columns * self.sq_size[0], self.rows * self.sq_size[1])

    self.vertlines = []
    for x in range(self.columns):
      self.vertlines.append(pg.Rect(self.pos[0] + self.sq_size[0] * x, self.pos[1], 2, self.size[1] + 1))
    self.vertlines.append(pg.Rect(self.pos[0] + self.sq_size[0] * self.columns + 1, self.pos[1], 2, self.size[1] + 1))

    self.horilines = []
    for x in range(self.rows):
      self.horilines.append(pg.Rect(self.pos[0], self.pos[1] + self.sq_size[1] * x, self.size[0] + 1, 2))
    self.horilines.append(pg.Rect(self.pos[0], self.pos[1] + self.sq_size[1] * self.rows + 1, self.size[0] + 1, 2))


  def display(self, surface):
    for rect in self.vertlines:
      pg.draw.rect(surface, BLACK, rect)
    for rect in self.horilines:
      pg.draw.rect(surface, BLACK, rect)