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
    def way(self):
        inc = 1
        """Ligne verticale"""
        if self.beg[0] == self.end[0]:
            """Variable d'incrémentation"""
            if(self.beg[1]>self.end[1]):
                inc = -1
            for i in range(self.beg[1],self.end[1],inc):
                self.fiberCase += [(self.beg[0], i)]
            return None
        """Ligne horizontale"""
        if self.beg[1] == self.end[1]:
            """Variable d'incrémentation"""
            if(self.beg[0]>self.end[0]):
                inc = -1
            for i in range(self.beg[0],self.end[0],inc):
                self.fiberCase += [(i,self.beg[1])]
            return None
        else:
            """Est ce vraiment utile ?"""
            swap=False
            if(self.end[1]<self.beg[1]):
                swap=True
                self.end,self.beg = self.beg,self.end
            """Coefficient directeur de la droite"""
            coef = (self.end[1] - self.beg[1]) / (self.end[0] - self.beg[0])
            """Ajout de la première case"""
            self.fiberCase += [self.beg]
            """Variable d'incrémentation"""
            if(self.beg[0]>self.end[0]):
                inc = -1
            decalage = self.beg[1]+(self.beg[0]*coef*-1)
            for x in range (self.beg[0]+1, self.end[0],inc):
                y = int(coef * x + 0.5+decalage)
                self.fiberCase += [(x,y)]
                if ((len(self.fiberCase) > 1) and (y-self.fiberCase[-2][1] > 1)):
                    step = y - self.fiberCase[-2][1]
                    for i in range(1,step):
                        self.fiberCase = self.fiberCase[:-1] + [(x,y-step+i)] + [self.fiberCase[-1]]
            if(swap==True):
                self.end,self.beg=self.beg,self.end
        return self.fiberCase
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
