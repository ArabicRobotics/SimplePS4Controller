#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# simple Playstation 4 Controller
#
# Copyright © TareqGamal ArabicRobotics 
# ArabicRobotics.com
# https://github.com/ArabicRobotics
# https://www.youtube.com/channel/UCj3IoLXlUfjYTHpwgXm4xsg

# you can Add your code In File (Demo.py) No Change in this file

import os
import pygame
import threading
import time
from clsControllerData import ControllerData
class SimplePS4Controller(threading.Thread):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None



    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(PS4Controller, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self.cTime = time.ctime
        self.paused = False
        """Initialize the joystick components"""
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()        

    def stop(self):
        self._stop.set()
        self.join()

    def stopped(self):
        return self._stop.isSet()



    def pause(self):
        self.paused = True
        #this is should make the calling thread wait if pause() is
        #called while the thread is 'doing the thing', until it is
        #finished 'doing the thing'

    #should just resume the thread
    def resume(self):
        self.paused = False


    def run(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
              
            if self.stopped():
                return
            if not self.paused:
                for event in pygame.event.get():
                    #print "Changed!"
                    ControllerData.changed=True
                    ControllerData.newData=True
                    if event.type == pygame.JOYAXISMOTION:
                        self.axis_data[event.axis] = round(event.value,2)

                    elif event.type == pygame.JOYBUTTONDOWN:
                        self.button_data[event.button] = True
                    elif event.type == pygame.JOYBUTTONUP:
                        self.button_data[event.button] = False
                        
                    elif event.type == pygame.JOYHATMOTION:
                        #print (event.value)
                        self.hat_data[event.hat] = event.value

                    # Insert your code on what you would like to happen for each event here!
                    # In the current setup, I have the state simply printing out to the screen.
                    
                    

                    #print ("buttuns Data")
                    #print self.button_data
                    #print ("Axis Data")
                    #print self.axis_data
                    ControllerData.button_data=self.button_data
                    ControllerData.axis_data = self.axis_data
                    ControllerData.simplfyData()
                else:
                    ControllerData.changed =False




                
            self.cTime= time.ctime()
            #print(self.cTime)