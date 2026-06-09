import pygame
import random
from pygame.transform import rotate

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne4")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

taust = pygame.image.load("bg_rally.jpg")

punane_auto = pygame.image.load("f1_red.png")
sinine_auto_img = pygame.image.load("f1_blue.png")
sinine_auto_img = rotate(sinine_auto_img, 180)

lane_x = [170, 320, 470]

punane_lane = 1
punane_rect = punane_auto.get_rect()
punane_rect.centerx = lane_x[punane_lane]
punane_rect.bottom = HEIGHT - 10

sinised = []
siniste_kiirus = 4

for i in range(3):
    while True:
        rect = sinine_auto_img.get_rect()
        rect.centerx = random.choice(lane_x)
        rect.y = random.randint(-700, -50)

        liiga_lähedal = False

        for auto in sinised:
            teine_rect = auto[0]

            if teine_rect.centerx == rect.centerx:
                if abs(teine_rect.y - rect.y) < 120:
                    liiga_lähedal = True
                    break

        if not liiga_lähedal:
            break

    speed = siniste_kiirus
    sinised.append([rect, speed])

score = 0
game_over = False
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                score = 0
                game_over = False

                punane_lane = 1
                punane_rect.centerx = lane_x[punane_lane]
                punane_rect.bottom = HEIGHT - 10

                for car in sinised:
                    rect, speed = car
                    rect.centerx = random.choice(lane_x)
                    rect.y = random.randint(-700, -50)

            if not game_over:
                if event.key == pygame.K_LEFT and punane_lane > 0:
                    punane_lane -= 1
                    punane_rect.centerx = lane_x[punane_lane]

                if event.key == pygame.K_RIGHT and punane_lane < 2:
                    punane_lane += 1
                    punane_rect.centerx = lane_x[punane_lane]

    if not game_over:
        for car in sinised:
            rect, speed = car

            saab_liikuda = True

            for teine_car in sinised:
                teine_rect = teine_car[0]

                if teine_rect != rect:
                    if teine_rect.centerx == rect.centerx:
                        if teine_rect.y > rect.y:
                            if teine_rect.y - rect.y < 120:
                                saab_liikuda = False
                                break

            if saab_liikuda:
                rect.y += speed

            if punane_rect.colliderect(rect):
                game_over = True

            if rect.top > HEIGHT:
                while True:
                    uus_rada = random.choice(lane_x)
                    uus_y = random.randint(-700, -50)

                    liiga_lähedal = False

                    for auto in sinised:
                        teine_rect = auto[0]

                        if teine_rect != rect:
                            if teine_rect.centerx == uus_rada:
                                if abs(teine_rect.y - uus_y) < 120:
                                    liiga_lähedal = True
                                    break

                    if not liiga_lähedal:
                        rect.centerx = uus_rada
                        rect.y = uus_y
                        break

                score += 1

    screen.blit(taust, (0, 0))
    screen.blit(punane_auto, punane_rect)

    for car in sinised:
        screen.blit(sinine_auto_img, car[0])

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        text1 = font.render("GAME OVER", True, (255, 0, 0))
        text2 = font.render("Vajuta R, et uuesti alustada", True, (255, 255, 255))

        screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 10))

    pygame.display.flip()

pygame.quit()
