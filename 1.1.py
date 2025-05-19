import pygame
import sys
import math

pygame.init()

LAIUS, KÕRGUS = 800, 600
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.display.set_caption("Lihtne aken")
font = pygame.font.SysFont("arial", 50, bold=True)

SININE = (0, 0, 200)
ROHELINE = (0, 255, 0)
KOLLANE = (255, 255, 0)
HALL = (100, 100, 100)
ROOSA = (255, 0, 255)
TUMEROOSA = (150, 0, 150)
VALGE = (255, 255, 255)
TUMEROHELINE = (0, 100, 0)

bee_image = pygame.image.load("bee.png")
bee_image = pygame.transform.scale(bee_image, (100, 100))

def joonista_päike():
    for nurk in range(0, 360, 5):
        lõpp_x = 100 + 200 * math.cos(math.radians(nurk))
        lõpp_y = 100 + 200 * math.sin(math.radians(nurk))
        pygame.draw.line(ekraan, KOLLANE, (100, 100), (lõpp_x, lõpp_y), 2)

def joonista_pilv():
    pygame.draw.circle(ekraan, HALL, (650, 100), 50)
    pygame.draw.circle(ekraan, HALL, (700, 130), 50)

def joonista_lill():
    for raadius in range(100, 10, -10):
        värv = ROOSA if raadius % 20 == 0 else TUMEROOSA
        pygame.draw.circle(ekraan, värv, (400, 300), raadius, 2)
    pygame.draw.rect(ekraan, TUMEROHELINE, (390, 300, 20, 200))

def joonista_tekst():
    tekst = font.render("Tere tulemast!", True, VALGE)
    ekraan.blit(tekst, (300, 50))

while True:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ekraan.fill(SININE)
    pygame.draw.rect(ekraan, ROHELINE, (0, KÕRGUS // 2, LAIUS, KÕRGUS // 2))

    joonista_päike()
    joonista_pilv()
    joonista_lill()
    joonista_tekst()

    ekraan.blit(bee_image, (340, 100))

    pygame.display.flip()