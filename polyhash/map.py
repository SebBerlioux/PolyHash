#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['Map'] # ajouter dans cette liste tous les symboles 'importables'


from PIL import Image
from .cell import Cell
from .RouterList import RouterList
from .polyhmodel import Bitmap
from .backbone_road import Path
from multiprocessing import Process,Value
import os, errno


class Map:
    """
    Classe representant une carte
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
        self.routerTrash = RouterList()
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
        self.nbPass = 0
        if(fileName != None):
            self.initFromFile(fileName)
        self.fichier = "SAVE/image_"
        self.nbSave = 0
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

    def isCoveredBy(self,cell,cellRouter):
        """Détermine si une cellule cell est couverte par un routeur positionné à la cellule cellRouter"""
        """SUBSQUARING AREA"""
        if(cell.cellType == "WALL" or cell.cellType == "VOID"):
            return False
        stepColumn = 1
        if(cell.column<cellRouter.column):
            stepColumn = -1
        for i in range(cellRouter.column,cell.column+stepColumn,stepColumn):
            stepRow = 1
            if(cell.row<cellRouter.row):
                stepRow = -1
            for j in range(cellRouter.row,cell.row+stepRow,stepRow):
                if(self.outOfMap(j,i)==False):
                    if(self.map[j][i].cellType=="WALL"):
                        return False
        return True

    def buildArea(self,cellRouter):
        """Détermine les cellules que couvre un routeur"""
        for i in range(cellRouter.column - self.routerRangeRadius,cellRouter.column + self.routerRangeRadius):
            for j in range(cellRouter.row - self.routerRangeRadius,cellRouter.row + self.routerRangeRadius):
                if(self.outOfMap(j,i)==False):
                    if(self.map[j][i].cellType == "FLOOR"):
                        if(self.isCoveredBy(self.map[j][i],cellRouter)==True):
                            cellRouter.coveredCell.append(self.map[j][i])
        cellRouter.setPotential()

    def analyseMap(self):
        """
        Calul tout les routeurs de la carte
        Chaque routeur doit être mit dans une liste triée par leurs potentiels
        """
        for router in self.notComputeRouter:
            self.buildArea(router)
            self.routerList.insert(router)
            self.asciiMap[router.row][router.column] = "B"
        self.routerList.listPotential.sort(reverse=True)

    def save(self):
        """Fonction qui sauvegarde l'itération actuelle de la carte en image"""
        for router in self.placedRouter:
            for case in router.backRoad.fiberCase:
                self.asciiMap[case[1]][case[0]] = 'E'
            self.asciiMap[router.row][router.column] = 'B'
        self.saveASCIIMap(self.fichier+str(self.nbSave)+self.extension)

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
        self.nbSave +=1

    def saveASCIIMapAsFile(self,fileName):
        """Sauvegarde la carte sous forme de texte"""
        file = open(fileName,'w')
        for line in self.asciiMap:
            temp = ""
            for char in line:
                temp += char
            file.write(temp)
        file.close()

    def isNotFull(self):
        """Indique si la carte est totalement fibré"""
        out = False
        for cell in self.notComputeRouter:
            if(cell.isCovered==False):
                out = True
            #else:
            #    self.notComputeRouter.remove(cell)
        return out

    def placeRouter(self):
        """Méthode de placement de routeur intelligente"""
        RouterTrace = ""
        isFirst = True
        temp = 0
        PLACEDCELL = [self.firstCell]
        while(self.budget > 0 and len(self.routerList.listPotential)>0 and self.isNotFull()==True):
            self.nbPass += 1
            for i in self.routerList.listPotential:
                for router in self.routerList[i]:
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
                            rendement = (1000 * router.nbCoveredCell)-(self.routerCosts + pathToRouter.cost())
                            if(self.budget - self.routerCosts - pathToRouter.cost()>0 and rendement >=0):
                                self.placedRouter.append(router)
                                PLACEDCELL.append(router)
                                router.isRouter = True
                                router.coverSelfCell()
                                router.backRoad = pathToRouter
                                self.budget = self.budget - self.routerCosts - pathToRouter.cost()
                            else:
                                pathToRouter.cancel(self)
                            if(self.record == True):
                                RouterTrace += "("+str(self.nbSave)+") : ("+str(router.row)+","+str(router.column)+") link to ("+str(self.firstCell.row)+","+str(self.firstCell.column)+")\n"
                    else:
                        self.routerTrash.insert(router)
            """Indique que toutes les cases ne sont pas recouvertes afin de re-effectuer le calcul"""
            self.routerList = self.routerTrash
            self.routerList.listPotential.sort(reverse=True)
            self.routerTrash = RouterList()
        if(self.record==True):
            self.save()
            file = open("SAVE/trace.txt",'w')
            file.write(RouterTrace)
            file.close()
