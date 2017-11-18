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
        nbRouter = len(self.placedRouter)
        routerStr = str(nbRouter)+'\n'
        fiberStr = ""
        nbFiber = 0
        out = ""
        for router in self.placedRouter:
            nbFiber += len(router.backRoad.fiberCase)
            routerStr += str(router.row)+' '+str(router.column)+'\n'
            for case in router.backRoad.fiberCase:
                fiberStr +=str(case[0])+' '+str(case[1])+'\n'
        fiberStr = str(nbFiber)+"\n"+fiberStr+"\n"
        out = fiberStr+routerStr
        file = open(self.fileName, "w")
        file.write(out)
        file.close()
