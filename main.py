from polyhash import *
import copy
def main():
    print("............DEBUT DU PROGRAMME..........")
    saveLocation = "solution.out"
    if(len(getArgument())>= 3):
        saveLocation = getArgument()[2]
    mapIn = Map(getArgument()[1])
    print("............ANALYSE............")
    mapIn.analyseMap()
    print("............PLACEMENT............")
    mapIn.placeRouter()
    print("SCORE : ",mapIn.score)
    print("............SAUVEGARDE DE LA SOLUTION............")
    solution = SolverSaver(saveLocation,mapIn.placedRouter,mapIn.firstCell)
    solution.writeInFile()
    print("............FIN DU PROGRAMME............")

if __name__ == '__main__':
    main()
