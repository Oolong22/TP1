# Affiche un menu d'opérations disponibles
def menu():
    print("Choisissez une operation:")
    print("    1. Addition")
    print("    2. Soustraction")
    print("    3. Multiplication")
    print("    4. Division")
    return

def division(): #Fonction qui effectue la division
    if (secondNum == 0):
        print("Erreur: Division par zero.")
    else:
        answer = float(firstNum / secondNum)
        print("Resultat: " + str(answer))
        return
    
# Demande à l'utilisateur de saisir le numéro de l'opération choisie
menu()
option = int(input())

# Demande à l'utilisateur de saisir deux nombress
firstNum = float(input("Entrez le premier nombre: "))
secondNum = float(input("Entrez le second nombre: "))

if option == 1:   #Addition
    answer = float(firstNum + secondNum)
    print("Resultat: " + str(answer))
elif option == 2: #Soustraction
    answer = float(firstNum - secondNum)
    print("Resultat: " + str(answer))
elif option == 3: #Multiplication
    answer = float(firstNum * secondNum)
    print("Resultat: " + str(answer))
elif option == 4: #Division
    division()
else:
    print("Choix invalide")


