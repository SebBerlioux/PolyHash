from time import *

class PersonnalClock():
    """
    Classe représentant une horloge
    """

    def __init__(self):
        """Constructeur de la classe"""
        self.timeBuffer = 0
        self.ElapsedTime = 0
        self.isRunning = False

    def begin(self):
        """Méthode qui démarre l'horloge"""
        self.timeBuffer = clock()
        self.isRunning = True

    def getElapsedTime(self):
        """Méthode qui retourne le temps écoulé"""
        if(self.isRunning == True):
            self.ElapsedTime = clock() - self.timeBuffer
        return self.ElapsedTime

    def end(self):
        """Méthode qui stop l'horloge"""
        self.timeBuffer = 0
        self.isRunning = False

    def restart(self):
        """Méthode qui redémarre l'horloge"""
        out = self.getElapsedTime()
        self.begin()
        return out
