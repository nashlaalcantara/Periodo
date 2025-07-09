import speech_recognition as speech_recog
import random

def trasnscription():
    mic = speech_recog.Microphone() 
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Por favor, hable")

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
    
        try:
            return recog.recognize_google(audio, language="es-ES")
        except speech_recog.UnknownValueError:
            print("No se entendió lo que dijiste")
            return None
    
count= 0
niveles= { 
    "facil": ["Femenino","Hola","Masculino"],
    "intermedio": ["Efímero","Paradigma","Sibilino"],
    "dificil": ["Rinoceronte","Otorrinolaringologia","Murcielago"] }
while True:
    if count <= 3:
        nivel= "facil"
    elif count <= 6:
        nivel= "intermedio"
    elif count <= 9:
        nivel= "dificil"
    else:
        print("Es todo gracias por jugar")
        break
    
    pala= random.choice(niveles[nivel])
    print("Tienes esta cantidad de puntos", count)
    print("...A juagr estas en el nivel",nivel, "...")
    print("Di", pala)
    palabra = trasnscription()

    if palabra  == pala:
        print("Es correcto")
        niveles[nivel].remove(pala)
        count = count + 1
    else:
        print("Es incorecto, escuche bien")

