import pygame
from constants import *
from player import Player

def main():
    # Console start message.
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # GAME SETUP
    pygame.init() # Pygame initializes

    # Creating groups.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Initializing screen and player.
    Player.containers = (updatable, drawable) # Asigning the player class to groups.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    # MAIN GAME LOOP
    while 1:

        # Allows us to quit the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXIT")
                pygame.quit()
                return
            
            
        screen.fill("black") # Fill the screen with color.
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(dt)
        pygame.display.flip() # Frame forward.
        dt = clock.tick(60) / 1000 # Delta time stored to be used by object methods.

if __name__ == "__main__":
    main()