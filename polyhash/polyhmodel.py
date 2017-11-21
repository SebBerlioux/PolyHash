#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Module de définition des structures de données de Poly#.
"""
from PIL import Image
__all__= ["Bitmap"]


class Bitmap:
    """
    Classe gerant l'enregistrement d'une matrice de caractere en une Image
    - noneArg -> caractere representant une cellule non initialise (pour l'addition de bitmap)
    - noneColor -> couleur associe au noneArg
    - rgbDctionnary -> dictionnaire associant un caractere a une couleur
    - charMap -> matrice de caractere
    """

    def __init__(self,noneArg=None,noneColor=None,rgbDictionnary=None,charMap=None):
        """ Constructeur de la classe """
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

    def save(self,file=None):
        """ Enregistre la bitmap sous forme de .png """
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
