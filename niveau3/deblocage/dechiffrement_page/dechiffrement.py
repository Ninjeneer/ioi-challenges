cle = input()
page = input()

for lettre in page:
    if lettre.upper() >= 'A' and lettre.upper() <= 'Z':
        index = ord(lettre.upper()) - 65
        if lettre.isupper():
            lettre = cle[index].upper()
        else:
            lettre = cle[index]
    print(lettre, end="")
