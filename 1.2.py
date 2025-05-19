import pygame, sys
pygame.init()
ekraan = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Aleks Tagirov")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ekraan.fill((0, 0, 0))
    pygame.draw.rect(ekraan, (100, 100, 100), (110, 40, 80, 220))
    pygame.draw.circle(ekraan, (255, 0, 0), (150, 80), 30)
    pygame.draw.circle(ekraan, (255, 255, 0), (150, 150), 30)
    pygame.draw.circle(ekraan, (0, 255, 0), (150, 220), 30)
    pygame.display.flip()

