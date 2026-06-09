import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hiir")

clock = pygame.time.Clock()

# Hele sinine taust
TAUST = (155, 190, 230)

ringid = []
ringi_suurus = 10

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Tumesinine värv
            varv = (0, 0, 139)

            ringid.append([x, y, ringi_suurus, varv])

            # Iga uus ring on suurem
            ringi_suurus += 1

            # Maksimaalselt 10 ringi
            if len(ringid) > 10:
                ringid.pop(0)

    screen.fill(TAUST)

    for ring in ringid:
        x, y, suurus, varv = ring

        # Ainult kontuur
        pygame.draw.circle(
            screen,
            varv,
            (x, y),
            suurus,
            1
        )

    pygame.display.flip()

pygame.quit()