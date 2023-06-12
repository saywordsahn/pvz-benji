import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics/Bullets/PeaNormal/PeaNormal_0.png')
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)
        self.speed = 2
        self.damage = 20

    # we take two rects and return true if they collide
    def collided(self, s1, s2):
        if self.rect.colliderect(s2.hitbox):
            return True

        return False

    def update(self, enemy_group):
        self.rect.x += self.speed


        collided = pygame.sprite.spritecollide(self, enemy_group, False, collided = self.collided)

        for zombie in collided:
            zombie.take_damage(self.damage)
            print(zombie.hp)
            self.kill()
            return


        #     print(zombie.hp)
        #
        # if pygame.sprite.spritecollide(self, enemy_group, False):
        #     self.kill()

            # explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            # explosion_group.add(explosion)
            # explosion_fx.play()