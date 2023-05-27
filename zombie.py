import pygame

class Zombie(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animations = []
        self.current_image_index = 0
        self.count = 0
        self.float_x = 800.0
        self.speed = .15
        self.hp = 100

        for i in range(22):
            loc = 'graphics/Zombies/NormalZombie/Zombie/zombie_' + str(i) + '.png'
            zombie_img = pygame.image.load(loc)
            self.animations.append(zombie_img)

        self.image = self.animations[self.current_image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (800, 100)

    def switch_image(self):
        self.image = self.animations[self.current_image_index]

        # if the index is 21, set it to 0 next time
        if self.current_image_index == len(self.animations) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1

    def update(self):
        self.float_x -= self.speed
        self.rect.x = self.float_x

        if self.count >= 5:

            self.switch_image()

            self.count = 0
        else:
            self.count += 1

    def take_damage(self, amount):
        self.hp -= amount