import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics/Bullets/PeaNormal/PeaNormal_0.png')
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)
        self.speed = 1
        self.damage = 20

    def update(self, enemy_group):
        self.rect.x += self.speed


        for zombie in enemy_group.sprites():

            if pygame.sprite.collide_rect(zombie, self):
                self.kill()
                zombie.take_damage(self.damage)
                print(zombie.hp)


        #     print(zombie.hp)
        #
        # if pygame.sprite.spritecollide(self, enemy_group, False):
        #     self.kill()

            # explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            # explosion_group.add(explosion)
            # explosion_fx.play()