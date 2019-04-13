#!/usr/bin/python
#-*- coding: utf-8 -*-

from PID_INPUT import PID_INPUT

class AnalogInput(PID_INPUT):
    def __init__(self):
        self.value = None
        self.frequency = None
        self.convertTable = None

    def getValue(self, ):
        pass

    def getConvertedValue(self, ):
        pass

