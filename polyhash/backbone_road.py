class Path:
    """Entré et sortie doivent être une cell"""
    def __init__(self,beg=None,end=None,backBoneCost = 0):
    #def __init__(self,beg=(0,0),end=(0,0),backBoneCost = 0):
        self.beg = (beg.column,beg.row)
        self.end = (end.column,end.row)
        self.fiberCase = []
        self.backBoneCost = backBoneCost
        self.way()
    """Fonction renvoyant la distance du chemin"""
    """Utilise vite fait pythagore ça economisera des ressources"""

    def getDistance(self):
        return 0
    """Si c'est pour tracer le chemin, il faudrait qu'elle soit appelée depuis le Constructeur du Path"""

    def way(self):
        """Ligne verticale"""
        if self.beg[0] == self.end[0]:
            """Variable d'incrémentation"""
            inc = 1
            if(self.beg[1]>self.end[1]):
                inc = -1
            for i in range(self.beg[1],self.end[1],inc):
                self.fiberCase += [(self.beg[0], i)]
            return None
        """Ligne horizontale"""
        if self.beg[1] == self.end[1]:
            """Variable d'incrémentation"""
            inc = 1
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
            print(self.beg,self.end)
            coef = (self.end[1] - self.beg[1]) / (self.end[0] - self.beg[0])
            print(coef)
            """Ajout de la première case"""
            self.fiberCase += [self.beg]
            """Variable d'incrémentation"""
            inc = 1
            if(self.beg[0]>self.end[0]):
                inc = -1

            for x in range (self.beg[0]+1, self.end[0],inc):
                y = int(coef * x + 0.5)
                self.fiberCase += [(x,y)]
                print([(x,y)])
                if ((len(self.fiberCase) > 1) and (y-self.fiberCase[-2][1] > 1)):
                    step = y - self.fiberCase[-2][1]
                    print(step)
                    for i in range(1,step):
                        self.fiberCase = self.fiberCase[:-1] + [(x,y-step+i)] + [self.fiberCase[-1
                        
            if(swap==True):
                self.end,self.beg=self.beg,self.end
        return self.fiberCase
    def cost():
        return len(self.fiberCase) * self.backboneCosts

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
