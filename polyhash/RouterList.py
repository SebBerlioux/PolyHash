#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__all__ = ['RouterList'] # ajouter dans cette liste tous les symboles 'importables'


class RouterList:
    """
    Classe représentant une liste de routeurs
    """

    def __init__(self):
        """Constructeur de la classe"""
        self.dict = {}
        self.listPotential = []

    def insert(self, potential, cell):
        """Méthode qui ajoute une cellule au dictionnaire"""
        if potential in self.dict:
            print(potential)
            self.dict[potential] += [cell]
        else:
            self.dict[potential] = [cell]
            self.insertPotential(potential)

    def insertPotential(self, potential):
        """Méthode qui ajoute les potentiels dans une liste triée"""
        if len(self.listPotential) == 0:
            self.listPotential += [potential]
        else:
            for i in range(0, len(self.listPotential)):
                if self.listPotential[i] < potential:
                    self.listPotential.append(0)
                    for j in range(len(self.listPotential)-1, i, -1):
                        self.listPotential[j] = self.listPotential[j-1]
                    self.listPotential[i] = potential
                    return
            self.listPotential.append(potential)

    def __getitem__(self, key):
        """Surcharge de l'accesseur d'attribue"""
        return self.data[key]