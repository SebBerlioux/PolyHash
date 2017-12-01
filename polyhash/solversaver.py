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

    def writeInFile(self):
        """Fonction qui écrit la solution dans le fichier"""
        nbRouter = len(self.placedRouter)
        self.routerStr = str(nbRouter)+'\n'
        self.fiberStr = ""
        self.nbFiber = 0
        out = ""
        for road in self.firstCell.nextRoad:
            self.nbFiber += len(road.fiberCase)
            for case in road.fiberCase:
                self.fiberStr +=str(case[1])+' '+str(case[0])+'\n'
        for router in self.placedRouter:
            self.routerStr += str(router.row)+' '+str(router.column)+'\n'
            for road in router.nextRoad:
                self.nbFiber += len(road.fiberCase)
                for case in road.fiberCase:
                    self.fiberStr +=str(case[1])+' '+str(case[0])+'\n'
        self.fiberStr = str(self.nbFiber)+"\n"+self.fiberStr
        out = self.fiberStr+self.routerStr
        file = open(self.fileName, "w")
        file.write(out)
        file.close()
