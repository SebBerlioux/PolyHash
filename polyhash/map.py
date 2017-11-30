#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['Map'] # ajouter dans cette liste tous les symboles 'importables'


from PIL import Image
from .cell import Cell
from .routerlist import RouterList
from .polyhmodel import Bitmap
from .backbone_road import Path
from multiprocessing import Process,Value
import os, errno, math


class Map:
    """
    Classe représentant une carte
    - rowsNumber -> nombre de ligne
    - columnsNumber -> nombre de colonne
    - routerRangeRadius -> rayon des routeurs
    - routerCosts -> cout d'un routeur
    - backboneCosts -> cout des cellules de fibre
    - buget -> budget de la carte
    - map -> matrice des caractere composant la carte
    - isInit -> si la carte est initialise avec un fichier
    """

    def __init__(self,fileName = None,record = False):
        """ Constructeur de la classe """
        self.notComputeRouter = []
        self.routerList = RouterList()
        self.source = ""
        self.isInit = False
        self.map = list()
        self.rowsNumber = 0
        self.columnsNumber = 0
        self.routerRangeRadius = 0
        self.backBoneCosts = 0
        self.routerCosts = 0
        self.budget = 0
        self.firstCell = Cell()
        self.asciiMap = []
        self.placedRouter = []
        if(fileName != None):
            self.initFromFile(fileName)
        self.fichier = "SAVE/image_"
        self.extension = ".png"
        self.record = record
        if(self.record == True):
            directory = "./SAVE"
            if not os.path.exists(directory):
                os.makedirs(directory)

    def initFromFile(self,file):
        """ Initialise la carte avec un fichier """
        self.source = file
        file_reader = open(file,"r")
        self.isInit = True
        lineCounter = 0
        firstLine = None
        SecondLine = None
        ThirdLine = None
        for line in file_reader:
            if(lineCounter == 0):
                firstLine = line.split()
                self.rowsNumber = int(firstLine[0])
                self.columnsNumber = int(firstLine[1])
                self.routerRangeRadius = int(firstLine[2])
            if(lineCounter == 1):
                SecondLine = line.split()
                self.backBoneCosts = int(SecondLine[0])
                self.routerCosts = int(SecondLine[1])
                self.budget = int(SecondLine[2])
            if(lineCounter == 2):
                ThirdLine = line.split()
                self.firstCell = Cell(int(ThirdLine[0]),int(ThirdLine[1]))
            if(lineCounter>2):
                self.asciiMap.append([])
                self.map.append([])
                LINE = line
                columnCounter = 0
                for char in LINE:
                    temp = Cell(len(self.map)-1,columnCounter,Cell.getCellType(char))
                    self.asciiMap[len(self.asciiMap)-1].append(char)
                    self.map[len(self.map)-1].append(temp)
                    if(temp.cellType == "FLOOR"):
                        self.notComputeRouter.append(temp)
                    columnCounter += 1
            lineCounter +=1
        self.isInit = True

    def getDescription(self):
        """ Renvoie la description de la carte """
        if(self.isInit == True):
            STR="Map source : "+self.source+"\n"
            STR += str(self.rowsNumber) + " rows, "+str(self.columnsNumber)+" columns, router range radius is "+str(self.routerRangeRadius)+"\n"
            STR +="backbone costs "+str(self.backBoneCosts)+", router costs "+str(self.routerCosts)+", buget is "+str(self.budget)+"\n"
            STR +="the initial cell connected to backbone is ["+str(self.firstCell.row)+","+str(self.firstCell.column)+"]"
            return STR
        else:
            return "MAP NOT INITIALISED"

    def outOfMap(self,x,y):
        """Indique si des coordonnées d'une cellule sont hors de la carte"""
        if(y<0 or x<0 or x>=self.rowsNumber or y>=self.columnsNumber):
            return True
        else:
            return False

    def buildArea(self,cellRouter):
        """Test par block"""
        """On divise la zone autour du routeur en 4"""
        """On parcours chaque zone (en forme de carré)"""
        """Lorsqu'on tombe sur un mur ou du vide on enregistre cette limite et la stocke dans block"""
        """On parcours la suite du carré jusqu'à block"""
        """On enregistre également les piliers (droite verticale et horizontale partant du router) dans les variables central"""
        BREAK = False
        centralVertTop = cellRouter.row -self.routerRangeRadius - 1
        centralVertBottom = cellRouter.row +self.routerRangeRadius + 1
        centralVert = centralVertTop
        for incColumn in range(-1,2,2):
            centralBlock = cellRouter.column + (self.routerRangeRadius+1)*incColumn
            for incRow in range(-1,2,2):
                if(incRow==1):
                    centralVert = centralVertBottom
                else:
                    centralVert = centralVertTop
                block = centralBlock
                for row in range(cellRouter.row+int((incRow+1)/2),centralVert,incRow):
                    for column in range(cellRouter.column+int((incColumn+1)/2),block,incColumn):
                        if(self.outOfMap(row,column)==False):
                            CASE = self.map[row][column]
                            if(CASE.cellType=="FLOOR"):
                                cellRouter.coveredCell.append(CASE)
                            else:
                                if(row == cellRouter.row):
                                    centralBlock = column
                                if(column==cellRouter.column):
                                    if(incRow == 1):
                                        centralVertBottom = row
                                    else:
                                        centralVertTop = row
                                    BREAK = True
                                block = column
                                break
                        else:
                            block = column
                            break
                    if(BREAK == True):
                        BREAK = False
                        break
        cellRouter.setPotential()

    def analyseMap(self):
        """
        Calul tout les routeurs de la carte
        Chaque routeur doit être mit dans une liste triée par leurs potentiels
        """
        best = 0
        for router in self.notComputeRouter:
            self.buildArea(router)
            if(router.potential>best):
                best = router.potential
            self.routerList.insert(router)
            self.asciiMap[router.row][router.column] = "B"

        self.routerList.listPotential.sort(reverse=True)
        print("BEST POTENTIEL : ",best)

    def save(self):
        """Fonction qui sauvegarde l'itération actuelle de la carte en image"""
        for router in self.placedRouter:
            if router.backRoad != None:
                for case in router.backRoad.fiberCase:
                    self.asciiMap[case[1]][case[0]] = 'E'
                self.asciiMap[router.row][router.column] = 'B'
        self.saveASCIIMap(self.fichier+self.extension)

    def saveASCIIMap(self,fileName="out.png"):
        """Sauvegarde la carte en Bitmap"""
        charDictionnary = dict()
        charDictionnary['-']=(125,125,125)
        charDictionnary['#']=(0,0,0)
        charDictionnary['.']=(255,255,255)
        charDictionnary['B']=(65, 99, 155)
        charDictionnary['E']=(65, 155, 103)
        charDictionnary['R']=(0,0,255)
        #recuperation du tableau de caractere representant la carte
        MAP = self.asciiMap
        #creation de la bitmap
        temp = Bitmap('X',(6,6,6),charDictionnary,MAP)
        #sauvegarde la bitmap en out.png
        temp.save(fileName)

    def isNotFull(self):
        """Indique si la carte est totalement fibré"""
        for cell in self.notComputeRouter:
            if(cell.isCovered==False):
                return True
        return False

    def placeRouter(self):
        """Méthode de placement de routeur intelligente"""
        RouterTrace = ""
        isFirst = True
        temp = 0
        PLACEDCELL = [self.firstCell]
        while(self.budget>self.routerCosts and self.isNotFull()==True):
            print("BEGIN")
            routerNode = self.routerList.head
            while routerNode != None and self.isNotFull()==True and routerNode.potential>0:
                routerToRemove = []
                for router in routerNode.cellList:
                    AddActualRouter = False
                    """Trigger du resetPotentiel si le router n'est pas le premier à être placé"""
                    if isFirst == True:
                        isFirst = False
                    """Recalcul du potentiel"""
                    if isFirst == False:
                        temp = router.resetPotiental()
                    if(temp == router.potential):
                        AddActualRouter = True
                    if AddActualRouter == True:
                        """
                        Récupération du coût du routeur et de son chemin
                        Ajout si il n'y pas de dépassement de
                        Et recalcul du buget
                        """
                        if(router.isCovered == False):
                            router.setBestProch(PLACEDCELL)
                            pathToRouter = Path(router.bestRouter,router,self.backBoneCosts,self)
                            COST = pathToRouter.cost()
                            if(self.budget - self.routerCosts-COST > 0):
                                self.placedRouter.append(router)
                                router.backBoneDist = router.getDistance(self.firstCell)
                                PLACEDCELL.append(router)
                                router.isRouter = True
                                router.coverSelfCell()
                                router.backRoad = pathToRouter
                                self.budget -=(self.routerCosts + COST)
                                routerToRemove.append(router)
                            else:
                                pathToRouter.cancel(self)
                    else:
                        """Si le potentiel du routeur a changé, on le ré-insert dans la liste chainée"""
                        self.routerList.insert(router)
                if(len(routerToRemove)>0):
                    for router in routerToRemove:
                        routerNode.cellList.remove(router)
                """On passe au routeur suivant dans la liste"""
                routerNode = routerNode.next
            print("BUDGET AVANT OPTIMISATION : ",self.budget)
            self.pathFinder()
            print("BUDGET APRES OPTIMISATION : ",self.budget)
        if(self.record==True):
            """On sauvegarde la solution dans le fichier"""
            self.save()
            file = open("SAVE/trace.txt",'w')
            file.write(RouterTrace)
            file.close()

    def pathFinder(self):
        """Méthode qui trouve un arbre couvrant minimum reliant tous les routeurs grâce à l'algorithme de Prim"""
        cost = {}
        pred = {}
        queue = []
        temp = []
        """INIT"""
        cost[self.firstCell] = math.inf
        pred[self.firstCell] = None
        alreadyPlace = [self.firstCell]

        """Tri de la liste de routeur en fonction de la distance au backbone"""
        self.placedRouter.sort(key= lambda Cell:(Cell.backBoneDist))

        for router in self.placedRouter:
            self.budget += router.backRoad.cost()+1
            router.backRoad.cancel(self)
            cost[router] = math.inf
            pred[router] = None
            queue.append(router)

        """Tant que l'on a pas placé tout les routeurs"""
        for router in queue:
            """recherche du routeur placé le plus proche"""
            Last = None
            for i in alreadyPlace:
                    if cost[router] >i.getDistance(router):
                        cost[router] = i.getDistance(router)
                        pred[router] = i
                        Last = router
            if(pred[router]==None):
                print("ERREUR")
            alreadyPlace.append(Last)

        """Parcours du résultat pour la création des chemins"""
        for router in pred.keys():
            if(pred[router]!=None):
                pathToRouter = Path(pred[router],router,self.backBoneCosts,self)
                router.backRoad = pathToRouter
                pred[router].nextRoad.append(pathToRouter)
                self.budget -= pathToRouter.cost()+1
