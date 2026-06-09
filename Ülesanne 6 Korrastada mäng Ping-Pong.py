import pygame

pygame.init()
pygame.mixer.init()

# Taustamuusika
pygame.mixer.music.load("taustamuusika.mp3")
pygame.mixer.music.play(-1)

# Heliefektid
bounce_sound = pygame.mixer.Sound("hit.mp3")
gameover_sound = pygame.mixer.Sound("lõpp.mp3")

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne5")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

taust_varv = (200, 230, 255)

pall_img = pygame.image.load("ball.png")
pall_img = pygame.transform.scale(pall_img, (20, 20))

alus_img = pygame.image.load("pad.png")
alus_img = pygame.transform.scale(alus_img, (120, 20))

pall_rect = pall_img.get_rect()
pall_rect.centerx = WIDTH // 2
pall_rect.top = 20

ballSpeedX = 4
ballSpeedY = 4

alus_rect = alus_img.get_rect()
alus_rect.centerx = WIDTH // 2
alus_rect.y = HEIGHT / 1.5

alus_speed = 6

score = 0
game_over = False
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        pall_rect.x += ballSpeedX
        pall_rect.y += ballSpeedY

        # Vasak ja parem sein
        if pall_rect.left <= 0 or pall_rect.right >= WIDTH:
            bounce_sound.play()
            ballSpeedX = -ballSpeedX

        # Ülemine sein
        if pall_rect.top <= 0:
            bounce_sound.play()
            ballSpeedY = -ballSpeedY

        # Alumine serv = mäng läbi
        if pall_rect.bottom >= HEIGHT:
            gameover_sound.play()
            game_over = True

        # Aluse juhtimine
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            alus_rect.x -= alus_speed

        if keys[pygame.K_RIGHT]:
            alus_rect.x += alus_speed

        if alus_rect.left < 0:
            alus_rect.left = 0

        if alus_rect.right > WIDTH:
            alus_rect.right = WIDTH

        # Põrge alusega
        if pall_rect.colliderect(alus_rect) and ballSpeedY > 0:
            bounce_sound.play()
            pall_rect.bottom = alus_rect.top
            ballSpeedY = -ballSpeedY
            score += 1

    screen.fill(taust_varv)

    screen.blit(pall_img, pall_rect)
    screen.blit(alus_img, alus_rect)

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(
            text,
            (
                WIDTH // 2 - text.get_width() // 2,
                HEIGHT // 2 - text.get_height() // 2
            )
        )

    pygame.display.flip()

pygame.quit()