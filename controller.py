'''
Controller Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Takes controller input
'''

import pygame
from pygame.locals import *

class Controller:
    """ Handles mouse input from the user """
    def __init__(self):
        self.mouse_pos = (0, 0)

        self.model = None #will be updated in circuit.py
        self.view = None

        self.wire_place = False
        self.analysis = False

        self.component1 = None
        self.position1 = 0

        self.mouse_pressed = False
    def handle_event(self, event):
        """ Senses if mouse is pressed and updates mouse pressed """
        if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_pressed = True
            x,y = event.pos

            if self.analysis: #analysis mode
                for component in self.model.components:
                    if component.rect.collidepoint(x, y):
                        print("The voltage drop over the selected resistor is")
                        print(self.model.r_in_series(component))

            elif self.wire_place: #wire placing mode
                for component in self.model.components:
                    if component.rect.collidepoint(x, y):
                        print(component.type)
                        if self.component1 is None:
                            self.component1 = component
                            self.position1 = (x, y)
                        else:
                            self.add_wire(self.component1, component, self.position1, (x, y))

            else: #placing and dragging of components
                if self.model.comp_type == None: #when simulation starts
                    self.model.first_click = True #to track placing vs. dragging
                else:
                    self.model.first_click = False

                for component in self.model.components:
                    if component.rect.collidepoint(x,y): #get type of component clicked
                        if not (self.model.comp_type == component.type): #switching components
                            self.model.first_click = True
                        self.model.comp_type = component.type #set type in model to that type

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.wire_place ^= True #w -> write placing mode
            elif event.key == pygame.K_a:
                self.analysis ^= True #a -> write placing mode

            if self.wire_place: #wire placing and analysis cannot overlap
                self.analysis = False
            if self.analysis:
                self.wire_place = False

    def add_wire(self, c1, c2, p1, p2):
        """ Draws a wire between two components"""
        self.model.connections[c1].append(c2)
        self.model.connections[c2].append(c1)
        self.model.wires.append((p1[0], p1[1], p2[0], p2[1]))
        self.component1 = None
        self.posiiton1 = None
        self.model.print_connections()

    def update(self):
        """ Updates position of the mouse """
        self.mouse_pos = pygame.mouse.get_pos()
        if self.wire_place:
            self.model.comp_type = None
