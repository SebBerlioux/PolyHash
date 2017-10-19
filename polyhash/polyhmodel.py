#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Module de définition des structures de données de Poly#.
"""

__all__ = ['cell','mapRepresentation','bitmap'] # ajouter dans cette liste tous les symboles 'importables'


from PIL import Image
#class representant une cellule de la carte
class cell:
    def __init__(self,r=0,c=0):
        self.row = r
        self.column = c

#class representant une carte
#rowsNumber = nombre de ligne
#columnsNumber = nombre de colonne
#routerRangeRadius = rayon des routeurs
#routerCosts = cout d'un routeur
#backboneCosts = cout des cellules de fibre
#buget = budget de la carte
#map = matrice des caractere composant la carte
#isInit = si la carte est initialise avec un fichier
class mapRepresentation:
    def __init__(self,fileName = None):
        self.source = ""
        self.isInit = False
        self.map = list()
        self.rowsNumber = 0
        self.columnsNumber = 0
        self.routerRangeRadius = 0
        self.backBoneCosts = 0
        self.routerCosts = 0
        self.budget = 0
        self.firstCell = cell()
        if(fileName != None):
            self.initFromFile(fileName)
    #initialise la carte avec un fichier
    def initFromFile(self,file):
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
                self.backBoneCosts = SecondLine[0]
                self.routerCosts = SecondLine[1]
                self.budget = SecondLine[2]
            if(lineCounter == 2):
                ThirdLine = line.split()
                self.firstCell = cell(int(ThirdLine[0]),int(ThirdLine[1]))
            if(lineCounter>2):
                self.map.append(line)
            lineCounter +=1
        self.isInit = True
    #renvoit la description de la carte
    def getDescription(self):
        if(self.isInit == True):
            STR="Map source : "+self.source+"\n"
            STR += str(self.rowsNumber) + " rows, "+str(self.columnsNumber)+" columns, router range radius is "+str(self.routerRangeRadius)+"\n"
            STR +="backbone costs "+str(self.backBoneCosts)+", router costs "+str(self.routerCosts)+", buget is "+str(self.budget)+"\n"
            STR +="the initial cell connected to backbone is ["+str(self.firstCell.row)+","+str(self.firstCell.column)+"]"
            return STR
        else:
            return "MAP NOT INITIALISED"

#Class gerant l'enregistrement d'une matrice de caractere en une Image
#noneArg = caractere representant une cellule non initialise (pour l'addition de bitmap)
#noneColor = couleur associe au noneArg
#rgbDctionnary = dictionnaire associant un caractere a une couleur
#charMap = matrice de caractere
class bitmap:
    def __init__(self,noneArg=None,noneColor=None,rgbDictionnary=None,charMap=None):
        if(charMap!=None):
            self.charMap = charMap
        else:
            self.charMap = list()
        if(rgbDictionnary!= None):
            self.rgbDictionnary = rgbDictionnary
        else:
            self.rgbDictionnary = dict()
        if(noneArg != None):
            self.noneArg = noneArg
        else:
            self.noneArg = '$'
        if(noneColor!=None):
            self.noneColor = noneColor
        else:
            self.noneColor = (255,255,255)
    #enregistre la bitmap sous forme de .png
    def save(self,file=None):
        if(self.charMap==None):
            print("CharMap is not initialised")
            return None
        #si un fichier de destionation n'est pas precise, enregistrement en tant que out.png
        direction = "out.png"
        if(file!=None):
            direction = file
        #creation de l'image
        img= Image.new('RGB',(int(len(self.charMap[0])),int(len(self.charMap))),"black")
        pixel = img.load()
        #parcours de la charMap
        for row in range(len(self.charMap)-1):
            for column in range(len(self.charMap[row])-1):
                #recuperation de la couleur associe au caractere
                color =  self.rgbDictionnary[self.charMap[row][column]]
                #donne la couleur color au pixel (column,row)
                pixel[column,row] = color
        #sauvegarde du fichier
        img.save(direction)
