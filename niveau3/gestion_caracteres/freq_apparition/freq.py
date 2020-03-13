userInput = input().upper()
longueur = 0
frequences = []
for i in range(26):
    frequences.append(0)

for car in userInput:
    if car >= 'A' and car <= 'Z':
        longueur += 1
        index = ord(car) - 65
        frequences[index] += 1

for i in range(26):
    frequences[i] = frequences[i] / longueur
    print(frequences[i])