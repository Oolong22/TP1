# Demande à l'utilisateur d'entrer une phrase.
sentence = input("Entrez une phrase: ")
# Divise la phrase en mots en utilisant l'espace comme séparateur et compte le nombre de mots
#wordList = split(sentence)
wordCount = len(sentence.split())
# Affiche le nombre de mots dans la phrase
print("La phrase contient " + str(wordCount) + " mots.")
# Affiche la phrase en lettres majuscules
print("Phrase en majuscules: " + str(sentence.upper()))
