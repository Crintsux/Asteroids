import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Console start message.
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # GAME SETUP
    pygame.init() # Pygame initializes

    # Creating groups.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Asigning classes to their groups.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Initializing screen and player.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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
        for object in asteroids:
            for bullet in shots:
                if object.collision_check(bullet):
                    bullet.kill()
                    object.split()
            if object.collision_check(player):
                print("GAME OVER")
                pygame.quit()
                return
        pygame.display.flip() # Frame forward.
        dt = clock.tick(60) / 1000 # Delta time stored to be used by object methods.

if __name__ == "__main__":
    main()