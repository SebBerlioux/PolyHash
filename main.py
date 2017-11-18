
from polyhash import *
def main():
    CLOCK = PersonnalClock()
    print("............LECTURE DU FICHIER............")
    mapIn = Map(getArgument()[1],False)
    print("............LECTURE FINIT............")

    print("............DEBUT DE L'ANALYSE............")
    CLOCK.begin()
    mapIn.analyseMap()
    timeELapsed = CLOCK.getElapsedTime()
    CLOCK.end()
    print("DUREE DE L'ANALYSE : ",str(timeELapsed)," SECONDES")


    print("............DEBUT DU PLACEMENT............")
    CLOCK.begin()
    mapIn.placeRouter()
    timeELapsed = CLOCK.getElapsedTime()
    CLOCK.end()
    print("DUREE DU PLACEMENT : ",str(timeELapsed)," SECONDES")

    """
    for router in mapIn.placedRouter:
        for case in router.backRoad.fiberCase:
            mapIn.asciiMap[case[1]][case[0]] = 'E'
        mapIn.asciiMap[router.row][router.column] = 'B'
    mapIn.saveASCIIMap()

    coordA = (150,100)
    coordB = (25,100)
    test2 = Path(mapIn.map[coordA[0]][coordA[1]], mapIn.map[coordB[0]][coordB[1]], 2)
    print(test2.fiberCase)
    for case in test2.fiberCase:
        mapIn.asciiMap[case[1]][case[0]] = 'E'
    mapIn.asciiMap[coordA[0]][coordA[1]] = 'B'
    mapIn.asciiMap[coordB[0]][coordB[1]] = 'B'

    print("SAUVEGARDE DE LA CARTE EN IMAGE")
    mapIn.saveASCIIMap()
    """
if __name__ == '__main__':
    main()
