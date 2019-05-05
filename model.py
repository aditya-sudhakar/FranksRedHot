'''
Model file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Create and update components
'''
from resistor import Resistor
from voltage import Voltage
from ground import Ground
import pygame as pg

class CircuitModel:
    """ Stores the components """
    def __init__(self):
        self.components = pg.sprite.Group()

        # Adds the sideboard components to click on
        self.r = Resistor(100, 80, 165)
        self.components.add(self.r)
        self.v = Voltage(5, 80, 260, 0, 60, 60) #200 450
        self.components.add(self.v)
        self.g = Ground(80, 360, 0, 140, 140) #200 550
        self.components.add(self.g)

        #stores components and their connections
        self.graph = dict()
        self.connections = dict()

        self.wires = list()

        self.vcc = None
        self.first_click = True
        self.comp_type = None #component that is clicked

        self.view = None
        self.controller = None
        self.analysis = None

    def grid_snap(self, x, y):
        """ Makes components snap to grid positions when placed """
        grid_positions_x = [150, 300, 440, 585, 730, 870, 1010, 1150]
        grid_positions_y = [115, 220, 320, 425, 535, 635, 740, 845]
        new_x = 800
        new_y = 800
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
        new_component = None
        if comp == 'r':
            value = input('Please enter a resistor value (-1 to cancel): ')
            value = int(value)
            if not value == -1:
                new_component = Resistor(value, xpos, ypos)
            else:
                print('canceling')

        elif comp == 'v':
            value = 5
            new_component = Voltage(value, xpos, ypos)
            self.vcc = new_component
        elif comp == 'g':
            value = 0
            new_component = Ground(xpos, ypos)
        else:
            print('Not an existing component') #just for debugging

        if not new_component is None:
            self.components.add(new_component)
            self.graph.update({(xpos,ypos):(comp,value)}) #component info for analysis
            self.connections[new_component] = list()
            print(self.graph)

    def update(self):
        """ Update the software state """

    def print_connections(self):
        """ Prints connections between components """
        for key in self.connections:
            print(key, " is connected to:")
            for conn in self.connections[key]:
                print(conn)

    def r_in_series(self, component):
        """ Gets voltage drop for a component in series"""
        return self.analysis.get_voltage_drop(component)

    def __str__(self):
        """ Prints components to help in debugging """
        output_lines = []
        for component in self.components.sprites():
            output_lines.append(str(component))
        return "\n".join(output_lines) #prints one component per line
