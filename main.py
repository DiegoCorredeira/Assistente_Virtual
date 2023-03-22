import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import os
import sys
import pyaudio

model = Model('model')
gravacao = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    pack = stream.read(4000)
    if len(pack) == 0:
        break
    if gravacao.AcceptWaveform(pack):
        print(gravacao.Result())
    else:
        print(gravacao.PartialResult())

r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        print(r.recognize_google(audio, language="pt-BR", show_all=False))