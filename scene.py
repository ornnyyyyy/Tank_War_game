import pygame
import random


# Stone wall
class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.brick = pygame.image.load('./images/scene/brick.png')
        self.rect = self.brick.get_rect()
        self.being = False


# Steel wall
class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.iron = pygame.image.load('./images/scene/iron.png')
        self.rect = self.iron.get_rect()
        self.being = False


# Map
class Map():
    def __init__(self, stage):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup  = pygame.sprite.Group()
        if stage == 1:
            self.stage1()
        elif stage == 2:
            self.stage2()
    # Level 1
    def stage1(self):
        for x in [2, 3, 6, 7, 18, 19, 22, 23]:
            for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x in [10, 11, 14, 15]:
            for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x in [4, 5, 6, 7, 18, 19, 20, 21]:
            for y in [13, 14]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x in [12, 13]:
            for y in [16, 17]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
            self.brick = Brick()
            self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
            self.brick.being = True
            self.brickGroup.add(self.brick)
        for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
            self.iron = Iron()
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
            self.iron.being = True
            self.ironGroup.add(self.iron)
    # Level 2
    def stage2(self):
        for x in [2, 3, 6, 7, 18, 19, 22, 23]:
            for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x in [10, 11, 14, 15]:
            for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x in [4, 5, 6, 7, 18, 19, 20, 21]:
            for y in [13, 14]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x in [12, 13]:
            for y in [16, 17]:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brick.being = True
                self.brickGroup.add(self.brick)
        for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
            self.brick = Brick()
            self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
            self.brick.being = True
            self.brickGroup.add(self.brick)
        for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
            self.iron = Iron()
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
            self.iron.being = True
            self.ironGroup.add(self.iron)
    def protect_home(self):
        for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
            self.iron = Iron()
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
            self.iron.being = True
            self.ironGroup.add(self.iron)