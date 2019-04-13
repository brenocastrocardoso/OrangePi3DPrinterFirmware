#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import weakref

class PrinterParameter:
    currentPrinter = None
    def __init__(self, configFile):
        self.fileName = configFile
        try:
            self.configFile = open(self.fileName, 'r')
            print("fileread")
            fileStr = self.configFile.read()
            if fileStr:
                self.parameter = json.loads(fileStr)
            else:
                self.parameter = dict()
        except FileNotFoundError:
            self.configFile = open(self.fileName, 'w')
            print("file created")
        self.configFile.close()
        PrinterParameter.currentPrinter = weakref.ref(self)

    def updateFile(self):
        self.configFile = open(self.fileName, 'w')
        self.configFile.write(json.dumps(self.parameter, indent=4, sort_keys=True))
        self.configFile.close()
    
    def __del__(self):
        self.updateFile()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.updateFile()

    @classmethod
    def delCurrent(cls):
        del cls.currentPrinter

    @classmethod
    def registerParameter(cls, parameter):
        #if this parameter doesnt exist
        if not ( parameter in cls.currentPrinter().parameter) :
            #create the parameter as empty, all the parameter needs to be configured by the parameter file
            cls.currentPrinter().parameter.update({ parameter : ""})
            return True
        return False            
    
    @classmethod
    def __getattr__(cls, parameter):
        if parameter in cls.currentPrinter().parameter:
            return cls.currentPrinter().parameter[parameter]
        else:
            raise Exception('The parameter requested is not present in the dictonary')
