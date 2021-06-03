nbPages = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(2, nbPages+1):
    page = input()
    if i % 2 == 0:
        decallage = -3 * i
    else:
        decallage = 5 * i

    for lettre in page:
        if lettre.isalpha():
            if lettre.isupper():
                lettre = alphabet[(alphabet.index(lettre.lower()) + decallage) % 26].upper()
            else:
                lettre = alphabet[(alphabet.index(lettre) + decallage) % 26]
        print(lettre, end="")
    print("")
