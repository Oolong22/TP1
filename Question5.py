# Demande à l'utilisateur d'entrer le montant initial de l'investissement
argent = float(input("Entrez le montant initial: "))
# Demande à l'utilisateur d'entrer le taux d'intérêt annuel en pourcentage
interet = float(input("Entrez le taux d'interet annuel (en %): "))
# Demande à l'utilisateur d'entrer le nombre d'années de l'investissement
tempsAn = float(input("Entrez le nombre d'annees de l'investissement: "))
# Calcule le montant final en utilisant la formule de l'intérêt composé
montantFinal = round((((1 + (interet/100))**tempsAn)*argent), 2)
# Affiche le montant final avec deux décimales
print("Montant final apres 25 ans: " + str(montantFinal))

#380000
#4.2
#25