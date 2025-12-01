"""
    Slicing a list
"""
players = ['charles', 'martina', 'florence', 'eli']
print ("Lista original:", players)
print("Slice ", players[0:3]) #-> ['charles', 'martina', 'florence']
print("Slice ", players[1:4]) #-> ['martina', 'florence', 'eli']
print("Slice ", players[:4])  #-> ['charles', 'martina', 'florence', 'eli']
print("Slice ", players[2:])  #-> ['florence', 'eli']
print("Slice ", players[-3:]) #-> ['martina', 'florence', 'eli']
print("Slice ", players[5:]) #-> []
#Slicing en un for
players = ['charles', 'martina', 'florence', 'eli',]
for player in players[0:3]:
    print("Jugador:", player.title())
#Copiar una lista
players = ['charles', 'martina', 'florence', 'eli']
#player_2 = players <-- Esto no funciona
player_2 = players[:] #Copia correcta
player_2 = list(players) #Otra forma de copiar una lista
player_3 = players.copy() #Otra forma de copiar una lista
print("--------------------------------")
cars = ["Bnw", "Toyota", "Volkswagen", "Porche"]
print(cars)
cars[0]= "Bmw"
cars[3] = "Porsche"
print (cars)