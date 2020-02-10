import pygame
import random


# Food, used to enhance tank capacity
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Destroy all current enemies
        self.food_boom = './images/food/food_boom.png'
        # All current enemies are still for a while
        self.food_clock = './images/food/food_clock.png'
        # Make the tank bullets shatterable steel
        self.food_gun = './images/food/food_gun.png'
        # Make the wall of the base camp into a steel plate
        self.food_iron = './images/food/food_gun.png'
        # The tank gets a protective cover for a while
        self.food_protect = './images/food/food_protect.png'
        # Tank upgrade
        self.food_star = './images/food/food_star.png'
        # Tank life +1
        self.food_tank = './images/food/food_tank.png'
        # All food
        self.foods = [self.food_boom, self.food_clock, self.food_gun, self.food_iron,
                      self.food_protect, self.food_star, self.food_tank]
        self.kind = None
        self.food = None
        self.rect = None
        # does it exist
        self.being = False
        # Time of existence
        self.time = 1000

    # Generating food
    def generate(self):
        self.kind = random.randint(0, 6)
        self.food = pygame.image.load(self.foods[self.kind]).convert_alpha()
        self.rect = self.food.get_rect()
        self.rect.left, self.rect.top = random.randint(100, 500), random.randint(100, 500)
        self.being = True

