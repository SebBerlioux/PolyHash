from time import *

class PersonnalClock():
    def __init__(self):
        self.timeBuffer = 0
        self.ElapsedTime = 0
        self.isRunning = False
    def begin(self):
        self.timeBuffer = clock()
        self.isRunning = True
    def getElapsedTime(self):
        if(self.isRunning == True):
            self.ElapsedTime = clock() - self.timeBuffer
        return self.ElapsedTime
    def end(self):
        self.timeBuffer = 0
        self.isRunning = False
    def restart(self):
        out = self.getElapsedTime()
        self.begin()
        return out
