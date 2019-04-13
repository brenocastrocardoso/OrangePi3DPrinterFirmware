#!/usr/bin/python
#-*- coding: utf-8 -*-

from PrinterParameter import *
from enum import Enum

class Move:
        class Direction(Enum):
            FORWARD = 0
            BACKWARD = 1
            

        def __init__(self):
            self.acceleration = None
            self.speed = None
            self.direction = None
            self.steps = None

        def __str__(self):
            ret = str(self.steps) + " " + str(self.direction.value) + " " + str(self.speed) + " " + str(self.acceleration)
            return ret

class StepperController:
    listOfInstances = []
    nextMoveFeedrate = 0
    operationFileName = "OperationFile"
    configurationFileName = "ConfigurationFile"
    def __init__(self, name):
        self.nextMove = None
        self.name = name
        StepperController.listOfInstances.append(self)
        self.registerParameter()


    def programMove(self, move):
        if self.readyToMove():
            self.nextMove = move
            return True
        return False

    def readyToMove(self):
        return (not self.nextMove)

    def stop(self, ):
        pass

    def emergencyStop(self, ):
        pass
    
    def __getattr__(self, parameter):
        return PrinterParameter.__getattr__(self.name + parameter)

    def registerParameter(self):
        PrinterParameter.registerParameter(self.name + "stepPerMM")
        PrinterParameter.registerParameter(self.name + "maxSpeed")
        PrinterParameter.registerParameter(self.name + "Jitter")
        PrinterParameter.registerParameter(self.name + "maxAcceleration")
        PrinterParameter.registerParameter(self.name + "updateFileLock")
        PrinterParameter.registerParameter(self.name + "feedSpeed")

    @classmethod
    def updateConfigurationFile(cls, ):
        pass

    @classmethod
    def setNextMoveFeedrate(cls, value):
        cls.nextMoveFeedrate = value

    @classmethod
    def updateOperationFile(cls, moveFeedRate):
        bufferToWrite = ""
        for instance in cls.listOfInstances:
            bufferToWrite += instance.name + " : " + str(instance.nextMove) + "\n"
        bufferToWrite += "class : " + str(cls.nextMoveFeedrate) + "\n"

        file = open(cls.operationFileName, "w")
        file.write(bufferToWrite)
        file.close()

    @classmethod
    def registerClassParameters(cls):
        PrinterParameter.registerParameter("StepperController" + "OperationFile")
        PrinterParameter.registerParameter("StepperController" + "ConfigurationFile")

    @classmethod
    def isMoveDone(cls):
        return cls.readOperationFile()

    @classmethod
    def readOperationFile(cls):
        file = open(cls.operationFileName + "ReadDebug", "r")
        data = file.read()
        file.close()
        if data == 1:
            return True
        return False
