# Demander à l'utilisateur d'entrer les coefficients de l'équation quadratique
a = float(input("Veuillez entrer la valeur de a (coefficient de x^2): "))
b = float(input("Veuillez entrer la valeur de b (coefficient de x): "))
c = float(input("Veuillez entrer la valeur de c (terme constant): "))
# Calculer le discriminant
delta = (b**2 - 4*a*c)
# Vérifier si le discriminant est négatif (aucune racine réelle)

if delta < 0 :
    print("Le projectile n'atteint jamais l'altitude desiree.")

else:
    # Vérifier si le discriminant est nul (une seule racine réelle

    if delta == 0:
        # Calculer l'instant unique où le projectile atteint l'altitude
        x = ( (b*(-1))/(2*a))


        # Vérifier si l'instant est positif
        if x > 0:
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print("Instant de l'impact:", x)
        else:
            print("Le projectile n'atteint jamais l'altitude desiree.")

    else:
        x = (((b*(-1))-((delta)**0.5))/(2*a))
        y = (((b*(-1))+((delta)**0.5))/(2*a))

        print(x)
        print(y)
        # Vérifier si les instants sont positifs
       
        if x > 0 and y < 0:
            
            print("Instant de l'impact:", x)

        elif y > 0 and x < 0:
            
            print("Instant de l'impact:", y)

            # Afficher l'instant positif

        elif x > 0 and y > 0:
            
            print("Instant de l'impact:", x, "et", y)

            # Afficher les deux instants
            
        else:
            print("Le projectile n'atteint jamais l'altitude desiree.")