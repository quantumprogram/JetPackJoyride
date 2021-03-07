# JetpackJoyride-clone
This is an attempt to make a clone of Jetpack Joyride clone game in python. The end result works quite great. The entire code is designed in Object Oriented Design with minimal python library.   

## Controls:

W: move up
A: move left
D: move right
F: shoot
V: speedboost ( can be used only once in the game )

Gravity is implemented ( constant accelaration )
Obstacles can be shot down
Defeat the dragon in final if you can.

To run the game simply run the main.py file after cloning the repository. Use python3 compiler.

## Implementation:

Entity Class: Classes belonging to all objects appearing on the board inherit entity class. This class attaches itself to the entity list of the game, has the concept of co-ordiantes. Basically it can be imagined as a pin or anchor tethering objects to the canvas. Note: Entity itself is not used. Only it's children are used.

Person Class: This is used to make square shape objects of a given size. It inherits from entity. This class has been used over and over to create classes such as the Mandalorian, Coins, Shield, Bullets, Dragon etc. This is the prime example of power of OOPS

Obstacles: Directly inherit from entity class as they vary in shape and size. They have thier own collisi9on related functions.

Concept: At frequent intervals entitys are randomly generated. There is a list of entities in the game object. At every frame, each object is "ticked" and updated. If it needs to be shown on the screen, it is rendered. After all objects are updated we check collisions in the list and based on collisions update the game state. By this time due to the ticks, all objects have been rendered in the canvas. We draw the canvas using a 2D array. Canvas is refreshed at the start of every tick. 

Note: Not all variables are made private and in some casses getter and setter functions are not used. Example : Rendering on the canvas. This is due to simplicity and performance overhead.
