# Demander à l'utilisateur de choisir le type de conversion
def menu():
    print("Type de conversion :")
    print("1: Kilometres vers Miles (K vers M)")
    print("2: Miles vers Kilometres (M vers K)")


menu()
option = int(input("Entrez votre choix (1 ou 2): "))

distance = float(input("Entrez la distance a convertir: "))

if option == 1:
    output = float(distance * 0.621371)
    print(str(distance) + " kilometres equivalent a " + str(round(output, 2)) + " miles.")
elif option == 2:
    output = float(distance / 0.621371)
    print(str(distance) + " miles equivalent a " + str(round(output, 2)) + " kilometres.")