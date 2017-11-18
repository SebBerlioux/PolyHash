
from polyhash import *
def main():
    """ADRESSE DU JUGE"""
    """http://pitools.polytech.univ-nantes.fr/polyhash/app/index"""
    CLOCK = PersonnalClock()
    print("............LECTURE DU FICHIER............")
    mapIn = Map(getArgument()[1],True)
    print("............LECTURE FINIT............")
    print("DESCRIPTION : ")
    print(mapIn.getDescription())
    print("............DEBUT DE L'ANALYSE............")
    CLOCK.begin()
    mapIn.analyseMap()
    timeELapsed = CLOCK.getElapsedTime()
    CLOCK.end()
    print("DUREE DE L'ANALYSE : ",str(timeELapsed)," SECONDES\n")
    print("............DEBUT DU PLACEMENT............")
    CLOCK.begin()
    mapIn.placeRouter()
    timeELapsed = CLOCK.getElapsedTime()
    CLOCK.end()
    print("DUREE DU PLACEMENT : ",str(timeELapsed)," SECONDES")
    print("............FIN DU PLACEMENT............\n")
    print("............ACQUISITION DES DONNEES............")
    print("Nombre de router placés : ",len(mapIn.placedRouter))
    print("Budget restant : ",mapIn.budget)
    print("Nombre de recalcul : ",mapIn.nbPass)
    print("............SAUVEGARDE DE LA SOLUTION............")
    solution = SolverSaver("solution.out",mapIn.placedRouter)
    solution.writeInFile()
    print("SAUVEGARDE DE LA CARTE EN IMAGE\n")
    mapIn.saveASCIIMap()
    print("............FIN DU PROGRAMME............")

if __name__ == '__main__':
    main()
