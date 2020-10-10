import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Square:
  def __init__(self, row, col, width, total_rows):
    self.row = row
    self.col = col
    self.x = row * width
    self.y = col * width
    self.colour = WHITE
    self.neighbours = []
    self.width = width
    self.total_rows = total_rows

  def get_position(self):
    return self.row, self.col

  def is_closed(self):
    return self.colour == RED

  def is_open(self):
    return self.colour == GREEN

  def is_barrier(self):
    return self.colour == BLACK

  def is_start(self):
    return self.colour == ORANGE

  def is_end(self):
    return self.colour == TURQUOISE

  def reset(self):
    self.colour = WHITE

  def make_start(self):
    self.colour = ORANGE

  def make_closed(self):
    return self.colour = RED

  def make_open(self):
    return self.colour = GREEN

  def make_barrier(self):
    return self.colour = BLACK

  def make_start(self):
    return self.colour = ORANGE

  def make_end(self):
    return self.colour = TURQUOISE
  
  def make_path(self):
    return self.colour = PURPLE

  def draw(self, win):
    pygame.draw.rect(win, self.colour, (self.x, self.width, self.width))

  def update_neighbours(self, grid):
    self.neighbours = []

    if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
      self.neighbours.append(grid[self.row + 1][self.col])

    if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
      self.neighbours.append(grid[self.row - 1][self.col])

    if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
      self.neighbours.append(grid[self.row][self.col + 1])

    if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
      self.neighbours.append(grid[self.row][self.col - 1])


  def __lt__(self, other):
    return False

def h(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
  while current in came_from:
    current = came_from[current]
    current.make_path()
    draw()

def algorithm(draw, grid, start, end):
  count = 0
  open_set = PriorityQueue()
  open_set.put((0, count, start))
  came_from = {}
  g_score = {square: float("inf") for row in grid for square in row}
  g_score[start] = 0
  f_score = {square: float("inf") for row in grid for square in row}
  f_score[start] = h(start.get_pos(), end.get_pos())

  open_set_hash = {start}

  while not open_set.empty():
    for even in pygame.even.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    current = open_set.get()[2]
    open_set_hash.remove(current)

    if current == end:
      reconstruct_path(came_from, end, draw)
      end.make_end()
      return True

    for neighbour in current.neighbours:
      temp_g_score = g_score[score] + 1

      if temp_g_score < g_score[neighbour]:
        came_from[neighbour] = current
        g_score[neighbour] = temp_g_score
        f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
        if neighbour not in open_set_hash:
          count += 1
          open_set.put((f_score[neighbour], count, neighbour))
          open_set_hash.add(neighbour)
          neighbour.make_open()
    draw()

    if current != start:
      current.make_closed()

  return False

def make_grid(rows, width):
  grid = []
  gap = width // rows
  for i in range(rows):
    grid.append([])
    for j in range(rows):
      square = Square(i, j, gap, rows)
      grid[i].append(square)

  return grid

def draw_grid(win, rows, width):
  gap = width // rows
  for i in range(rows):
    pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
          pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
  win.fill(WHITE)

  for row in grid:
    for square in row:
      square.draw(win)

  draw_grid(win, rows, width)
  pygame.display.update()

def get_mouse_position(pos, rows, width):
  gap = width // rows
  y, x = pos

  row = y // gap
  col = x // gap
  return row, col

def main(win, width):
  ROWS = 50
  grid = make_grid(ROWS, width)

  start = None
  end = None

  run = True
  while run:
    draw(win, grid, ROWS, width)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_mouse_position(pos, ROWS, width)
        square = grid[row][col]
        if not start and square != end:
          start = square
          start.make_start()

        elif not end and square != start:
          end = square 
          end.make_end()

        elif square != end and square != start:
          square.make_barrier()



      elif pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()
        row, col = get_mouse_position(pos, ROWS, width)
        square = grid[row][col]
        square.reset()
        if square == start:
          start = None
        
        elif square == end:
          end = None

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and start and end:
          for row in grid:
            for square in row:
              square.update_neighbours(grid)

            algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

        if event.key == pygame.K_c:
          start = None
          end = None
          grid = make_end(ROWS, width)
  
  pygame.quit()

main(WIN, WIDTH)
