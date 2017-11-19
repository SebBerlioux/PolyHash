#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['Cell']



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

    """Indique qu'une cellule est déjà couverte"""
    def cover(self):
        self.isCovered = True
    """Renvoit le nombre de routeur suivant"""
    def getNbNexCell(self):
        return len(nextRoad)
    """Renvoit le routeur suivant à l'index index"""
    def nextCell(self,index):
        return nextRoad[index].endCell
    """Renvoit le routeur précédent"""
    def backCell(self):
        return backRoad.beginCell
    """Indique les cellules que couvre le routeur"""
    def coverSelfCell(self):
        for cellule in self.coveredCell:
            cellule.cover()

    """Diminue le potentiel d'un routeur si une des cellules qu'il couvre est déjà couverte"""
    def resetPotiental(self):
        lastPotential = self.potential
        for cellule in self.coveredCell:
            if(cellule.isCovered==True):
                self.potential -= 1
        return lastPotential

    """Initialise le potentiel d'un routeur au nombre de cellule qu'il peut couvrir"""
    def setPotential(self):
        self.potential = len(self.coveredCell)

    def getWeight(self):
        return sefl.potential
    """Renvoit le type de cellule en fonction du caractère"""
    def getCellType(char):
        if(char == '#'):
            return "WALL"
        if(char == '.'):
            return "FLOOR"
        if(char == '-'):
            return "VOID"
        else:
            return "NONE"
