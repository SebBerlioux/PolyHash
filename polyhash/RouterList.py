#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__all__ = ['RouterList', 'RouterNode'] # ajouter dans cette liste tous les symboles 'importables'


class RouterList:
    """
    Classe représentant une liste chainée de potentiels caractérisée par :
    - head -> la tête de la liste chainée
    - listPotential -> la liste des potentiels trouvés
    - dict -> un dictionnaire réferençant les potentiels aux noeuds de la liste
    """

    def __init__(self):
        """Constructeur de la classe"""
        self.head = None
        self.listPotential = []
        self.dict = {}

    def insert(self, cell):
        """Méthode qui ajoute une cellule à la liste chainée"""
        potential = cell.potential
        if self.head == None:
            self.head = RouterNode(potential)
            self.dict[potential] = self.head
            self.head.cellList.append(cell)
            self.listPotential.append(potential)
        if potential not in self.listPotential:
            self.listPotential.append(potential)
            if self.head.potential < potential:
                tmp = RouterNode(potential)
                tmp.next = self.head
                self.head = tmp
                tmp.cellList.append(cell)
                self.dict[potential] = self.head
            else:
                currentCell = self.head
                if currentCell.next == None:
                    currentCell.next = RouterNode(potential)
                    currentCell.cellList.append(cell)
                    self.dict[potential] = currentCell.next
                    return
                else:
                    while currentCell.next != None:
                        if currentCell.next.potential < potential:
                            temp = currentCell.next
                            currentCell.next = RouterNode(potential)
                            currentCell.next.next = temp
                            currentCell.next.cellList.append(cell)
                            self.dict[potential] = currentCell.next
                            return
                        else:
                            currentCell = currentCell.next
                    currentCell.next = RouterNode(potential)
                    currentCell.next.cellList.append(cell)
                    self.dict[potential] = currentCell.next
        else:
            self.dict[potential].cellList.append(cell)


class RouterNode:
    """
    Classe représentant un noeud dans la liste chainée caractérisé par:
    - cellList -> une liste de cellule de même potentiel
    - next -> la cellule suivante dans la liste chainée
    - potential -> un potentiel
    """

    def __init__(self, potential):
        """Constructeur de la classe"""
        self.cellList = []
        self.next = None
        self.potential = potential
