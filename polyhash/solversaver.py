#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['SolverSaver'] # ajouter dans cette liste tous les symboles 'importables'

class SolverSaver:
    """
    Classe ayant pour but de sauver les résultats dans le fichier solution
    - fileName -> nom du fichier de solution
    - placedRouter -> liste des routeurs placés
    """

    def __init__(self, fileName, placedRouter,firstCell):
        """Constructeur de la classe"""
        self.fileName = fileName
        self.placedRouter = placedRouter
        self.firstCell = firstCell

        self.routerStr = ""
        self.fiberStr = ""
        self.nbFiber = 0

    def writerRec(self,actualNode):
        if(actualNode != self.firstCell):
            self.routerStr += str(actualNode.row)+' '+str(actualNode.column)+'\n'
        for road in actualNode.nextRoad:
            if(actualNode != self.firstCell):
                self.nbFiber += len(actualNode.backRoad.fiberCase)
                for case in actualNode.backRoad.fiberCase:
                    self.fiberStr +=str(case[1])+' '+str(case[0])+'\n'
            self.writerRec(road.endCell)
    def writeInFile(self):
        """Fonction qui écrit la solution dans le fichier"""
        nbRouter = len(self.placedRouter)

        self.routerStr = str(nbRouter)+'\n'
        self.fiberStr = ""
        self.nbFiber = 0
        out = ""
        """self.writerRec(self.firstCell)"""
        for router in self.placedRouter:
            self.nbFiber += len(router.backRoad.fiberCase)
            self.routerStr += str(router.row)+' '+str(router.column)+'\n'
            for case in router.backRoad.fiberCase:
                self.fiberStr +=str(case[1])+' '+str(case[0])+'\n'
        self.fiberStr = str(self.nbFiber)+"\n"+self.fiberStr
        out = self.fiberStr+self.routerStr
        file = open(self.fileName, "w")
        file.write(out)
        file.close()
