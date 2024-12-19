import random
#variable
caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
usulo= int(input("Indroduzca la longitud de la contraseña: "))
contra=""

#codigo3
for i in range(usulo):
    contra+=random.choice(caracter)
print(f"Esta es tu contraseña: {contra}")
