import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)
engine.say("hello anugrah")
engine.runAndWait()

def bolo(commond):
    engine.say(commond)
    engine.runAndWait()
bolo("how are you") 