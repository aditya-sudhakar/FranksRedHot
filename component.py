'''
Component Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Makes components
'''
import pygame as pg

class Component(pg.sprite.Sprite):
    """ Handles features of model components """
    def __init__(self):
        super().__init__()

    def load_image(name):
        """ Loads images and makes rectangles for sprites """

        image = pg.image.load(name)
        image = image.convert()

        return image, image.get_rect()
