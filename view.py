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

        self.analysis_mode = self.gen_text('You are in analysis mode')
        self.resistor_ask = self.gen_text('Please enter a resistor value in the terminal')
        self.wire_mode = self.gen_text('Currently in wire mode')

        self.controller = None #will be updated in circuit.py
        self.model = None

    def gen_text(self, text):
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 30)
        out = myfont.render(text, False, (255, 255, 255))
        return out

    def draw(self):
        """ Draws background and components on screen """
        self.screen.fill(pg.Color(255, 255, 255))
        pg.display.set_caption('Test Window')
        self.screen.blit(self.grid_image, (0, 0))
        self.model.components.draw(self.screen)

        #draw wires
        for x1, y1, x2, y2 in self.model.wires:
            pg.draw.line(self.screen, (0, 0, 255), (x1, y1), (x2, y2), 2)

        #blits component while its dragged
        comp_type = self.model.comp_type
        if not (comp_type is None) and self.model.first_click:
            mouse_pos = self.controller.mouse_pos #get mouse position from controller
            comp = TempComp(comp_type,0,0)
            self.screen.blit(comp.image, (mouse_pos[0] - comp.rect.width/2,
                                          mouse_pos[1] - comp.rect.height/2))
        #when mouse click, blits component in place
        elif self.controller.mouse_pressed == True and not self.model.first_click:
            mouse_pos = self.controller.mouse_pos
            print(comp_type)
            self.model.add_comp(comp_type, mouse_pos[0], mouse_pos[1]) #adds resistor
            self.controller.mouse_pressed = False #mouse is not pressed again
            self.model.first_click = True

        elif self.controller.wire_place: #if in wire mode
            self.screen.blit(self.wire_mode, (900, 20)) #show that
        elif self.controller.analysis: #if in analysis mode
            self.screen.blit(self.analysis_mode, (900, 20)) #show that
        # TO DO: If being asked for a resistor value, say so


        pg.display.flip()
