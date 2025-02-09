import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, STAMINA_REGEN_RATE, STAMINA_SPENT, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius = PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.stamina = 100
        self.shoot_cd = 0

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

    def shoot(self):
        # Prevents shooting when shoot is on CD.
        if self.shoot_cd > 0:
            return
        # Spawns the shot itself.
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cd = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        # print(self.stamina) # Placeholder stamina check.
        keys = pygame.key.get_pressed()

        # Shoot ability cooldown countdown.
        if self.shoot_cd != 0:
            self.shoot_cd -= dt

        # Stamina regeneration.
        if not keys[pygame.K_LSHIFT] and self.stamina < 100:
            self.stamina = min(self.stamina + STAMINA_REGEN_RATE, 100)
        # Sprint implementation.
        if keys[pygame.K_LSHIFT] and self.stamina > 0:
            dt *= 3
            self.stamina = max(self.stamina - STAMINA_SPENT, 0)
        
        # Restrics turning for when you're sprinting aside from when you're out of stam.
        can_turn = not keys[pygame.K_LSHIFT] or self.stamina <= 0

        # Main controls.
        if keys[pygame.K_a] and can_turn:
            self.rotate(-dt)
        if keys[pygame.K_d] and can_turn:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
