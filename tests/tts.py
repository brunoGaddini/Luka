import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id) # -1 US Voice / -2 Portuguese Voice

engine.say("Eu vou falar esse texto")
engine.runAndWait()