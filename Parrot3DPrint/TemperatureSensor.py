#!/usr/bin/python
#-*- coding: utf-8 -*-

from AnalogInput import AnalogInput
from TemperatureMonitor import TemperatureMonitor

class TemperatureSensor(AnalogInput, TemperatureMonitor):
    pass
