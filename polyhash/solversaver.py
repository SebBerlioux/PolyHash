#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['SolverSaver'] # ajouter dans cette liste tous les symboles 'importables'

class SolverSaver:
    """
    Classe ayant pour but de sauver les résultats dans le fichier solution
    - fileName -> nom du fichier de solution
    - placedRouter -> liste des routeurs placés
    """

    def __init__(self, fileName, placedRouter):
        """Constructeur de la classe"""
        self.fileName = fileName
        self.placedRouter = placedRouter

    def writeInFile(self):
        """Fonction qui écrit la solution dans le fichier"""
        file = open(self.fileName, "w")
        
        file.close()
