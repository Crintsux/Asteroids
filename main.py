import pygame
from constants import *
from player import Player

def main():
    # Console start message.
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Pygame initializes, game screen sets up, player gets initialized.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    # MAIN GAME LOOP
    while 1:

        # Allows us to quit the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            
        # Make the screen black and move the frame. clock.tick(60) limits the fps to 60
        # and saves delta time into dt variable.
        screen.fill("black")
        player.draw(screen)
        player.update(dt) # Movement controls: W A S D keys (not arrow keys!)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()