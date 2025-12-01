#Simple dictionary
alien_0 = {"color": "green", "points": 5}
#The simpliest dictuionary
alien_1 = {"color": "yellow"}
print(alien_0["color"])
print(alien_1["color"])
print("------------------------------")
#Adding new key-value pairs to a dictionary
alien_2 = {"color": "yellow"}
alien_2["color"] = "blue"
#Adding new key value parts
alien_2["position_x"] = 0
alien_2["position_y"] = 25
print(alien_2)
print("------------------------------")
#Dictionary to store random objects
favorite_lenguages = {
    "Jen":"Python",
    "sarah": "c",
    "edward" : "ruby",
    "phil" : "python",
}
print(f"Sarah favourite lenguage is: {favorite_lenguages['sarah']}")
print("------------------------------")
#looping through all key value pairs
for key, value in favorite_lenguages.items():
    print(f"{key.title()} ´s favourite \
lenguage is {value.title()}")
print("------------------------------")

covenant_grunt = {
    "color": "orange",
    "height": "small",
    "weapon": "plasma rifle",
    "health": 6,
    "points": 3,
 }

covenant_elite = {
    "color": "blue",
    "height" : "large",
    "weapon": "plasma sword",
    "health": 7,
    "points": 7,
}
covenant_jackal = {
    "color": "green",
    "height": "medium",
    "weapon": "plasma-gun",
    "hit_points": 7,
    "health": 3,
    "points": 2,
}
for key, value in covenant_grunt.items():
    print(key, value)
#nesitng
#estudiar - lista de diccionarios
#estudiar - lista de diccionarios
#estudiar -  diccionarios de diccionarios
covenants = [covenant_grunt, covenant_elite, covenant_jackal]
for aux in covenants:
    print("\n covenant", aux)
    for key, value in aux.items():
        print(key, value)
print("------------------------------")
#Diccionario en diccionarios
sensors = {
    "temperature": {
        "reading": 72,
        "units": "F",
    },
    "humidity": {
        "reading": 40,
        "units": "%",
    },
    "pressure": {
        "reading": 30,
        "units": "inHg",
    },
}
#Imprimir los valores de la temperatura
temp_reading = sensors["temperature"]["reading"]
temp_units = sensors["temperature"]["units"]
#lista en diccionarios
students = {
    "pablo":  ["cars", "programar en python"],
    "gerardo-pelon" : ["motos", "programar en arduino", "lo le gustan las tareas"],
    "gerardo-ame" : ["america"],
}
for name, hobbies in students.items():
    print(f"\n{name.title()} likes the following hobbies:")
    for hobby in hobbies:
        print(f"- {hobby.title()}")
#INVESTIGAR EL METODO GET