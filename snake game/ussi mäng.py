# Impordime PyGame teegi mängu tegemiseks
import pygame

# Impordime random teegi juhuslike asukohtade jaoks
import random

# Käivitame PyGame'i
pygame.init()

# Määrame akna laiuse
LAIUS = 800

# Määrame akna kõrguse
KORGUS = 600

# Määrame ühe mänguruudu suuruse
RUUT = 20

# Loome mänguakna
aken = pygame.display.set_mode((LAIUS, KORGUS))

# Paneme aknale pealkirja
pygame.display.set_caption("Minu Ussimäng")

# Loome mängukella kiiruse kontrollimiseks
kell = pygame.time.Clock()

# Määrame värvid
MUST = (0, 0, 0)
VALGE = (255, 255, 255)
ROHELINE = (0, 200, 0)
PUNANE = (220, 0, 0)
KOLLANE = (255, 220, 0)
HALL = (120, 120, 120)

# Loome teksti fondi
font = pygame.font.SysFont("arial", 28)

# Loome suurema fondi pealkirjade jaoks
suur_font = pygame.font.SysFont("arial", 48)


# Funktsioon teksti kuvamiseks
def kuva_tekst(tekst, x, y, varv=VALGE, suur=False):
    # Valime õige fondi
    kasutatav_font = suur_font if suur else font

    # Loome tekstipildi
    tekstipilt = kasutatav_font.render(tekst, True, varv)

    # Kuvame teksti ekraanile
    aken.blit(tekstipilt, (x, y))


# Funktsioon juhusliku koha leidmiseks
def juhuslik_koht():
    # Leiame juhusliku x-koordinaadi
    x = random.randrange(0, LAIUS, RUUT)

    # Leiame juhusliku y-koordinaadi
    y = random.randrange(0, KORGUS, RUUT)

    # Tagastame koordinaadid
    return [x, y]


# Funktsioon takistuste loomiseks
def loo_takistused(kogus):
    # Loome tühja takistuste listi
    takistused = []

    # Loome takistusi, kuni neid on piisavalt
    while len(takistused) < kogus:

        # Leiame uue juhusliku koha
        koht = juhuslik_koht()

        # Kontrollime, et takistus ei oleks juba olemas
        if koht not in takistused:

            # Lisame takistuse listi
            takistused.append(koht)

    # Tagastame takistused
    return takistused


