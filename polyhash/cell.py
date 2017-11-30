#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['Cell']
from math import sqrt


class Cell:
    """
    Classe définissant une cellule caractérisé par:
    - sa coordonnée en x
    - sa coordonnée en y
    - son type
    - routeur
    - fibre
    """
    def __init__(self, row=0, column=0, cellType="NONE"):
        """ Constructeur de la classe """
        self.row = row
        self.column = column
        self.cellType = cellType
        self.isCovered = False
        """Liste des cellules couvertes pour les cellules routeur"""
        self.coveredCell = []
        self.potential = 0
        self.isRouter = False
        """Si la case est déjà fibré"""
        self.isFiber =False
        """Path indiquant d'où vient le routeur"""
        self.backRoad = None
        """Path indiquant les routeurs suivants"""
        self.nextRoad = []
        self.bestDistance = None
        self.bestRouter = None
        self.nbCoveredCell = 0
        self.bufferIndex = 0
        self.subPotential = None
        self.backBoneDist = 0

    def cover(self):
        """Indique qu'une cellule est déjà couverte"""
        self.isCovered = True
    def getNbNexCell(self):
        """Renvoit le nombre de routeur suivant"""
        return len(nextRoad)

    def coverSelfCell(self):
        """Indique les cellules que couvre le routeur"""
        for cellule in self.coveredCell:
            cellule.cover()

    def resetPotiental(self):
        """Diminue le potentiel d'un routeur si une des cellules qu'il couvre est déjà couverte"""
        lastPotential = self.potential
        self.potential = 0
        self.nbCoveredCell = 0
        for cellule in self.coveredCell:
            if(cellule.isCovered!=True):
                self.potential += 1
                self.nbCoveredCell += 1
        return lastPotential

    def setPotential(self):
        """Initialise le potentiel d'un routeur au nombre de cellule qu'il peut couvrir"""
        self.potential = len(self.coveredCell)
        self.nbCoveredCell = self.potential

    def getDistance(self,cellule):
        """Donne la distance entre la cellule est une autre"""
        return sqrt((self.row-cellule.row)**2 + (self.column-cellule.column)**2)

    def setBestProch(self,placedRouter):
        """Indique de quelle cellule, la cellule actuelle est le plus proche"""
        best = None
        prochRouter = None
        for i in range(self.bufferIndex,len(placedRouter)):
            router = placedRouter[i]
            temp = self.getDistance(router)
            if(best == None):
                best = temp
                prochRouter = router
            elif(temp<best):
                best = temp
                prochRouter = router
        if(best != None):
            self.bestDistance = best
        if(prochRouter!=None):
            self.bestRouter = prochRouter
        self.bufferIndex = len(placedRouter)

    def getCellType(char):
        """Renvoit le type de cellule en fonction du caractère"""
        if(char == '#'):
            return "WALL"
        if(char == '.'):
            return "FLOOR"
        if(char == '-'):
            return "VOID"
        else:
            return "NONE"
