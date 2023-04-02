# Our main file
import speech_recognition as sr
# import pyaudio

# Create a recognizer
r = sr.Recognizer()

# Open the mic for capture
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)  # Defines the audio source

        print(r.recognize_google(audio, language='pt-BR'))

