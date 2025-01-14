import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Word Bank Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Font for displaying text
font_style = pygame.font.SysFont(None, 30)

# Word bank
word_bank = [
    "python", "javascript", "programming", "computer", "science",
    "algorithm", "data", "structure", "machine", "learning"
]

def display_text(text, color, x, y):
  """Displays text on the screen."""
  text_surface = font_style.render(text, True, color)
  screen.blit(text_surface, (x, y))

def draw_buttons(buttons):
  """Draws buttons on the screen."""
  for button in buttons:
    pygame.draw.rect(screen, blue, button["rect"])
    display_text(button["text"], white, button["rect"].x + 10, button["rect"].y + 10)

def check_button_click(buttons, pos):
  """Checks if a button is clicked."""
  for button in buttons:
    if button["rect"].collidepoint(pos):
      return button["text"]
  return None

def game_loop():
  """Main game loop."""
  running = True
  selected_word = random.choice(word_bank)
  scrambled_word = "".join(random.sample(selected_word, len(selected_word)))
  
  # Create buttons
  button_width = 100
  button_height = 50
  button_spacing = 20
  button_x = (screen_width - (button_width + button_spacing) * 4) / 2
  button_y = 400
  buttons = []
  for i in range(4):
    button_rect = pygame.Rect(button_x + (button_width + button_spacing) * i, button_y, button_width, button_height)
    button_text = random.choice(word_bank)
    buttons.append({"rect": button_rect, "text": button_text})
  # Ensure the correct word is among the options
  buttons[random.randint(0, 3)]["text"] = selected_word

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        clicked_button_text = check_button_click(buttons, pos)
        if clicked_button_text == selected_word:
          display_text("Correct!", green, 300, 200)
          pygame.display.update()
          pygame.time.delay(2000)  # Display "Correct!" for 2 seconds
          game_loop()  # Start a new round
        else:
          display_text("Incorrect!", red, 300, 200)
          pygame.display.update()
          pygame.time.delay(2000)  # Display "Incorrect!" for 2 seconds
          game_loop()  # Start a new round

    screen.fill(white)
    display_text("Scrambled Word: " + scrambled_word, black, 200, 100)
    display_text("Choose the correct word:", black, 200, 200)
    draw_buttons(buttons)
    pygame.display.update()

  pygame.quit()
  quit()

game_loop()