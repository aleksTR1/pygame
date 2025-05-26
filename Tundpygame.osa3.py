# #3.1. osa
# import pygame, sys
# pygame.init()

# #värvid
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]
# lBlue = [153, 204, 255]

# #ekraani seaded
# screenX = 800
# screenY = 600
# screen = pygame.display.set_mode([screenX, screenY])
# pygame.display.set_caption("Animeerimine")
# screen.fill(lBlue)

# clock = pygame.time.Clock() #3 lisame kella
# ball = pygame.image.load("bee.xcf") #graafika laadimine
# posX, posY = 580, 400 #kiirus ja asukoht
# speedX = 1 #2 lisame samm
# gameover = False

# while not gameover:
#     #fps
#     clock.tick(60) #3 paus
#     #mängu sulgemine ristist
#     events = pygame.event.get()
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
    
#     #pildi lisamine ekraanile
#     screen.blit(ball, (posX, posY))
#     posX -= speedX #2 koordinaadi muutmine ehk liigub vasakule
#     #graafika kuvamine ekraanil
#     pygame.display.flip()
#     screen.fill(lBlue)

# pygame.quit()

#3.2
# import pygame
# import sys

# pygame.init()

# # Värvid
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# pink = (255, 153, 255)
# lGreen = (153, 255, 153)
# lBlue = (153, 204, 255)

# # Ekraani seaded
# screenX = 640
# screenY = 480
# screen = pygame.display.set_mode([screenX, screenY])  # Parandus: oli screen-
# pygame.display.set_caption("Animeerimine_2")
# screen.fill(lBlue)
# clock = pygame.time.Clock()

# # Graafika laadimine (eeldades, et pall.png on olemas)
# try:
#     ball = pygame.image.load("bee.xcf")
# except:
#     # Kui pilti pole, loome lihtsa palli
#     ball = pygame.Surface((50, 50), pygame.SRCALPHA)
#     pygame.draw.circle(ball, red, (25, 25), 25)

# posX, posY = 0, 0  # Algpositsioon
# speedX, speedY = 3, 4  # Kiirus
# gameover = False

# while not gameover:
#     clock.tick(60)
    
#     # Mängu sulgemine ristist
#     for event in pygame.event.get():  # Parandus: oli kaks erinevat eventide kogumist
#         if event.type == pygame.QUIT:
#             gameover = True
    
#     # Pildi lisamine ekraanile
#     screen.fill(lBlue)  # Ekraani puhastamine enne uue kaadri joonistamist
#     screen.blit(ball, (posX, posY))
    
#     # Pall liigutamine
#     posX += speedX
#     posY += speedY
    
#     # Piiride kontroll
#     if posX > screenX - ball.get_rect().width or posX < 0:
#         speedX = -speedX
#     if posY > screenY - ball.get_rect().height or posY < 0:
#         speedY = -speedY
    
#     # Graafika kuvamine ekraanil
#     pygame.display.flip()

# pygame.quit()
# sys.exit()



#3.3
# import pygame
# import sys
# import random

# # Pygame'i initsialiseerimine
# pygame.init()

# # Värvide definitsioon
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# pink = (255, 153, 255)
# lGreen = (153, 255, 153)
# lBlue = (153, 204, 255)

# # Ekraani seaded
# screenX = 640
# screenY = 480
# screen = pygame.display.set_mode([screenX, screenY])
# pygame.display.set_caption("Animeerimine")
# screen.fill(lBlue)
# clock = pygame.time.Clock()

# # Objektide loomine
# coords = []
# for i in range(10):
#     posX = random.randint(1, screenX - 20)  # -20, et ruut mahuks ekraanile
#     posY = random.randint(1, screenY - 20)
#     coords.append([posX, posY])

# gameover = False

# # Peamine mängutsükkel
# while not gameover:
#     clock.tick(60)  # FPS
    
#     # Sündmuste töötlemine
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             gameover = True
    
#     # Ekraani puhastamine
#     screen.fill(lBlue)
    
