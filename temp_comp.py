'''
TempComp Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Makes temporary component objects to drag
'''
import pygame as pg
from component import Component

class TempComp(Component): #inherit from component
    """ Encodes the state of resistors """
    def __init__(self, type, x=0, y=0, angle=0, height=100, width=20):
        """ Intializes TempComp with a type
        and position (x,y) at angle """
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.angle = angle

        if self.type == 'r':
            self.image = pg.image.load('images/resistor.png')
        elif self.type == 'v':
            self.image = pg.image.load('images/voltage.png')
        elif self.type == 'g':
            self.image = pg.image.load('images/ground.png')
        self.image = pg.transform.scale(self.image, (height,width))

        self.rect = self.image.get_rect(center=(x,y))
    def __str__(self):
        return "temporary component of " + self.type + " type"
