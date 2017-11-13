
from polyhash import *

def main():
    #récupère la carte
    mapIn = Map(getArgument()[1])
    mapIn.analyseMap()
#    mapIn.saveASCIIMap()

if __name__ == '__main__':
    main()
