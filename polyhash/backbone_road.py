class Path:
    """Entré et sortie doivent être une cell"""
    #def __init__(self,beg=None,end=None,backBoneCost = 0):
    def __init__(self,beg=(0,0),end=(0,0),backBoneCost = 0):

        #self.beg = (beg.column, self.beg.row)
        #self.end = (self.end.column,self.end.row)

        self.beg = beg
        self.end = end
        self.fiberCase = []
        self.backBoneCost = backBoneCost
        print("initialisation ok   " + str(self.beg) + str(self.end) + "   " + str(self.backBoneCost))

    """Fonction renvoyant la distance du chemin"""
    """Utilise vite fait pythagore ça economisera des ressources"""

    def getDistance(self):
        return 0
    """Si c'est pour tracer le chemin, il faudrait qu'elle soit appelée depuis le Constructeur du Path"""

    def way(self):
        if self.beg[0] == self.end[0]:
            for i in range(self.beg[1],self.end[1]):
                self.fiberCase += [(self.beg[0], i)]
        else:
            coef = (self.end[1] - self.beg[1]) / (self.end[0] - self.beg[0])
            for x in range (self.beg[0], self.end[0]):
                y = int(coef * x + 0.5 - self.beg[0])
                self.fiberCase += [(x,y)]
                if ((len(self.fiberCase) > 1) and (y-self.fiberCase[-2][1] > 1)):
                    step = y - self.fiberCase[-2][1]
                    print(step)
                    for i in range(1,step):
                        self.fiberCase = self.fiberCase[:-1] + [(x,y-step+i)] + [self.fiberCase[-1]]
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
