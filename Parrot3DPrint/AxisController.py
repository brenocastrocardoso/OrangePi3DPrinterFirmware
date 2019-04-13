#!/usr/bin/python
#-*- coding: utf-8 -*-

from StepperController import *

class AxisController(StepperController):
    
    def __init__(self, name):
        super().__init__(name)
        self.position = None
        self.virtualPosition = None
        self.maxEndStop = None
        self.minEndStop = None

    def absoluteMove(self, targetPosition, speed=None, acceleration=None):
        self.relativeMove(self, targetPosition - self.position, speed=None, acceleration=None)
        pass
    
    def relativeMove(self, distance, speed=None, acceleration=None):
        if not speed:
            speed = self.maxSpeed
        if not acceleration:
            acceleration = self.maxAcceleration

        move = Move()
        #set direction
        if distance > 0:
            move.direction = Move.Direction.FORWARD
        else:
            move.direction = Move.Direction.BACKWARD

        move.steps = self.convertMMtoSteps(abs(distance))
        move.acceleration = self.convertMMtoSteps(acceleration)
        move.speed = self.convertMMtoSteps(speed)

        self.programMove(move)
        pass

    def homing(self, ):
        pass

    def convertMMtoSteps(self, mm):
        return float(mm)*float(self.stepPerMM)
