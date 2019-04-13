#!/usr/bin/python
#-*- coding: utf-8 -*-

from bedMap import bedMap
from AxisController import *
from GCodeParser import GCodeCommand
from StepperController import *

class MovimentController(bedMap):
    def __init__(self):
        self.axisList = []
        self.XAxis = AxisController("X")
        self.axisList.append(self.XAxis)
        self.YAxis = AxisController("Y")
        self.axisList.append(self.YAxis)
        self.ZAxis = AxisController("Z")
        self.axisList.append(self.ZAxis)

    def bedScan(self, ):
        pass

    def compensateZ(self, ):
        pass

    def commandG1(self, command):
        for parameters in command.parameters:
            for axis in self.axisList:
                if axis.name == parameters[0] : #the first leter should name the axis
                    numero = parameters[1:]
                    numero = float(numero)
                    axis.relativeMove(numero)
                    StepperController.updateOperationFile(100)
                    break
        pass
        
