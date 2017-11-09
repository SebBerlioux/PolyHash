
from polyhash import *

def main():
    #récupère la carte
    mapIn = Map(getArgument()[1])
    #creation du dictionnaire associant un caractere a une couleur
    charDictionnary = dict()
    charDictionnary['-']=(125,125,125)
    charDictionnary['#']=(0,0,0)
    charDictionnary['.']=(255,255,255)
    #recuperation du tableau de caractere representant la carte
    MAP = mapIn.map
    #creation de la bitmap
    temp = Bitmap('X',(6,6,6),charDictionnary,MAP)
    #sauvegarde la bitmap en out.png
    temp.save()
    #mapIn.saveAsImage()
    

if __name__ == '__main__':
    main()
