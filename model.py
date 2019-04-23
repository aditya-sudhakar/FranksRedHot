'''
Model file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Create and update components
'''
from resistor import Resistor
import pygame as pg

class CircuitModel:
    """ Stores the components """
    def __init__(self):
        self.components = pg.sprite.Group()

        # Adds the sideboard components to click on
        self.r = Resistor(100, 200, 150)
        self.components.add(self.r)

        self.graph = dict()

        # TO DO: Make so that it picks which image to load based on which
        # component was clicked
        self.comp_type = None #component that is clicked

        self.view = None
        self.controller = None

        #self.width = size[0]
        #self.height = size[1]
        #have dictionary of components

    def grid_snap(self, x, y):
        grid_positions_x = [150, 300, 440, 585, 730, 870, 1010, 1150]
        grid_positions_y = [120, 230, 330, 440, 550, 650, 760, 870]
        new_x = 50
        new_y = 50
        for x_pos in grid_positions_x:
            if x_pos <= x:
                new_x = x_pos + 65
        for y_pos in grid_positions_y:
            if y_pos <= y:
                new_y = y_pos + 50
        return (new_x, new_y)

    def add_comp(self, comp, x, y):
        """ Adds a component to the sprite group of a given type and position"""
        xpos, ypos = self.grid_snap(x, y)
        self.graph[comp] = list()
        if comp == 'r':
            self.components.add(Resistor(100, xpos, ypos)) #if type 'r', make a resistor
        elif comp == 'v':
            self.components.add(Voltage(5, xpos, ypos))
        else:
            print('Not an existing component')
    def update(self):
        """ Update the software state """
        #update components, position of components

    def __str__(self):
        """ Prints components to help in debugging """
        output_lines = []
        for component in self.components.sprites():
            output_lines.append(str(component))
        return "\n".join(output_lines) #prints one component per line
