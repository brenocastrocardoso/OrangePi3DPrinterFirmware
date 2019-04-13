#!/usr/bin/python
#-*- coding: utf-8 -*-


class GCodeCommand:
        def __init__(self, command):
            self.command = command
            self.parameters = []

        def addParameter(self, parameter):
            self.parameters.append(parameter)

        def print(self):
            print("Comand: ", self.command)
            for member in self.parameters:
                print("Parametro: ", member)

class GCodeParser:         

    def __init__(self, filename):
        self.gcodeFile = open(filename)
        self.currentCommand = None
        self.currentLine = 0

    def __del__(self):
        self.gcodeFile.close()

    def parseCommand(self, line):
        del self.currentCommand

        line = line.split(" ")

        self.currentCommand = GCodeCommand(line[0])
        
        #the first split is the command
        for parameter in line[1:]:
            if line:
                self.currentCommand.addParameter(parameter)

        return self.currentCommand

    def parseLine(self):
        line = None
        ret = None
        
        for line in self.getValidLine():
            ret = self.parseCommand(line)
            yield ret
        
    def getValidLine(self):
        caracteresToRemove = [";", "\n"]
        for gCodeFileLine in self.gcodeFile:
            self.currentLine += 1
            
            for caracter in caracteresToRemove:
                index = gCodeFileLine.find(caracter)
                gCodeFileLine = gCodeFileLine[0:index if (index != -1) else len(gCodeFileLine)]
                
            # remove white space int the beginning
            gCodeFileLine = gCodeFileLine.strip(" ")
            
            if (gCodeFileLine):  # this is a valid gCodeFileLine
                yield gCodeFileLine

