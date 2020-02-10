import pygame


# Base camp
class Home(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.home = pygame.image.load('./images/home/home1.png')
        self.rect = self.home.get_rect()
        self.rect.left, self.rect.top = (3 + 12 * 24, 3 + 24 * 24)
        self.alive = True

    # Base camp is destroyed
    def set_dead(self):
        self.alive = False