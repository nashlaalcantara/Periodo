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
    
def maq():
    consejos = ["Cartón: edificios, casas, y puentes.", 
                "Botellas plásticas: rascacielos."
                , "Latas: contenedores industriales o tanques de agua."
                , "Palitos de helado: bancos y mesas de picnic."
                , "Papel: árboles, arbustos y césped."]
    return random.choice(consejos)

def map():
    consejos = ["Cartón: casitas de hadas y pequeños caminos.", 
                "Tapas de botellas: estanques o fuentes."
                , "Piedras y conchas: decoraciones naturales."
                , "Retazos de tela: mini banderas o columpios."
                , "Cajas de huevos: colinas y montículos."]
    return random.choice(consejos)

def cho():
    consejos = ["Reducir: Evitar el uso de productos de un solo uso, como botellas de plástico y bolsas.", 
                "Reutilizar: Dar una segunda vida a los objetos, como frascos de vidrio y ropa vieja."
                , "Reciclar: Separar y reciclar adecuadamente el papel, plástico, vidrio y metal."
                , "Apagar luces y aparatos electrónicos cuando no estén en uso."
                , "Usar bombillas de bajo consumo o LED."]
    return random.choice(consejos)