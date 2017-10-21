#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Cell:
    """
    Classe définissant une cellule caractérisé par:
    - sa coordonnée en x
    - sa coordonnée en y
    - son type
    - routeur
    - fibre
    """

    def __init__(self, x, y, cellType, isRooter = False, isFibre = False):
        """ Constructeur de la classe """
        self.x = x
        self.y = y
        self.cellType = cellType
        self.isRooter = isRooter
        self.isFibre = isFibre
