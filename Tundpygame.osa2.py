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

#2,1	
import pygame
import sys
import math

pygame.init()

# Värvid
TAEVAS = (135, 206, 250)
MURU = (34, 139, 34)
PAIKE = (255, 223, 0)
SEIN = (255, 240, 180)
KATUS = (101, 67, 33)
KORSTEN = (80, 40, 20)
UKS = (139, 69, 19)
VALGE = (255, 255, 255)
RAAM = (0, 0, 100)
HALL = (100, 100, 100)

# Ekraan
LAIUS, KORGUS = 640, 480
ekraan = pygame.display.set_mode((LAIUS, KORGUS))
pygame.display.set_caption("Ilus maja")
kell = pygame.time.Clock()

def joonista_paike(x, y, r):
    pygame.draw.circle(ekraan, PAIKE, (x, y), r)
    for nurk in range(0, 360, 30):
        dx = int(r * 1.5 * math.cos(math.radians(nurk)))
        dy = int(r * 1.5 * math.sin(math.radians(nurk)))
        pygame.draw.line(ekraan, PAIKE, (x, y), (x + dx, y + dy), 2)

def joonista_maja(x, y, laius, korgus):
    seinakorgus = int(korgus * 0.75)
    katusekorgus = korgus - seinakorgus

    # Seinad
    pygame.draw.rect(ekraan, SEIN, (x, y - seinakorgus, laius, seinakorgus))

    # Katus
    punktid = [(x, y - seinakorgus), (x + laius // 2, y - korgus), (x + laius, y - seinakorgus)]
    pygame.draw.polygon(ekraan, KATUS, punktid)

    # Korsten
    korsten_l = laius // 12
    korsten_k = korgus // 3
    korsten_x = x + laius // 4
    korsten_y = y - korgus - 32
    pygame.draw.rect(ekraan, KORSTEN, (korsten_x, korsten_y, korsten_l, korsten_k))

    # Uks
    ukse_l = laius // 6
    ukse_k = seinakorgus // 2
    pygame.draw.rect(ekraan, UKS, (x + laius // 2 - ukse_l // 2, y - ukse_k, ukse_l, ukse_k))
    pygame.draw.circle(ekraan, HALL, (x + laius // 2 + ukse_l // 3, y - ukse_k // 2), 3)

    # Aken (üks)
    akna_suurus = laius // 6
    ax = x + int(laius * 0.15)
    ay = y - seinakorgus // 2 - akna_suurus // 2
    pygame.draw.rect(ekraan, VALGE, (ax, ay, akna_suurus, akna_suurus))
    pygame.draw.rect(ekraan, RAAM, (ax, ay, akna_suurus, akna_suurus), 2)
    pygame.draw.line(ekraan, RAAM, (ax, ay + akna_suurus // 2), (ax + akna_suurus, ay + akna_suurus // 2), 2)
    pygame.draw.line(ekraan, RAAM, (ax + akna_suurus // 2, ay), (ax + akna_suurus // 2, ay + akna_suurus), 2)

# Peatsükl
toori = True
while toori:
    ekraan.fill(TAEVAS)
    pygame.draw.rect(ekraan, MURU, (0, KORGUS - 80, LAIUS, 80))
    joonista_paike(550, 80, 40)
    joonista_maja(120, KORGUS - 80, 320, 360)

    pygame.display.flip()
    kell.tick(60)

    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            toori = False

pygame.quit()
sys.exit()
