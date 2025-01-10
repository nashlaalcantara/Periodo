import random
#variable
def gene(pass_length):
    caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra=""

#codigo
    for i in range(pass_length):
        contra+=random.choice(caracter)
    return contra

def emoji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Escudo"
