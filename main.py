# Our main file

import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# Open the mic for capture
with sr.Microphone() as source:
    audio = r.listen(source) # Defines the audio source

    print(r.recognize_google(audio))