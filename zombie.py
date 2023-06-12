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
        self.inflate_x = -150
        self.inflate_y = -75
        self.offset_l = 100
        self.offset_t = 25

        self.hitbox = self.rect.inflate(self.inflate_x, self.inflate_y)
        self.hitbox.y += self.offset_t
        # self.rect.inflate_ip(-100,0)


    def switch_image(self):
        self.image = self.animations[self.current_image_index]

        # if the index is 21, set it to 0 next time
        if self.current_image_index == len(self.animations) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1

    def update(self):

        if self.hp > 0:
            self.float_x -= self.speed
            self.rect.x = self.float_x
            self.hitbox.x = self.float_x + self.offset_l

            if self.count >= 5:

                self.switch_image()

                self.count = 0
            else:
                self.count += 1

    def take_damage(self, amount):
        self.hp -= amount

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (0, 255, 0), self.rect, 1)
        # pygame.draw.rect(screen, (0, 0, 255), self.hitbox, 1)
