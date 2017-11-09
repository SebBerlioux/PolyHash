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
    """Indique qu'une cellule est déjà couverte"""
    def Cover():
        self.isCovered = True
    """Indique les cellules que couvre le routeur"""
    def coverSelfCell():
        for cellule in self.coveredCell
            cellule.Cover()
    """Diminue le potentiel d'un routeur si une des cellules qu'il couvre est déjà couverte"""
    def resetPotiental():
        for cellule in self.coveredCell
            if(cellule.isCovered==True):
                self.potential -= 1
    """Initialise le potentiel d'un routeur au nombre de cellule qu'il peut couvrir"""
    def setPotential():
        self.potential = len(self.coveredCell)
    def getCellType(char):
        if(char == '#'):
            return "WALL"
        if(char == '.'):
            return "FLOOR"
        if(char == '-'):
            return "VOID"
        else:
            return "NONE"
