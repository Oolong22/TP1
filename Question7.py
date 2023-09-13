#year: 31536000
#week: 604800
#day: 86400
#hour: 3600

# Demande à l'utilisateur de saisir le nombre de secondes
secondsEnd = seconds = float(input("Entrez le nombre de secondes: "))

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
# Affichage du nombre d'années, de semaines, de jours, d'heures, de minutes et de secondes

text = ("En " + (str(int(secondsEnd))) + " secondes, on a: ")

if years != 0:
    text += ((str(int(years))) + " annees, ")
else:
    pass

if weeks != 0:
    text += ((str(int(weeks))) + " semaines, ")
else:
    pass

if days != 0:
    text += ((str(int(days))) + " jours, ")
else:
    pass

if hours != 0:
    text += ((str(int(hours))) + " heures, ")
else:
    pass

if minutes != 0:
    text += ((str(int(minutes))) + " minutes, ")
else:
    pass

text = text[:-2]

text += (" et " + (str(int(seconds))) + " secondes")

text += (".")

print(text)






