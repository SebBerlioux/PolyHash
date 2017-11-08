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
                self.map.append(line)
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
