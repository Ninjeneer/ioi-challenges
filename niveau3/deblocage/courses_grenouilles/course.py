nbGrenouilles = int(input())
nbTours = int(input())

grenouilles = []
scores = []
for i in range(nbGrenouilles):
    scores.append(0)
    grenouilles.append(0)


        
for i in range(nbTours):
    if grenouilles.count(max(grenouilles)) == 1:
        indiceGrenouille = grenouilles.index(max(grenouilles))
        scores[indiceGrenouille] += 1
    resultatTour = input()
    numGrenouille = int(resultatTour.split(' ')[0]) - 1
    saut = int(resultatTour.split(' ')[1])

    grenouilles[numGrenouille] += saut


grenouilleGagnante = scores.index(max(scores)) + 1
print(grenouilleGagnante)
