import pygame
from zombie import Zombie
from peashooter import Peashooter
from bullet import Bullet
from sun import Sun
from sunflower import Sunflower

pygame.init()

RES = (1400, 600)
FPS = 60

bg = pygame.image.load('graphics/Items/Background/Background_0.jpg')
hud = pygame.transform.scale_by(pygame.image.load('graphics/Screen/ChooserBackground.png'), .90)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
sun_font = pygame.font.Font('freesansbold.ttf', 18)


# ZOMBIES
zombie = Zombie()

zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

# PLANTS
peashooter = Peashooter()

plant_group = pygame.sprite.Group()
plant_group.add(peashooter)

# Bullet

bullet_group = pygame.sprite.Group()


# Sun
sun = Sun(600, 0)
sun_group = pygame.sprite.Group()
sun_group.add(sun)

sun_amount = 0


# sunFlower
sunflower = Sunflower()
plant_group.add(sunflower)

while True:
    clock.tick(FPS)

    elapsed_time = pygame.time.get_ticks()

    ################################
    # INPUT
    ################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            x = pos[0]
            y = pos[1]
            print('x: {} y: {}'.format(x, y))
            in_x_range = sun.rect.left < x < sun.rect.right
            in_y_range = sun.rect.top < y < sun.rect.bottom

            if in_x_range and in_y_range:
                sun_amount += 50
                sun.kill()



    ################################
    # UPDATE
    ################################

    if peashooter.can_shoot(elapsed_time):
        bullet = Bullet(peashooter.get_mouth_x(), peashooter.get_mouth_y())
        bullet_group.add(bullet)


    sunflower.update(elapsed_time)
    zombie.update(elapsed_time)
    peashooter.update(elapsed_time)
    bullet_group.update(zombie_group)
    sun_group.update(elapsed_time)

    ################################
    # DRAW
    ################################
    screen.blit(bg, (0, 0))
    screen.blit(hud, (0, 0))
    zombie.draw(screen)
    # zombie_group.draw(screen)
    plant_group.draw(screen)
    bullet_group.draw(screen)
    sun_group.draw(screen)
    screen.blit(sun_font.render(str(sun_amount), True, (0, 0, 0)), (22, 56))

    pygame.display.update()
