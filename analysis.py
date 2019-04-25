'''
Analysis Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Responsible for the backend portion of Frank's Red Hot SPICE Software - contains functions necessary to
''''''
Model file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Create and update components
'''

from resistor import Resistor
from voltage import Voltage
from ground import Ground
import pygame as pg

class Analysis:
    """ Gets voltage and current for a given circuit """
    def __init__(self):
        #format of components is {(xpos,ypos):(comp,value)}
        self.grid_positions_x = [150, 300, 440, 585, 730, 870, 1010, 1150]
        self.grid_positions_y = [120, 230, 330, 440, 550, 650, 760, 870]

        self.model = None
        self.view = None
        self.controller = None

    def get_voltage(self):
        components = self.model.graph
        for comp in components:
            if comp[0] == self.grid_positions_x[0]: #x coord
                first = comp

    def get_current(self):
        pass
    def update(self):
        """ Update the software state """
        pass

    def __str__(self):
        """ Prints components to help in debugging """
        output_lines = []
        for component in self.components.sprites():
            output_lines.append(str(component))
        return "\n".join(output_lines) #prints one component per line
