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

    def insert(self, cell):
        """Méthode qui ajoute une cellule au dictionnaire"""
        potential = cell.potential
        if potential not in self.listPotential:
            self.listPotential.append(potential)
        if potential in self.dict:
            self.dict[potential] += [cell]
        else:
            #self.insertPotential(potential)
            self.dict[potential] = [cell]
        self.dict[potential]

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
        return self.dict[key]

    def delete(self, key):
        """Fonction de suppression d'une key dans le dico"""
        del self.dict[key]
