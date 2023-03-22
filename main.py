from vosk import Model, KaldiRecognizer
import os
import sys
import pyaudio
import pyttsx3
import json

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def sintese_voz(frases):
    engine.say(frases)
    engine.runAndWait()


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
        resultado = gravacao.Result()
        resultado = json.loads(resultado)

        if resultado is not None:
            frases = resultado['text']