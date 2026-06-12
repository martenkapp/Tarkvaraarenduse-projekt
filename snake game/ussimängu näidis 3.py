# Import Modules
import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Define Colours
blue = (26, 1, 249)
green = (5, 135, 36)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 203, 80)
red = (255, 0, 0)


# Create the Squares Class that Will be Used to Make the Snake and the Food
class square():
    n = 15  # Rows
    length = 600  # Length of Display

    def __init__(self, start_position, colour=orange, dx=1, dy=0):
        self.position = start_position
        self.dy = dy
        self.dx = dx
        self.colour = colour

    # Draw Squares
    def draw(self, game_display, eyes=False):
        dd = self.length // self.n
        x_pos = self.position[0]
        y_pos = self.position[1]
        pygame.draw.rect(game_display, self.colour, (x_pos * dd + 1, y_pos * dd + 1, dd - 2, dd - 2))

        # Draw Eyes for Head of the Snake
        if eyes:
            c = dd // 2  # Centerpoint
            r = 3  # Radius
            eye_1 = (x_pos * dd + c - r, y_pos * dd + 8)
            eye_2 = (x_pos * dd + dd - r * 2, y_pos * dd + 8)
            pygame.draw.circle(game_display, black, eye_1, r)
            pygame.draw.circle(game_display, black, eye_2, r)

    # Move Squares
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.position = (self.position[0] + self.dx, self.position[1] + self.dy)


# Create a Class for Snakes
class snake():
    body = []
    turns = {}

    def __init__(self, colour, position):
        self.colour = colour
        self.head = square(position)
        self.body.append(self.head)

    # Move the Snake
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Define How the Game Reacts to Pressing the Arrow Keys
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.position[:]] = [self.dx, self.dy]

                elif keys[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.position[:]] = [self.dx, self.dy]

                elif keys[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.position[:]] = [self.dx, self.dy]

                elif keys[pygame.K_LEFT]:
                    self.dx = -1
                    self.dy = 0
                    self.turns[self.head.position[:]] = [self.dx, self.dy]

        # How the Snake Turns
        for num, square_ in enumerate(self.body):
            t = square_.position[:]
            if t in self.turns:
                turn = self.turns[t]
                square_.move(turn[0], turn[1])
                if num == len(self.body) - 1:
                    self.turns.pop(t)

            else:  # When the Snake Crosses the Edges of the Game Window
                if square_.dx == -1 and square_.position[0] <= 0:
                    square_.position = (square_.n - 1, square_.position[1])
                elif square_.dx == 1 and square_.position[0] >= square_.n - 1:
                    square_.position = (0, square_.position[1])
                elif square_.dy == 1 and square_.position[1] >= square_.n - 1:
                    square_.position = (square_.position[0], 0)
                elif square_.dy == -1 and square_.position[1] <= 0:
                    square_.position = (square_.position[0], square_.n - 1)
                else:
                    square_.move(square_.dx, square_.dy)

    # Reset the Snake
    def reset(self, position):
        self.head = square(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}

    # Add a Square to the Snake After Eating Each Snack
    def add_square(self):
        tail = self.body[-1]
        tdx, tdy = tail.dx, tail.dy

        if tdx == 1 and tdy == 0:
            self.body.append(square((tail.position[0] - 1, tail.position[1])))
        elif tdx == -1 and tdy == 0:
            self.body.append(square((tail.position[0] + 1, tail.position[1])))
        elif tdx == 0 and tdy == 1:
            self.body.append(square((tail.position[0], tail.position[1] - 1)))
        elif tdx == 0 and tdy == -1:
            self.body.append(square((tail.position[0], tail.position[1] + 1)))

        self.body[-1].dx = tdx
        self.body[-1].dy = tdy

    # Draw the Snake
    def draw(self, game_display):
        for num, square_ in enumerate(self.body):
            if num == 0:
                square_.draw(game_display, True)  # Uses Draw Method from Square Class
            else:
                square_.draw(game_display)


# Create the Snack (Apple)
def create_apple(n, item, obstacles):
    body_squares = item.body
    while True:
        x = random.randrange(n)
        y = random.randrange(n)
        if len(list(filter(lambda l: l.position == (x, y), body_squares))) > 0 or len(
                list(filter(lambda l: l.position == (x, y), obstacles))) > 0:
            continue
        else:
            break
    return (x, y)


# Create a Function to Make Obstacles
def create_obstacles(coordinates, colour):
    walls = []
    for c in coordinates:
        walls.append(square(c, colour))
    return walls


# Redraw the Game Window in While Loop
def redraw_win(game_display, coordinates):
    game_display.fill(white)
    sn.draw(game_display)  # Redraw Snake
    apple.draw(game_display)  # Redraw Apple

    # Redraw Obstacles
    for w in walls:
        w.draw(game_display)

    pygame.display.update()


# Message Box After Losing
def message(header, body):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(header, body)
    try:
        root.destroy()
    except:
        pass


# The Main Function to Run the Game
def run():
    global length, n, dist, sn, apple, coordinates, walls  # Define Global Variables
    n = 15
    length = 600
    coordinates = [(3, 3), (3, 4), (3, 5), (6, 8), (7, 8), (8, 8), (9, 8), (2, 12), (2, 13), (2, 14), (10, 1), (11, 1),
                   (12, 1), (12, 2), (12, 3), (12, 12), (12, 13)]

    init_window = pygame.display.set_mode(size=(length, length))  # Create Game Window
    timer = pygame.time.Clock()

    # Create Snake, Obstacles & Apple
    sn = snake(colour=orange, position=(6, 6))
    walls = create_obstacles(coordinates, black)
    apple = square(create_apple(n, sn, walls), colour=green)

    while True:
        pygame.time.delay(50)
        timer.tick(15)

        sn.move()
        if sn.body[0].position == apple.position:
            sn.add_square()
            apple = square(create_apple(n, sn, walls), colour=green)

        for b in range(len(sn.body)):
            if sn.body[b].position in list(map(lambda l: l.position, sn.body[b + 1:])) or sn.body[b].position in list(
                    map(lambda w: w.position, walls)):
                message(header="You Lost!", body="Your score was: {}".format(len(sn.body)))
                sn.reset((6, 6))
                break

        redraw_win(init_window, coordinates)


# Run the Game
run()