
from polyhash import *
def main():
    #récupère la carte
    mapIn = Map(getArgument()[1])
    a = (15,7)
    b = (30,30)
    test = Path(a, b, 2)
    test.way()
    print(test.fiberCase)
    for case in test.fiberCase:
        mapIn.asciiMap[case[1]][case[0]] = 'E'
    #mapIn.analyseMap()
    mapIn.saveASCIIMap()

if __name__ == '__main__':
    main()
