#1
# import pygame
# import sys

# pygame.init()  # Pygame'i tööle rakendamiseks

# # värvid
# lGreen = [153, 255, 153]
# lBlue = [153, 204, 255]

# ekraani_pind = pygame.display.set_mode((640, 480))
# ekraani_pind.fill(lGreen)
# pygame.display.set_caption("Esimene mäng")

# # Load image before the game loop
# try:
#     youWin = pygame.image.load("Sigma.png")
#     youWin = pygame.transform.scale(youWin, [300, 200])
# except:
#     print("Could not load image")
#     pygame.quit()
#     sys.exit()

# gameover = False

# while not gameover:
#     # Fill screen with green
#     ekraani_pind.fill(lGreen)
    
#     # Draw the image
#     ekraani_pind.blit(youWin, [180, 100])

#     pygame.display.flip()
    
#     # Handle events
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             gameover = True

# pygame.quit()  # Pygame välja lülitamine
# sys.exit()



#2
# import pygame
# import random
# import sys

# pygame.init()

# # värvid
# r = random.randint(0, 255)
# g = random.randint(0, 255)
# b = random.randint(0, 255)
# varv = [r, g, b]
# lGreen = [153, 255, 153]

# pind = pygame.display.set_mode([640, 480])
# pygame.display.set_caption("Juhuslikud kujundid")
# pind.fill(lGreen)

# # Draw 10 random rectangles
# for i in range(1, 10):
#     x = random.randint(0, 620)
#     y = random.randint(0, 460)
#     pygame.draw.rect(pind, varv, [x, y, 20, 20])

# pygame.display.flip()

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # You could add more drawing/updating code here if you want
#     # the shapes to move or change over time

# pygame.quit()
# sys.exit()



#3
# import pygame
# import sys

# pygame.init()

# # Colors
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]

# # Screen setup
# screen = pygame.display.set_mode([640, 480])
# pygame.display.set_caption("Majake")
# screen.fill(lGreen)

# def draw_house(x, y, width, height, surface, color):
#     """Draw a house with rectangular base and triangular roof"""
#     # Calculate points for the house shape
#     base_height = (3/4) * height
#     points = [
#         (x, y - base_height),  # Top-left of base
#         (x, y),                # Bottom-left
#         (x + width, y),        # Bottom-right
#         (x + width, y - base_height),  # Top-right of base
#         (x, y - base_height),  # Back to top-left (for roof lines)
#         (x + width/2, y - height),     # Roof peak
#         (x + width, y - base_height)   # Top-right of base (for roof)
#     ]
#     line_thickness = 3
#     pygame.draw.lines(surface, color, False, points, line_thickness)

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # Clear screen
#     screen.fill(lGreen)
    
#     # Draw house
#     draw_house(100, 400, 300, 400, screen, red)
    
#     # Update display
#     pygame.display.flip()

# pygame.quit()
# sys.exit()

import pygame
import sys

pygame.init()

# Colors
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
brown = [139, 69, 19]
white = [255, 255, 255]
gray = [200, 200, 200]

# Screen setup
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Majake")
screen.fill(lGreen)

def draw_house(x, y, width, height, surface, color):
    """Draw a house with base, roof, window, and door"""
    base_height = int((3 / 4) * height)
    roof_height = int(height / 4)

    # Base rectangle
    base_rect = pygame.Rect(x, y - base_height, width, base_height)
    pygame.draw.rect(surface, color, base_rect)

    # Roof triangle
    roof_points = [
        (x, y - base_height),
        (x + width // 2, y - height),
        (x + width, y - base_height)
    ]
    pygame.draw.polygon(surface, pink, roof_points)

    # Door
    door_width = width // 5
    door_height = base_height // 2
    door_rect = pygame.Rect(x + width // 2 - door_width // 2, y - door_height, door_width, door_height)
    pygame.draw.rect(surface, brown, door_rect)

    # Window
    window_size = width // 5
    window_rect = pygame.Rect(x + width // 4 - window_size // 2, y - base_height + 20, window_size, window_size)
    pygame.draw.rect(surface, white, window_rect)
    pygame.draw.line(surface, gray, window_rect.topleft, window_rect.bottomright, 2)
    pygame.draw.line(surface, gray, window_rect.topright, window_rect.bottomleft, 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill(lGreen)
    
    # Draw house
    draw_house(150, 400, 300, 300, screen, red)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()