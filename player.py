import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.stamina = 100

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        print(self.stamina)
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_LSHIFT] and self.stamina < 100:
            self.stamina += 0.2
        if keys[pygame.K_LSHIFT] and self.stamina > 0: # Sprint when pressing shift.
            dt *= 3
            self.stamina -= 0.9
        # Makes you turn only when not sprinting but allows turning when you're out of stamina.
        if (keys[pygame.K_a] and not keys[pygame.K_LSHIFT]) or (keys[pygame.K_a] and self.stamina <= 0):
            self.rotate(-dt)
        if (keys[pygame.K_d] and not keys[pygame.K_LSHIFT]) or (keys[pygame.K_d] and self.stamina <= 0):
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
