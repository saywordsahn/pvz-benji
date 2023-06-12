import pygame
import os
import re


class Animation:

    def __init__(self, name, dir, speed):

        # self.image_count = self.get_file_count(dir)
        self.images = []
        self.name = name
        self.speed = speed
        self.last_flipped = -self.speed
        self.image_count = self.get_file_count(dir)

        for i in range(self.image_count):
            loc = dir + name + '_' + str(i) + '.png'
            img = pygame.image.load(loc)
            self.images.append(img)

        self.current_image_index = 0
        self.image = self.images[self.current_image_index]


    def get_file_count(self, dir_path):
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        return count


    def switch_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.image = self.images[self.current_image_index]

    def update(self, elapsed_time):

        if elapsed_time - self.last_flipped > self.speed:
            self.switch_image()
            self.last_flipped = elapsed_time

    def get_image(self):
        return self.image


