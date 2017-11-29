class Path:
    """
    Classe représentant un chemin fibré représenté par :
    - beg -> la cellule de début
    - end -> la cellule de fin
    - backBoneCost -> le coût du chemin
    - map -> la carte
    """

    def __init__(self,beg=None,end=None,backBoneCost = 0,map=None):
        """Constructeur de la classe"""
        """Déclaration des cellules"""
        self.beginCell = beg
        self.endCell = end
        """Coordonnée des cellules de début et fin"""
        self.beg = (beg.column,beg.row)
        self.end = (end.column,end.row)
        """Liste des cases fibrés"""
        self.fiberCase = []
        """coût de une cellule de fibre"""
        self.backBoneCost = backBoneCost
        self.way(map)

    def way(self,map):
        """
        Construction du chemin fibré
        Algorithme inspiré de l'Algorithme de bresenham
        """
        X = self.beg[0]
        Y = self.beg[1]
        deltaX = self.end[0]-self.beg[0]
        deltaY = self.end[1]-self.beg[1]
        incX = 1
        incY = 1
        """Choix de l'incrément en fonction du sens de la droite"""
        if(deltaX<0):
            incX = -1
        if(deltaY<0):
            incY = -1
        deltaX = abs(deltaX)
        deltaY = abs(deltaY)
        """Placement du premier point, pas nécessaire"""
        #self.fiberCase += [self.beg]
        """Si la pente en X est plus grande que la pente en Y"""
        if(deltaX>deltaY):
            erreur = deltaX/2
            for i in range(1,deltaX+1):
                """On incrémente selon les X"""
                X+= incX
                erreur += deltaY
                """Si la différence est supérieur à l'avancement des X"""
                if(erreur>=deltaX):
                    """On retire le delta"""
                    erreur -= deltaX
                    """Et on incrémente en Y"""
                    Y += incY
                if(map.map[Y][X].isFiber==False):
                    self.fiberCase += [(X,Y)]
                    map.map[Y][X].isFiber = True
                else:
                    self.cancel(map)
                    self.fiberCase = []
                    self.beginCell = map.map[Y][X]
        else:
            erreur = deltaY/2
            for i in range(1,deltaY+1):
                Y += incY
                erreur += deltaX
                if(erreur >= deltaY):
                    erreur -= deltaY
                    X += incX
                if(map.map[Y][X].isFiber==False):
                    self.fiberCase += [(X,Y)]
                    map.map[Y][X].isFiber = True
                else:
                    pass
                    self.cancel(map)
                    self.fiberCase = []
                    self.beginCell = map.map[Y][X]

    def cancel(self,map):
        """Méthode qui retire les cellules fibrées"""
        for case in self.fiberCase:
            map.map[case[1]][case[0]].isFiber = False

    def cost(self):
        """Méthode qui calcul le coût d'un chemin"""
        return len(self.fiberCase) * self.backBoneCost
