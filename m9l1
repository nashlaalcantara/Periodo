import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 225)  
uno= int(input("el primer numero porfavor"))
seg= int(input("el segundo numero porfavor"))
r= uno + seg
engine.say(r)
engine.runAndWait()
