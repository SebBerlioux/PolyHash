class Path:
    def __init__(entrance=(0,0),exit=(0,0)):
        self.a = entrance
        self.b = exit
        self.fiberCase = []
    def way():
        if self.a[0] == self.b[0]:
            for i in range(self.a[1],self.b[1]):
                self.fiberCase += [(self.a[0], i)]
        else:
            for i in range ():

    def cost():
        return len(self.fiberCase * mapIn.backBoneCosts)

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
