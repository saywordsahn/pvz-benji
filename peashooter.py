import pygame

class Peashooter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.current_image_index = 0
        self.count = 0


        for i in range(13):
            loc = 'graphics/Plants/Peashooter/Peashooter_' + str(i) + '.png'
            img = pygame.image.load(loc)
            self.images.append(img)

        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (260, 170)

        self.cooldown = 1000
        self.last_shot = -self.cooldown

    def get_mouth_x(self):
        return self.rect.centerx + 18

    def get_mouth_y(self):
        return self.rect.centery - 15

    def switch_image(self):
        self.image = self.images[self.current_image_index]
        # if the index is 21, set it to 0 next time
        if self.current_image_index == len(self.images) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1

    def can_shoot(self, elapsed_time):

        if elapsed_time - self.last_shot > self.cooldown:
            self.last_shot = elapsed_time
            return True

        return False

    def update(self, elapsed_time):

        # slow our animations down
        if self.count >= 5:

            self.switch_image()

            self.count = 0
        else:
            self.count += 1