# FranksRedHot

### SPICE Software for Software Design Spring 2019

## Authors
* Aditya Sudhakar  @aditya-sudhakar
* Arwen Sadler     @arwensadler
* Alex Wenstrup    @awenstrup
* Riley Zito      @RileyZito


## Description

Frank's Red Hot is a  circuit analysis software that allows users to analyze basic circuits containing components like resistors, capacitors, and op amps. 

## Website

View the website here: [Frank's Red Hot](https://aditya-sudhakar.github.io/FranksRedHot/)

## Using Frank's Red Hot

* Install the pygame library with `pip3 install pygame` in your terminal
* Run `circuit.py` in the terminal to open the software. 
* Click on a component to select it
* Click on a grid box to place the component (one per box)
* When placing resistors, tab into the terminal and type in the desired field value
* Once your componenets are placed, hit the "w" key to enter "wire mode"
* In wire mode, you can click on componenets to link them in your desired configuration
* Once done, hit "a" to enter "analysis mode"
* Click on a resistor to find out the voltage drop across it
* Close the popup window/type "ctrl+c" in the terminal to halt the program.

#### Version 0.6
* Implemented dictionary object that allows us to run the backend analysis
* Software can analyze resistors in series


#### Version 0.5
* Can only place one component per grid item
* User can now enter resistor value in the terminal
* Drag and Drop interface cleaned up


#### Version 0.4
* Components follow mouse cursor
* Removed hard coded images
* Started implementation of Drag & Drop features
* All components currently Resistors


#### Version 0.3
* Added first hard coded component
* Revamped class / inheritance structure (see UML Diagram)
* Fleshed out attributes for classes

#### Version 0.2
* Added background
* Implemented basic pygame boilerplate
