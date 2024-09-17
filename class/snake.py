
import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake properties
snake_block_size = 10
snake_speed = 15

# Font for displaying score
font_style = pygame.font.SysFont(None, 25)

def display_score(score):
  """Displays the score on the screen."""
  value = font_style.render("Your Score: " + str(score), True, white)
  screen.blit(value, [0, 0])

def draw_snake(snake_block_size, snake_list):
  """Draws the snake on the screen."""
  for x in snake_list:
    pygame.draw.rect(screen, green, [x[0], x[1], snake_block_size, snake_block_size])

def message(msg, color):
  """Displays a message on the screen."""
  mesg = font_style.render(msg, True, color)
  screen.blit(mesg, [screen_width / 6, screen_height / 3])

def game_loop():
  """Main game loop."""
  game_over = False
  game_close = False

  x1 = screen_width / 2
  y1 = screen_height / 2
  x1_change = 0
  y1_change = 0

  snake_list = []
  snake_length = 1

  clock = pygame.time.Clock()

  foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
  foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0

  while not game_over:

    while game_close == True:
      screen.fill(black)
      message("You Lost! Press C-Play Again or Q-Quit", red)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_over = True
            game_close = False
          if event.key == pygame.K_c:
            game_loop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x1_change = -snake_block_size
          y1_change = 0
        elif event.key == pygame.K_RIGHT:
          x1_change = snake_block_size
          y1_change = 0
        elif event.key == pygame.K_UP:
          y1_change = -snake_block_size
          x1_change = 0
        elif event.key == pygame.K_DOWN:
          y1_change = snake_block_size
          x1_change = 0

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
      game_close = True

    x1 += x1_change
    y1 += y1_change
    screen.fill(black)
    pygame.draw.rect(screen, red, [foodx, foody, snake_block_size, snake_block_size])
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
      del snake_list[0]

    for x in snake_list[:-1]:
      if x == snake_head:
        game_close = True

    draw_snake(snake_block_size, snake_list)
    display_score(snake_length - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
      foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0
      snake_length += 1

    clock.tick(snake_speed)

  pygame.quit()
  quit()

game_loop()