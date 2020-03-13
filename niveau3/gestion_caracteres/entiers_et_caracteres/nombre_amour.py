userInput = input().split()

for enfant in userInput:
    val = 0
    for lettre in enfant:
        val += ord(lettre) - 65

    while val >= 10:
        val = sum([int(x) for x in str(val)])

    print(val, end=" ")