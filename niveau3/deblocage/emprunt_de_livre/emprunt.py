nbLivres = 0
nbJours = 0
livres = []

userInput = input()
nbLivres = int(userInput.split(' ')[0])
nbJours = int(userInput.split(' ')[1])

for i in range(nbLivres):
   livres.append(0)

for i in range(nbJours):
   nbClientsJour = int(input())
   for j in range(nbClientsJour):
      userInput = input()
      indiceLivre = int(userInput.split(' ')[0])
      duree = int(userInput.split(' ')[1])

      if livres[indiceLivre] == 0:
         livres[indiceLivre] = duree
         print(1)
      else:
         print(0)

   for j in range(nbLivres):
      if livres[j] > 0:
         livres[j] -= 1













