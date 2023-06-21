import pygame

class Sunflower(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.current_image_index = 0
        self.count = 0


        for i in range(18):
            loc = 'graphics/Plants/SunFlower/SunFlower_' + str(i) + '.png'
            img = pygame.image.load(loc)
            self.images.append(img)

        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (260, 290)

        self.cooldown = 10000
        self.last_spawned = -self.cooldown


    def switch_image(self):
        self.image = self.images[self.current_image_index]
        # if the index is 21, set it to 0 next time
        if self.current_image_index == len(self.images) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1

    def can_spawn(self, elapsed_time):

        if elapsed_time - self.last_spawned > self.cooldown:
            self.last_spawned = elapsed_time
            return True

        return False

    def update(self, elapsed_time):

        # slow our animations down
        if self.count >= 5:

            self.switch_image()

            self.count = 0
        else:
            self.count += 1