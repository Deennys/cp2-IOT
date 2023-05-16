import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import frases

def base(reconhecedor, microfone, frase):
    reconhecedor.adjust_for_ambient_noise(microfone)
    flaFrase(frase)
    audio = reconhecedor.listen(microfone)
    print("reconhecendo...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print(texto)
    return texto

def flaFrase(frase):
    audio = gTTS(frase, lang='pt')
    audio.save('msg.mp3')
    playsound('msg.mp3')
    print(frase)