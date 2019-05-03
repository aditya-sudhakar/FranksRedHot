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
        #format of components is {(xpos,ypos):(type,value)}
        self.grid_positions_x = [150, 300, 440, 585, 730, 870, 1010, 1150]
        self.grid_positions_y = [120, 230, 330, 440, 550, 650, 760, 870]

        self.model = None
        self.view = None
        self.controller = None

    def get_voltage(self):
        components = self.model.graph
        place = 0
        head = -1
        visited = {}
        for comp in components:
            visited.add({comp:components[comp]})
            type,value = components[comp]
            if type == 'v' and head == -1: #make sure there aren't multiple sources
                head = place #store place of voltage source
            place += 1

    def get_current(self):
        pass

    def update(self):
        """ Update the software state """
        pass

    def is_r_in_series(self, component):
        if component is None:
            return False
        if len(self.model.connections[component]) == 2 and component.type == 'r':
            return True
        return False

    def series_to_req(self, head):
        req = 0
        curr = head
        prev = None
        while curr.is_r_in_series():
            req += curr.r
            prev = curr
            connected = self.model.connections[curr]
            a = connected.get(0)
            b = connected.get(1)
            if is_r_in_series(a) and a is not prev:
                curr = a
            elif is_r_in_series(b) and b is not prev:
                curr = b
            else:
                curr = None

        print('The equivalent resistance for this section is ', req)
        return req

    def get_voltage_drop(self, component):
        for c in self.model.connections:
            if c.type == 'r':
                if not is_r_in_series(c):
                    return False

        vcc = self.model.vcc
        first = self.model.connections[vcc].get(0)
        req = series_to_req(first)

        return component.r / req * vcc.v


    def __str__(self):
        """ Prints components to help in debugging """
        output_lines = []
        for component in self.components.sprites():
            output_lines.append(str(component))
        return "\n".join(output_lines) #prints one component per line
