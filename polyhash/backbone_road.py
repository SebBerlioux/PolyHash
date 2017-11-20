class Path:
    """Entré et sortie doivent être une cell"""
    def __init__(self,beg=None,end=None,backBoneCost = 0,map=None):
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

    """Construction du chemin fibré"""
    """Algorithme inspiré de l'Algorithme de bresenham"""
    def way(self,map):
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
    def cost(self):
        return len(self.fiberCase) * self.backBoneCost
