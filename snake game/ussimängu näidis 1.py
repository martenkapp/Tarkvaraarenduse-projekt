import pygame
import random, time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Snake Move..🐍🐍")

# Load Images
circle = pygame.image.load(round.png)  # Ensure this image exists
circle = pygame.transform.scale(circle, (30, 30))
cirX, cirY = 200, 200
circle_list = []
snake_length = 10

font = pygame.font.Font(None, 32)
font_1 = pygame.font.Font(None, 20)
score = 0

foodx = random.randint(0, WIDTH - 50)
foody = random.randint(0, WIDTH - 50)
fruit = pygame.image.load("fruit.png")
fruit = pygame.transform.scale(fruit, (30, 30))

# Velocity
velocity = 3
x, y = velocity, 0  # Initial movement to the right

# Directions
UP = (0, -velocity)
DOWN = (0, velocity)
LEFT = (-velocity, 0)
RIGHT = (velocity, 0)

direction = RIGHT  # Initial direction
next_direction = RIGHT  # Variable to store the next direction change


def score_display(score):
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, [10, 10])

def game_over(score):
    screen.fill((255, 255, 255))  # White background
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over", True, (255, 0, 0))
    text1 = (f"You lose! Your score is: {score}")
    text2 = font_1.render(text1, True, (255, 0, 0))
    screen.blit(text2, (WIDTH // 2 - 80, HEIGHT // 2-10))
    screen.blit(text, (WIDTH // 2 - 90 , HEIGHT // 2 - 70))
    pygame.display.update()
    pygame.time.delay(3000)  # Pause for 3 seconds

# When the game ends, call the function:



def plot_snake(window, snake_list):
    for seg_x, seg_y in snake_list:
        screen.blit(circle, (seg_x, seg_y))


def draw_circles(x, y):
    screen.blit(circle, (x, y))


def game_loop():
    global cirX, cirY, x, y, foodx, foody, snake_length, score, direction, next_direction
    running = True
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    while running:
        # Control the frame rate
        clock.tick(60)  # Limit to 60 frames per second

        # Clear the screen
        screen.fill((0, 0, 0))  # Clear screen before drawing

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Key press event handling with reverse prevention
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    next_direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    next_direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    next_direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    next_direction = RIGHT

        # Apply direction change only if it's not the reverse
        direction = next_direction
        x, y = direction

        # Update circle position
        cirX += x
        cirY += y

        if cirX < 0 or cirX > WIDTH - circle.get_width() or cirY < 0 or cirY > HEIGHT - circle.get_height():
            running = False
            game_over(score)


        # Food collision detection
        if abs(cirX - foodx) < 20 and abs(cirY - foody) < 20:
            foodx = random.randint(0, WIDTH - 50)
            foody = random.randint(0, WIDTH - 50)
            snake_length += 2
            score += 1

        # Update snake body
        head = [cirX, cirY]
        circle_list.append(head)

        if len(circle_list) > snake_length:
            del circle_list[0]

        plot_snake(screen, circle_list)

        # Check if the snake goes out of bounds
        if cirX < 0:
            cirX = 0
        elif cirX > WIDTH - circle.get_width():
            cirX = WIDTH - circle.get_width()
        if cirY < 0:
            cirY = 0
        elif cirY > HEIGHT - circle.get_height():
            cirY = HEIGHT - circle.get_height()

        # Draw the fruit
        screen.blit(fruit, (foodx, foody))
        score_display(score)
        pygame.display.update()  # Update the display


# Run the game
game_loop()
pygame.quit()