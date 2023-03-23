from vosk import Model, KaldiRecognizer
import os
import sys
import pyaudio
import pyttsx3
import json
import core

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
    pack = stream.read(16000)
    if len(pack) == 0:
        break
    if gravacao.AcceptWaveform(pack):
        resultado = gravacao.Result()
        resultado = json.loads(resultado)

        if resultado is not None:
            frases = resultado['text']
            print(frases)

            if frases == 'me informe as horas' or frases == 'que horas são':
                sintese_voz(core.InformacaodoSistema.retornar_hora())
            if frases == 'qual é o seu nome' or frases == 'como você se chama':
                sintese_voz(core.InformacaodoSistema.retornar_nome())
            if frases == 'que dia é hoje':
                sintese_voz(core.InformacaodoSistema.retornar_dia())