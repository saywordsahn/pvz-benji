import pygame
import os
import re


class Animation:

    def __init__(self, name, dir):

        # self.image_count = self.get_file_count(dir)
        self.images = []
        self.name = name

        for i in range(self.get_file_count(dir)):
            loc = dir + name + '_' + str(i) + '.png'
            img = pygame.image.load(loc)
            self.images.append(img)


    def get_file_count(self, dir_path):
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        return count


animations = Animation('Zombie', 'graphics/Zombies/NormalZombie/Zombie/')
