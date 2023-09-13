#Demander poids et taille
weight = float(input("Entrez votre poids en kg: "))
height = float(input("Entrez votre taille en m: "))

#Calculer IMC
if height != 0:
    imc = round((weight/(height**2)), 2)
    print("Votre IMC est: " + str(imc))
else:
    print("Entrez une taille valide")

#Insuffisance pondérale: IMC inférieur à 18.5.
#Poids normal: IMC entre 18.5 et 24.9.
#Surpoids: IMC entre 25 et 29.9.
#Obésité: IMC de 30 ou plus

if imc < 18.5:
    print("Vous etes en sous-poids.")
elif imc >=18.5 and imc <25:
    print("Votre poids est normal.")
elif imc >=25 and imc <30:
    print("Vous etes en surpoids.")
elif imc >=30:
    print("Vous etes obese.")