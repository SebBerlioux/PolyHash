__all__ = ['Map'] # ajouter dans cette liste tous les symboles 'importables'


from PIL import Image
from .cell import Cell
from .polyhmodel import Bitmap
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
        self.asciiMap = []
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
                self.asciiMap.append([])
                self.map.append([])
                LINE = line
                columnCounter = 0
                for char in LINE:
                    self.asciiMap[len(self.asciiMap)-1].append(char)
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
    def outOfMap(self,x,y):
        if(y<0 or x<0 or x>=self.rowsNumber or y>=self.columnsNumber):
            return True
        else:
            return False
    """Détermine si une cellule cell est couverte par un routeur positionné à la cellule cellRouter"""
    def isCoveredBy(self,cell,cellRouter):
        """SUBSQUARING AREA"""
        if(cell.cellType == "WALL" or cell.cellType == "VOID"):
            return False
        stepColumn = 1
        if(cell.column<cellRouter.column):
            stepColumn = -1
        for i in range(cellRouter.column,cell.column+stepColumn,stepColumn):
            stepRow = 1
            if(cell.row<cellRouter.row):
                stepRow = -1
            for j in range(cellRouter.row,cell.row+stepRow,stepRow):
                if(self.outOfMap(j,i)==False):
                    if(self.map[j][i].cellType=="WALL"):
                        return False
        return True
    """Détermine les cellules que couvre un routeur"""
    def buildArea(self,cellRouter):
        for i in range(cellRouter.column - self.routerRangeRadius,cellRouter.column + self.routerRangeRadius+1):
            for j in range(cellRouter.row - self.routerRangeRadius,cellRouter.row + self.routerRangeRadius+1):
                if(self.outOfMap(j,i)==False):
                    if(self.map[j][i].cellType == "FLOOR"):
                        if(self.isCoveredBy(self.map[j][i],cellRouter)==True):
                            cellRouter.coveredCell.append(self.map[j][i])
        cellRouter.setPotential()
    """Calul tout les routeurs de la carte"""
    """Chaque routeur doit être mit dans une liste triée par leurs potentiels"""
    def analyseMap(self):
        routeurList = []
        for j in range(len(self.map)):
            for i in range(len(self.map[j])):
                if(self.map[j][i].cellType == "FLOOR"):
                    routeurList.append(routeurList)
                    self.buildArea(self.map[j][i])

    def potentialToChar(self,potential):
        maxPotential = (self.routerRangeRadius*2)*(self.routerRangeRadius*2)
        temp = (chr(ord('A')+int(potential/maxPotential/24)))
        return temp
    def saveASCIIMap(self):
            charDictionnary = dict()
            charDictionnary['-']=(125,125,125)
            charDictionnary['#']=(0,0,0)
            charDictionnary['.']=(255,255,255)
            charDictionnary['E']=(255,0,0)

            #recuperation du tableau de caractere representant la carte
            MAP = self.asciiMap
            #creation de la bitmap
            temp = Bitmap('X',(6,6,6),charDictionnary,MAP)
            #sauvegarde la bitmap en out.png
            temp.save()
    def saveASCIIMapAsFile(self,fileName):
        file = open(fileName,'w')
        for line in self.asciiMap:
            temp = ""
            for char in line:
                temp += char
            file.write(temp)
        file.close()
