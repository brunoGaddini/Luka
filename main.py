# Our main file

'''
# Online version
import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

# Open the mic for capture
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)  # Defines the audio source

        print(r.recognize_google(audio, language='pt-BR'))
'''

from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

# Speech synthesis
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id) # -1 US Voice / -2 Portuguese Voice

engine.say("Eu vou falar esse texto")
engine.runAndWait()

'''
https://www.youtube.com/watch?v=9aGC5Omlf_k
7:37
Criando a função para a síntese de voz
'''


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())

