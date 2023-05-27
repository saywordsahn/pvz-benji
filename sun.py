import pygame

class Sun(pygame.sprite.Sprite):

    def __init__(self, centerx, bottomy):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        for i in range(22):
            loc = 'graphics/Plants/Sun/Sun_' + str(i) + '.png'
            img = pygame.image.load(loc)
            self.images.append(img)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (centerx, bottomy)
        self.current_image_index = 0
        self.animation_cooldown = 100
        self.last_frame_switch = -self.animation_cooldown
        self.speed = 1


    def switch_image(self):
        self.image = self.images[self.current_image_index]

        # if the index is 21, set it to 0 next time
        if self.current_image_index == len(self.images) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1

    def update(self, elapsed_time):

        if elapsed_time - self.last_frame_switch > self.animation_cooldown:
            self.switch_image()
            self.last_frame_switch = elapsed_time

        self.rect.y += self.speed