#     # Ruutude liigutamine ja joonistamine
#     for i in range(len(coords)):
#         pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
#         coords[i][1] += 3  # Liikumiskiirus allapoole
        
#         # Kui ruut jõuab ekraani alla, läheb ta uuesti üles
#         if coords[i][1] > screenY:
#             coords[i][1] = random.randint(-40, -10)
#             coords[i][0] = random.randint(0, screenX - 20)
    
#     # Ekraani värskendus
#     pygame.display.flip()

# # Mängu lõpetamine
# pygame.quit()
# sys.exit()


import pygame
import random
import sys

pygame.init()

# Экран
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rallimäng")

# Шрифт и часы
font = pygame.font.SysFont('Arial', 24)
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Загрузка изображений
player_image = pygame.image.load("player.xcf").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 80))

enemy_images = [
    pygame.transform.scale(pygame.image.load("enemy1.xcf").convert_alpha(), (50, 80)),
    pygame.transform.scale(pygame.image.load("enemy2.xcf").convert_alpha(), (50, 80)),
    pygame.transform.scale(pygame.image.load("enemy3.xcf").convert_alpha(), (50, 80))
]

# Игрок
player_x = screen_width // 2 - 25
player_y = screen_height - 100
player_speed = 5

# Враги
enemy_speed = 4
enemies = []

# Дорожные полосы (x-координаты)
lanes = [screen_width // 4 - 25, screen_width // 2 - 25, 3 * screen_width // 4 - 25]

score = 0
game_over = False

enemy_spawn_timer = 0

# Смещение для движущейся дорожной разметки
line_offset = 0

def create_enemy():
    lane = random.choice(lanes)
    enemy_y = -80
    enemy_img = random.choice(enemy_images)
    enemies.append({"x": lane, "y": enemy_y, "img": enemy_img})

# Создаем стартовых 3 врага
for _ in range(3):
    create_enemy()

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                score = 0
                enemies.clear()
                player_x = screen_width // 2 - 25
                player_y = screen_height - 100
                for _ in range(3):
                    create_enemy()

    if not game_over:
        # Управление игроком
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - 50:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < screen_height - 80:
            player_y += player_speed

        # Движение врагов и проверка столкновений
        for enemy in enemies[:]:
            enemy["y"] += enemy_speed
            if enemy["y"] > screen_height:
                enemies.remove(enemy)
                score += 10
                create_enemy()

            if (player_x < enemy["x"] + 50 and
                player_x + 50 > enemy["x"] and
                player_y < enemy["y"] + 80 and
                player_y + 80 > enemy["y"]):
                game_over = True

    # Отрисовка фона дороги
    road_color = (50, 50, 50)  # темно-серый
    screen.fill(road_color)

    # Боковые границы дороги
    border_color = (180, 180, 180)
    border_width = 20
    pygame.draw.rect(screen, border_color, (lanes[0] - 40, 0, border_width, screen_height))
    pygame.draw.rect(screen, border_color, (lanes[-1] + 50, 0, border_width, screen_height))

    # Пунктирные линии на полосах
    line_color = WHITE
    line_width = 5
    line_height = 40
    line_gap = 20

    # Обновляем смещение для движения линий вниз
    line_offset = (line_offset + enemy_speed) % (line_height + line_gap)

    for lane_x in lanes:
        y = -line_offset
        while y < screen_height:
            pygame.draw.rect(screen, line_color, (lane_x + 22, y, line_width, line_height))
            y += line_height + line_gap

    # Отрисовка игрока
    screen.blit(player_image, (player_x, player_y))

    # Отрисовка врагов
    for enemy in enemies:
        screen.blit(enemy["img"], (enemy["x"], enemy["y"]))

    # Отрисовка счета
    score_text = font.render("Skoor: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))

    # Текст "Game Over"
    if game_over:
        go_text = font.render("MÄNG LÄBI! Vajuta R, et uuesti alustada", True, RED)
        screen.blit(go_text, (screen_width // 2 - 200, screen_height // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()