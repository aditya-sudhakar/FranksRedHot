'''
Ground Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Makes ground objects
'''
import pygame as pg
from component import Component

class Ground(Component): #inherit from component
    """ Encodes the state of resistors """
    def __init__(self, x=0, y=0, angle=0, height=180, width=180):
        """ Intializes Resistor with value r
        and position (x,y) at angle """
        super().__init__()
        self.g = 0
        self.x = x
        self.y = y
        self.angle = angle
        self.name = 'ground'
        self.type = 'g'
        self.fieldValue = 'G*'

        self.image = pg.image.load('images/ground.png')
        self.image = pg.transform.scale(self.image, (height,width))

        self.rect = self.image.get_rect(center=(x,y))
    def __str__(self):
        return self.name + " at pos " + str(self.x) + ", " + str(self.y)