# Peamine mängufunktsioon
def mang():
    # Määrame ussi algse x-asukoha
    uss_x = LAIUS // 2

    # Määrame ussi algse y-asukoha
    uss_y = KORGUS // 2

    # Määrame algse liikumise paremale
    dx = RUUT

    # Määrame algse y-liikumise nulliks
    dy = 0

    # Loome ussi keha listina
    uss = [[uss_x, uss_y]]

    # Määrame ussi algse pikkuse
    pikkus = 1

    # Loome tavalise toidu
    toit = juhuslik_koht()

    # Loome boonustoidu
    boonustoit = juhuslik_koht()

    # Määrame, et boonustoit pole alguses nähtav
    boonus_nahtav = False

    # Määrame boonustoidu aja
    boonus_aeg = 0

    # Loome takistused
    takistused = loo_takistused(10)

    # Määrame algse skoori
    skoor = 0

    # Määrame algse kiiruse
    kiirus = 10

    # Määrame mängu tööle
    mang_kaib = True

    # Peamine mängutsükkel
    while mang_kaib:

        # Käime läbi kõik sündmused
        for event in pygame.event.get():

            # Kui kasutaja sulgeb akna
            if event.type == pygame.QUIT:

                # Sulgeme PyGame'i
                pygame.quit()

                # Lõpetame programmi
                quit()

            # Kui kasutaja vajutab klahvi
            if event.type == pygame.KEYDOWN:

                # MUUDATUS 1: vastassuunas liikumise keelamine
                # Kui uss liigub vasakule/paremale, ei saa kohe vastassuunas minna

                # Kui vajutatakse vasakule ja uss ei liigu horisontaalselt
                if event.key == pygame.K_LEFT and dx == 0:

                    # Paneme ussi liikuma vasakule
                    dx = -RUUT

                    # Peatame vertikaalse liikumise
                    dy = 0

                # Kui vajutatakse paremale ja uss ei liigu horisontaalselt
                elif event.key == pygame.K_RIGHT and dx == 0:

                    # Paneme ussi liikuma paremale
                    dx = RUUT

                    # Peatame vertikaalse liikumise
                    dy = 0

                # Kui vajutatakse üles ja uss ei liigu vertikaalselt
                elif event.key == pygame.K_UP and dy == 0:

                    # Peatame horisontaalse liikumise
                    dx = 0

                    # Paneme ussi liikuma üles
                    dy = -RUUT

                # Kui vajutatakse alla ja uss ei liigu vertikaalselt
                elif event.key == pygame.K_DOWN and dy == 0:

                    # Peatame horisontaalse liikumise
                    dx = 0

                    # Paneme ussi liikuma alla
                    dy = RUUT

        # Liigutame ussi x-koordinaati
        uss_x += dx

        # Liigutame ussi y-koordinaati
        uss_y += dy

        # Loome ussi uue pea
        pea = [uss_x, uss_y]

        # Kontrollime, kas uss läks vastu seina
        if uss_x < 0 or uss_x >= LAIUS or uss_y < 0 or uss_y >= KORGUS:

            # Lõpetame mängu
            mang_kaib = False

        # Lisame uue pea ussi listi
        uss.append(pea)

        # Kui uss on liiga pikk
        if len(uss) > pikkus:

            # Eemaldame saba
            del uss[0]

        # Kontrollime, kas uss sõitis enda vastu
        if pea in uss[:-1]:

            # Lõpetame mängu
            mang_kaib = False

        # MUUDATUS 2: takistused mänguväljal
        # Kui uss sõidab halli takistuse vastu, lõpeb mäng
        if pea in takistused:

            # Lõpetame mängu
            mang_kaib = False

        # Kontrollime, kas uss sõi tavalise toidu
        if pea == toit:

            # Suurendame ussi pikkust ühe võrra
            pikkus += 1

            # Lisame ühe punkti
            skoor += 1

            # Loome uue toidu
            toit = juhuslik_koht()

            # MUUDATUS 3: boonustoit
            # Vahel ilmub kollane boonustoit, mis annab rohkem punkte
            if random.randint(1, 4) == 1:

                # Teeme boonustoidu nähtavaks
                boonus_nahtav = True

                # Anname boonustoidule uue koha
                boonustoit = juhuslik_koht()

                # Boonustoit on nähtav piiratud aja
                boonus_aeg = 80

        # Kui boonustoit on nähtav ja uss sööb selle ära
        if boonus_nahtav and pea == boonustoit:

            # Suurendame ussi pikkust kolme võrra
            pikkus += 3

            # Lisame viis punkti
            skoor += 5

            # Peidame boonustoidu
            boonus_nahtav = False

        # Kui boonustoit on nähtav
        if boonus_nahtav:

            # Vähendame boonustoidu aega
            boonus_aeg -= 1

            # Kui aeg saab otsa
            if boonus_aeg <= 0:

                # Peidame boonustoidu
                boonus_nahtav = False

        # MUUDATUS 4: kiiruse suurenemine mängu jooksul
        # Iga 5 punkti järel muutub mäng kiiremaks
        kiirus = 10 + skoor // 5

        # Värvime tausta mustaks
        aken.fill(MUST)

        # Joonistame tavalise toidu punasena
        pygame.draw.rect(aken, PUNANE, (toit[0], toit[1], RUUT, RUUT))

        # Kui boonustoit on nähtav
        if boonus_nahtav:

            # Joonistame boonustoidu kollasena
            pygame.draw.rect(aken, KOLLANE, (boonustoit[0], boonustoit[1], RUUT, RUUT))

        # Joonistame kõik takistused
        for takistus in takistused:

            # Joonistame ühe takistuse hallina
            pygame.draw.rect(aken, HALL, (takistus[0], takistus[1], RUUT, RUUT))

        # Joonistame ussi
        for osa in uss:

            # Joonistame ühe ussi kehaosa rohelisena
            pygame.draw.rect(aken, ROHELINE, (osa[0], osa[1], RUUT, RUUT))

        # MUUDATUS 5: skoori ja kiiruse kuvamine ekraanil
        # Kuvame mängijale hetkeseisu
        kuva_tekst(f"Skoor: {skoor}", 10, 10)

        # Kuvame mängu kiiruse
        kuva_tekst(f"Kiirus: {kiirus}", 10, 40)

        # Uuendame ekraani
        pygame.display.update()

        # Määrame mängu kiiruse
        kell.tick(kiirus)

    # Kui mäng lõppeb, avame lõpuakna
    lopuaken(skoor)


# Mängu lõpu funktsioon
def lopuaken(skoor):
    # Lõpuaken töötab seni, kuni kasutaja valib tegevuse
    while True:

        # Värvime tausta mustaks
        aken.fill(MUST)

        # Kuvame mängu lõpu teksti
        kuva_tekst("Mäng läbi!", 280, 170, PUNANE, True)

        # Kuvame mängija skoori
        kuva_tekst(f"Sinu skoor: {skoor}", 300, 250)

        # MUUDATUS 6: taaskäivitamise ekraan
        # Kasutaja saab mängu uuesti alustada ilma programmi sulgemata
        kuva_tekst("ENTER - mängi uuesti", 270, 330)

        # Kuvame väljumise juhise
        kuva_tekst("ESC - välju mängust", 290, 370)

        # Uuendame ekraani
        pygame.display.update()

        # Käime läbi sündmused
        for event in pygame.event.get():

            # Kui kasutaja sulgeb akna
            if event.type == pygame.QUIT:

                # Sulgeme PyGame'i
                pygame.quit()

                # Lõpetame programmi
                quit()

            # Kui kasutaja vajutab klahvi
            if event.type == pygame.KEYDOWN:

                # Kui kasutaja vajutab ENTER
                if event.key == pygame.K_RETURN:

                    # Käivitame mängu uuesti
                    mang()

                # Kui kasutaja vajutab ESC
                if event.key == pygame.K_ESCAPE:

                    # Sulgeme PyGame'i
                    pygame.quit()

                    # Lõpetame programmi
                    quit()


# Käivitame mängu
mang()