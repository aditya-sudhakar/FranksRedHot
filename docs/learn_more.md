# About Frank's Red Hot

### Concept
We wanted to learn more about circuit analysis by building a circuit analysis software, or SPICE
(Simulation Program with Integrated Circuit Emphasis) software. In order to scope our project 
correctly, we decided to focus on the kinds of things we would've found helpful in our introductory
circuits class, ISIM (Introduction to Sensors, Instrumentation, and Measurements). We also wanted 
to have a focus on having a good user interface, since current SPICE software has a clunky, 
90's-looking aesthetic.

### Process
We wanted to start by making a clean UI, so we researched different UI packages in Python. Since
none of them had everything we wanted, we decided to use PyGame, since it had a good documentation
and we all had experience with it.

We started implementing the drag and drop functionality, allowing users to select a component and
place it anywhere on the screen. During this time, we also designed our components so that we could
go back and edit them more easily. We spent a lot of time trying to abstract the code and implement good
inheritance structure as much as possible, to minimize copy and pasted code. 

We then cleaned up the UI side, so that there would be one component per box, and started implementing
wires.

Finally, we used a dictionary object to link all the components and wires together, so that the software could
"understand" where the components were in relation to each other.

#### [Return to home page](index.md)
