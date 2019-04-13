#!/usr/bin/python
#-*- coding: utf-8 -*-

from threading import Thread
from GCodeParser import *
from MovimentController import *
from PrinterParameter import *

class PrintController(Thread):
    def __init__(self):
        super().__init__()
        self.printerParameter = PrinterParameter(".\config\parameterFile.json")
        self.gCodeParser = GCodeParser(".\G-Code_Example\Retraction.gcode")
        self.extruderPID = None
        self.bedPID = None
        self.printHeadMovimentController = MovimentController()
        self.extruderController = None
        self.implementedCommands = {
            "G1": self.printHeadMovimentController.commandG1,
        }
        self.printerParameter.updateFile()

    def run(self):
        self.runFile()
        pass

    def runFile(self):

        #commandGenerator = self.gCodeParser.parseLine()
        for command in self.gCodeParser.parseLine():
            self.handleCommand(command)

    def handleCommand(self, command):
        self.implementedCommands.get(command.command, self.invalidCommand)(command)

    def invalidCommand(self, command):
        print("Error command invalid: ")
        command.print()
