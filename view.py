'''
View for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Main Window for Pick-and-Place
'''

import pygame as pg
from resistor import Resistor
from temp_comp import TempComp

class PyGameWindowView:
    """ Creates the window/grid for placing components """
    def __init__(self, size):
        self.screen = pg.display.set_mode(size)
        self.grid_image = pg.image.load("./images/grid.png")
        self.grid_image = pg.transform.scale(self.grid_image, (1440, 1080))

        self.controller = None #will be updated in circuit.py
        self.model = None
    def draw(self):
        """ Draws background and components on screen """
        self.screen.fill(pg.Color(255, 255, 255))
        pg.display.set_caption('Test Window')
        self.screen.blit(self.grid_image, (0, 0))
        self.model.components.draw(self.screen)

        #draw wires
        for x1, y1, x2, y2 in self.model.wires:
            pg.draw.line(self.screen, (0, 0, 255), (x1, y1), (x2, y2), 2)

        #HARD-CODED, FIX LATER: mouse_pressed should depend on whether the mouse
        #has been clicked over a component

        #blits component while its dragged
        comp_type = self.model.comp_type
        if self.controller.mouse_pressed == False and not (comp_type is None):
            mouse_pos = self.controller.mouse_pos #get mouse position from controller
            comp = TempComp(comp_type,0,0)
            self.screen.blit(comp.image, (mouse_pos[0] - comp.rect.width/2,
                                          mouse_pos[1] - comp.rect.height/2))
        #when mouse click, blits component in place
        elif self.controller.mouse_pressed == True and not (comp_type == None):
            mouse_pos = self.controller.mouse_pos
            #HARD-CODED, FIX LATER: resistor is drawn when clicked, should be
            #any component/get it from model
            print(comp_type)
            self.model.add_comp(comp_type, mouse_pos[0], mouse_pos[1]) #adds resistor
            self.controller.mouse_pressed = False #mouse is not pressed again

            print("\nCurrent components:") #for debugging
            print(self.model)

        pg.display.flip()
