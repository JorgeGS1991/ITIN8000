import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Create our Main Surface
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Play game Tag!")


# Changed background color
GRASS_GREEN = (217,234,211)

# Sprites
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 40
DEER_SPRITE = pygame.image.load(os.path.join('Assets', 'deerbitmap.png'))
DEER = pygame.transform.scale(DEER_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

WOLF_SPRITE = pygame.image.load(os.path.join('Assets', 'wolfbitmap.png'))
WOLF = pygame.transform.scale(WOLF_SPRITE, (SPRITE_WIDTH, SPRITE_HEIGHT))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
FPS = 60


CAUGHT = pygame.USEREVENT + 1

DEER_HIT = pygame.USEREVENT + 2
# Game Parameters
SPEED = 5


# Define a main function that runs the game
def main():

    deer = pygame.Rect(400, 200, SPRITE_WIDTH, SPRITE_HEIGHT)
    wolf = pygame.Rect(900, 600, SPRITE_WIDTH, SPRITE_HEIGHT)
    deer_lives = 10
    wolf_lives = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # Checks for EVENTS
            if event.type == pygame.QUIT:  # if close clicked
                run = False  # change run to False to break loop

            if event.type == CAUGHT:
                if event.type == deer_lives:
                    deer_lives -= 1

                if event.type == wolf_lives:
                    wolf_lives -= 1

            winner_text = ""
            if deer_lives <= 0:
                winner_text = "Yellow Wins!"

            if wolf_lives <= 0:
                winner_text = "Red Wins!"

            if winner_text != "":
                deer_lives(winner_text)
                break
                run = False
                print('GOTCHA')

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and deer.x - SPEED > 0:
            deer.x -= SPEED
        if keys_pressed[pygame.K_d] and deer.x + SPEED + SPRITE_WIDTH < 1200:
            deer.x += SPEED
        if keys_pressed[pygame.K_w] and deer.y - SPEED > 0:
            deer.y -= SPEED
        if keys_pressed[pygame.K_s] and deer.y + SPEED + SPRITE_HEIGHT < 800:
            deer.y += SPEED

        if keys_pressed[pygame.K_LEFT] and wolf.x - SPEED > 0:
            wolf.x -= SPEED
        if keys_pressed[pygame.K_RIGHT] and wolf.x + SPEED + SPRITE_WIDTH < 1200:
            wolf.x += SPEED
        if keys_pressed[pygame.K_UP] and wolf.y - SPEED > 0:
            wolf.y -= SPEED
        if keys_pressed[pygame.K_DOWN] and wolf.y + SPEED + SPRITE_HEIGHT < 800:  # Wolf Down
            wolf.y += SPEED
        draw_window(deer, wolf)  # This function draws the screen
        deer_tagged(deer, wolf)  # Check if tagged


    pygame.quit()  # will close game


# Draw Window Function
def draw_window(deer, wolf):
    WIN.fill(GRASS_GREEN)  # Draw the Grass
    WIN.blit(DEER, (deer.x, deer.y))  # Sprites
    WIN.blit(WOLF, (wolf.x, wolf.y))  # Sprites
    pygame.display.update()  # Update the screen


# Create a function to determine if tagged
def deer_tagged(deer, wolf):
    if deer.colliderect(wolf):
        pygame.event.post(pygame.event.Event(CAUGHT))


if __name__ == "__main__":
    main()