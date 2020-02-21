from math import ceil

taille = (int(input()))

prefixe = ""
dernierCar = 'a'

for i in range(taille):
   car = chr(ord('a') + i)
   print(prefixe, end="")
   prefixe += car
   for j in range(taille * 2 - len(prefixe) * 2):
      print(car, end="")
   print(prefixe[::-1])
   dernierCar = car

prefixe = prefixe[0:len(prefixe)-1]
dernierCar = chr(ord(car) - 1)

for i in range(taille - 1):
    car = chr(ord(dernierCar) - i)
    prefixe = prefixe[0:len(prefixe)-1]
    print(prefixe, end="")
    for j in range (taille * 2 - len(prefixe) * 2 - 1):
        print(car, end="")
    print(prefixe[::-1])
