
from polyhash import *
def main():
    #récupère la carte
    mapIn = Map(getArgument()[1])

    test2 = Path(mapIn.map[20][20], mapIn.map[25][20], 2)
    print(test2.fiberCase)
    for case in test2.fiberCase:
        mapIn.asciiMap[case[1]][case[0]] = 'E'
    #mapIn.analyseMap()
    mapIn.saveASCIIMap()

if __name__ == '__main__':
    main()
