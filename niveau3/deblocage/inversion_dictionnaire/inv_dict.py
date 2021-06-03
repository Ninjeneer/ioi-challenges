nbMots = int(input())

dictionnaire = []
for i in range(nbMots):
    mots = input().split()
    dictionnaire.append((mots[1], mots[0]))
dictionnaire.sort()
for entry in dictionnaire:
    print(entry[0] + " " + entry[1])
