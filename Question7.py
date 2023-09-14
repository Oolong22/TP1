#year: 31536000
#week: 604800
#day: 86400
#hour: 3600

# Demande à l'utilisateur de saisir le nombre de secondes
secondsEnd = seconds = int(input("Entrez le nombre de secondes: "))

# Calcul du nombre d'années contenant ces secondes (en supposant une année de 365 jours)
years = (seconds // 31536000)
seconds %= 31536000
# Calcul du nombre de semaines restantes dans le reste des secondes
weeks = (seconds // 604800)
seconds %= 604800
# Calcul du nombre de jours restants dans le reste des secondes
days = (seconds // 86400)
seconds %= 86400
# Calcul du nombre d'heures restantes dans le reste des secondes
hours = (seconds // 3600)
seconds %= 3600
# Calcul du nombre de minutes restantes dans le reste des secondes
minutes = (seconds // 60)
seconds %= 60


text = ("En " + (str(int(secondsEnd))) + " secondes, on a: ")

#Elimination des valeurs a 0
if years != 0:
    if years == 1:
        text += ((str(years)) + " annee, ")
    else:
        text += ((str(years)) + " annees, ")
else:
    pass

if weeks != 0:
    if weeks == 1:
        text += ((str(weeks)) + " semaine, ")
    else:
        text += ((str(weeks)) + " semaines, ")
else:
    pass

if days != 0:
    if days == 1:
        text += ((str(days)) + " jour, ")
    else:
        text += ((str(days)) + " jours, ")
else:
    pass

if hours != 0:
    if hours == 1:
        text += ((str(hours)) + " heure, ")
    else:
        text += ((str(hours)) + " heures, ")
else:
    pass

if minutes != 0:
    if minutes == 1:
        text += ((str(minutes)) + " minute, ")
    else:
        text += ((str(minutes)) + " minutes, ")
else:
    pass


text = text[:-2]

if seconds == 1:
    text += (" et " + (str(seconds)) + " seconde")
else:
    text += (" et " + (str(seconds)) + " secondes")

text += (".")

if secondsEnd < 1 and secondsEnd >=0:
    print("En 0 secondes, on a 0 secondes")
elif secondsEnd < 0:
    print("Nombre invalide")
else:
    print(text)







