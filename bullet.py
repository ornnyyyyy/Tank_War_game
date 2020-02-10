import pygame

# Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Bullets in four directions (up, down, left, and right)
        self.bullets = ['./images/bullet/bullet_up.png', './images/bullet/bullet_down.png',
                        './images/bullet/bullet_left.png', './images/bullet/bullet_right.png']
        # Bullet direction (default up)
        self.direction_x, self.direction_y = 0, -1
        self.bullet = pygame.image.load(self.bullets[0])
        self.rect = self.bullet.get_rect()
        # Assign actual values to the tank class
        self.rect.left, self.rect.right = 0, 0
        # speed
        self.speed = 6
        # Survival
        self.being = False
        # Whether it is an enhanced version of the bullet (breakable steel plate)
        self.stronger = False

    # Change bullet direction
    def turn(self, direction_x, direction_y):
        self.direction_x, self.direction_y = direction_x, direction_y
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet = pygame.image.load(self.bullets[0])
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet = pygame.image.load(self.bullets[1])
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet = pygame.image.load(self.bullets[2])
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet = pygame.image.load(self.bullets[3])
        else:
            raise ValueError('Bullet class -> direction value error.')

    # moving
    def move(self):
        self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
        # Disappear after going to the edge of the map
        if (self.rect.top < 3) or (self.rect.bottom > 630 - 3) or (self.rect.left < 3) or (self.rect.right > 630 - 3):
            self.being = False
