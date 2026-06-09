import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne5")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Värvid
taust_varv = (200, 230, 255)

# Pildid
pall_img = pygame.image.load("ball.png")
pall_img = pygame.transform.scale(pall_img, (20, 20))

alus_img = pygame.image.load("pad.png")
alus_img = pygame.transform.scale(alus_img, (120, 20))

# Pall
pall_rect = pall_img.get_rect()
pall_rect.center = (WIDTH // 2, HEIGHT // 2)

ballSpeedX = 4
ballSpeedY = 4

# Alus
alus_rect = alus_img.get_rect()
alus_rect.centerx = WIDTH // 2
alus_rect.y = HEIGHT / 1.5

alus_speed = 5

# Skoor
score = 0

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Palli liikumine
    pall_rect.x += ballSpeedX
    pall_rect.y += ballSpeedY

    # Pall põrkub vasakust ja paremast seinast
    if pall_rect.left <= 0 or pall_rect.right >= WIDTH:
        ballSpeedX = -ballSpeedX

    # Pall põrkub ülemisest seinast
    if pall_rect.top <= 0:
        ballSpeedY = -ballSpeedY

    # Kui pall puudutab alumist äärt
    if pall_rect.bottom >= HEIGHT:
        pall_rect.bottom = HEIGHT
        ballSpeedY = -ballSpeedY
        score -= 1

    # Aluse liikumine
    alus_rect.x += alus_speed

    if alus_rect.left <= 0 or alus_rect.right >= WIDTH:
        alus_speed = -alus_speed

    # Kokkupõrge palli ja aluse vahel
    if pall_rect.colliderect(alus_rect) and ballSpeedY > 0:
        pall_rect.bottom = alus_rect.top
        ballSpeedY = -ballSpeedY
        score += 1

    # Joonistamine
    screen.fill(taust_varv)

    screen.blit(pall_img, pall_rect)
    screen.blit(alus_img, alus_rect)

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()