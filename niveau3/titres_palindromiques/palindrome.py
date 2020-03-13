nbInput = int(input())

for i in range(nbInput):
    titre = input()

    if titre.lower().replace(' ', '') == titre[::-1].lower().replace(' ', ''):
        print(titre)
