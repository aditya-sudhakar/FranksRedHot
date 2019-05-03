'''
Main file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Run the program
'''
import time
import pygame
from model import CircuitModel
from view import PyGameWindowView
from controller import Controller
from analysis import Analysis


def start_software(size):
    """
    Creates all the classes and tells the classes how to communicate with
    each other
    Given screen 'size' as (x,y) tuple and gives it to view
    """
    pygame.init()

    #initializes model, view, controller
    model = CircuitModel()
    view = PyGameWindowView(size)
    controller = Controller()
    analysis = Analysis()

    #gives model, view, controller references to the other ones
    model.view = view
    model.controller = controller
    model.analysis = analysis

    view.model = model
    view.controller = controller

    controller.model = model
    controller.view = view

    analysis.model = model

    #runs software
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            controller.handle_event(event)

        model.update()
        view.draw()
        controller.update()


    pygame.quit()

if __name__ == '__main__':
    size = (1440, 1080)
    start_software(size)
