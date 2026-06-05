import pygame

pygame.init()

# Ekraani suurus
LAIUS = 640
KORGUS = 480

screen = pygame.display.set_mode((LAIUS, KORGUS))
pygame.display.set_caption("Harjutamine")

# Taustavärv
TAUST = (200, 255, 200)


def joonista_ruudustik(ruudu_suurus, veerud, read, joone_varv):
    """
    Joonistab ekraanile ruudustiku.

    ruudu_suurus - ühe ruudu külje pikkus pikslites
    veerud - veergude arv
    read - ridade arv
    joone_varv - joonte värv (RGB)
    """

    # Vertikaalsed jooned
    for x in range(veerud + 1):
        pygame.draw.line(
            screen,
            joone_varv,
            (x * ruudu_suurus, 0),
            (x * ruudu_suurus, read * ruudu_suurus)
        )

    # Horisontaalsed jooned
    for y in range(read + 1):
        pygame.draw.line(
            screen,
            joone_varv,
            (0, y * ruudu_suurus),
            (veerud * ruudu_suurus, y * ruudu_suurus)
        )


# Parameetrid
RUUDU_SUURUS = 20
VEERUD = 32
READ = 24
JOONE_VARV = (255, 0, 0)

running = True
while running:

    # Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tausta värvimine
    screen.fill(TAUST)

    # Ruudustiku joonistamine
    joonista_ruudustik(
        RUUDU_SUURUS,
        VEERUD,
        READ,
        JOONE_VARV
    )

    pygame.display.flip()

pygame.quit()