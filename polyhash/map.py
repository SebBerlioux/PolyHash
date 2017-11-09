__all__ = ['Map'] # ajouter dans cette liste tous les symboles 'importables'


from PIL import Image
from .cell import Cell
class Map:
    """
    Classe representant une carte
    - rowsNumber -> nombre de ligne
    - columnsNumber -> nombre de colonne
    - routerRangeRadius -> rayon des routeurs
    - routerCosts -> cout d'un routeur
    - backboneCosts -> cout des cellules de fibre
    - buget -> budget de la carte
    - map -> matrice des caractere composant la carte
    - isInit -> si la carte est initialise avec un fichier
    """
    def __init__(self,fileName = None):
        """ Constructeur de la classe """
        self.source = ""
        self.isInit = False
        self.map = list()
        self.rowsNumber = 0
        self.columnsNumber = 0
        self.routerRangeRadius = 0
        self.backBoneCosts = 0
        self.routerCosts = 0
        self.budget = 0
        self.firstCell = Cell()
        if(fileName != None):
            self.initFromFile(fileName)

    def initFromFile(self,file):
        """ Initialise la carte avec un fichier """
        self.source = file
        file_reader = open(file,"r")
        self.isInit = True
        lineCounter = 0
        firstLine = None
        SecondLine = None
        ThirdLine = None
        for line in file_reader:
            if(lineCounter == 0):
                firstLine = line.split()
                self.rowsNumber = int(firstLine[0])
                self.columnsNumber = int(firstLine[1])
                self.routerRangeRadius = int(firstLine[2])
            if(lineCounter == 1):
                SecondLine = line.split()
                self.backBoneCosts = SecondLine[0]
                self.routerCosts = SecondLine[1]
                self.budget = SecondLine[2]
            if(lineCounter == 2):
                ThirdLine = line.split()
                self.firstCell = Cell(int(ThirdLine[0]),int(ThirdLine[1]))
            if(lineCounter>2):
                self.map.append([])
                LINE = line.split()
                columnCounter = 0
                for char in LINE:
                    self.map[len(self.map)-1].append(Cell(len(self.map)-1,columnCounter,Cell.getCellType(char)))
                    columnCounter += 1
            lineCounter +=1
        self.isInit = True

    def getDescription(self):
        """ Renvoie la description de la carte """
        if(self.isInit == True):
            STR="Map source : "+self.source+"\n"
            STR += str(self.rowsNumber) + " rows, "+str(self.columnsNumber)+" columns, router range radius is "+str(self.routerRangeRadius)+"\n"
            STR +="backbone costs "+str(self.backBoneCosts)+", router costs "+str(self.routerCosts)+", buget is "+str(self.budget)+"\n"
            STR +="the initial cell connected to backbone is ["+str(self.firstCell.row)+","+str(self.firstCell.column)+"]"
            return STR
        else:
            return "MAP NOT INITIALISED"
    """Indique si des coordonnées d'une cellule sont hors de la carte"""
    def outOfMap(x,y):
        if(y<0 or x<0 or x>=self.rowsNumber or y>=self.columnsNumber):
            return False
        else:
            return True
    """Détermine si une cellule cell est couverte par un routeur positionné à la cellule cellRouter"""
    def isCoveredBy(self,cell,cellRouter):
        """SUBSQUARING AREA"""
        if(cell.cellType == "WALL" || cell.cellType == "VOID"):
            return False
        for i in range(cell.x,cellRouter.x+1):
            for j in range(cell.y,cellRouter.y+1):
                if(not outOfMap(j,i)):
                    if(map[j][i].cellType=="WALL"):
                        return False
        return True
    """Détermine les cellules que couvre un routeur"""
    def buildArea(self,cellRouter):
        for i in range(cellRouter.column - self.routerRangeRadius,cellRouter.column + self.routerRangeRadius+1):
            for j in range(cellRouter.row - self.routerRangeRadius,cellRouter.row + self.routerRangeRadius+1):
                if(not outOfMap(j,i)):
                    if(map[j][i].cellType != "WALL" and map[j][i].cellType != "VOID" and map[j][i].cellType != "NONE"):
                        if(self.isCoveredBy(map[j][i],cellRouter)==True):
                            cellRouter.coveredCell.append(map[j][i])
        cellRouter.setPotential()
    """A FAIRE"""
    """Calul tout les routeurs de la carte"""
    """Chaque routeur doit être mit dans une liste triée par leurs potentiels"""
    #def analyseMap():
