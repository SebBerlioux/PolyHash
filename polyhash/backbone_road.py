class Path:
    """Entré et sortie doivent être une cell"""
    def __init__(self,beg=None,end=None,backBoneCost = 0):
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
        self.way()

    """Fonction renvoyant la distance du chemin"""
    """Utilise vite fait pythagore ça economisera des ressources"""
    def getDistance(self):
        return 0
    """Construit le chemin fibré"""
    """
    def way(self):
        inc = 1
        if self.beg[0] == self.end[0]:

            if(self.beg[1]>self.end[1]):
                inc = -1
            for i in range(self.beg[1],self.end[1],inc):
                self.fiberCase += [(self.beg[0], i)]
            return None
        if self.beg[1] == self.end[1]:

            if(self.beg[0]>self.end[0]):
                inc = -1
            for i in range(self.beg[0],self.end[0],inc):
                self.fiberCase += [(i,self.beg[1])]
            return None
        else:

            swap=False
            if( self.end[1]<self.beg[1]):
                swap=True
                self.end,self.beg = self.beg,self.end
            coef = (self.end[1] - self.beg[1]) / (self.end[0] - self.beg[0])
            self.fiberCase += [self.beg]
            if(self.beg[0]>self.end[0]):
                inc = -1
            decalage = self.beg[1]+(self.beg[0]*coef*-1)
            for x in range (self.beg[0]+1, self.end[0]+1,inc):
                y = int(coef * x + decalage)
                self.fiberCase += [(x,y)]
                if ((len(self.fiberCase) > 1) and (abs(y-self.fiberCase[-2][1]) > 1)):
                    step = y - self.fiberCase[-2][1]
                    for i in range(1,step):
                        self.fiberCase = self.fiberCase[:-1] + [(x,y-step+i)] + [self.fiberCase[-1]]
            if(swap==True):
                self.fiberCase.reverse()
                self.end,self.beg=self.beg,self.end
        return self.fiberCase
    """
    """Construction du chemin fibré"""
    """Algorithme inspiré de l'Algorithme de bresenham"""
    def way(self):
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
        """Placement du premier point"""
        self.fiberCase += [self.beg]
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
                self.fiberCase += [(X,Y)]
        else:
            erreur = deltaY/2
            for i in range(1,deltaY+1):
                Y += incY
                erreur += deltaX
                if(erreur >= deltaY):
                    erreur -= deltaY
                    X += incX
                self.fiberCase += [(X,Y)]
    def cost(self):
        return len(self.fiberCase) * self.backBoneCost

'''
ALGORITHMES DE BRESENHAM

procédure tracerSegment(entier x1, entier y1, entier x2, entier y2) est
  déclarer entier x, y, dx, dy ;
  déclarer rationnel e, e(1,0), e(0,1) ;  // valeur d’erreur et incréments
  dy ← y2 - y1 ;
  dx ← x2 - x1 ;
  y ← y1 ;  // rangée initiale
  e ← 0,0 ;  // valeur d’erreur initiale
  e(1,0) ← dy / dx ;
  e(0,1) ← -1.0 ;
  pour x variant de x1 jusqu’à x2 par incrément de 1 faire
    tracerPixel(x, y) ;
    si (e ←  e + e(1,0)) ≥ 0,5 alors  // erreur pour le pixel suivant de même rangée
      y ←  y + 1 ;  // choisir plutôt le pixel suivant dans la rangée supérieure
      e ←  e + e(0,1) ;  // ajuste l’erreur commise dans cette nouvelle rangée
    fin si ;
  fin pour ;
fin procédure ;
'''
