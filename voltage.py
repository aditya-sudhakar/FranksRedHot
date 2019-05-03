'''
Voltage Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Makes voltage source objects
'''
import pygame as pg
from component import Component

class Voltage(Component): #inherit from component
    """ Encodes the state of resistors """
    def __init__(self, v=5, x=0, y=0, angle=0, height=80, width=80):
        """ Intializes Resistor with value r
        and position (x,y) at angle """
        super().__init__()
        self.v = v
        self.x = x
        self.y = y
        self.angle = angle
        self.name = 'voltage source'
        self.type = 'v'
        self.fieldValue = 'V*'

        self.image = pg.image.load('images/voltage.png')
        self.image = pg.transform.scale(self.image, (height,width))

        self.rect = self.image.get_rect(center=(x,y))
    def __str__(self):
        return str(self.v) + " volts " + self.name + " at pos " + str(self.x) + ", " + str(self.y)
