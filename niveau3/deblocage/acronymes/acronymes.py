acronyme = input()
nbLivres = int(input())

for i in range(nbLivres):
    titre = input().lower()
    mots = titre.split()

    if len(acronyme) != len(mots):
        continue

    valid = True
    for i in range(len(acronyme)):
        if not mots[i].startswith(acronyme[i].lower()):
            valid = False

    if valid:
        print(titre.title())
