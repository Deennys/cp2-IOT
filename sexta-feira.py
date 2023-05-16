import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import frases
import funcoes

microfone = sr.Microphone()
rec = sr.Recognizer()

#Loop para aguardar a palavra chave
while texto.upper not in frases.gat_sair:
    with microfone as mic:
        texto = funcoes.base(rec, mic, "Diga 'Ok sexta-feira'")
        if texto.upper() in frases.gat_inicial:
            texto = funcoes.base(rec, mic, random.choice(frases.fra_inicial))
            if texto.upper() in frases.gat_agenda:
                rec.adjust_for_ambient_noise(mic)
                frase = random.choice(frases.fra_inicial)
                audio = gTTS(frase, lang='pt')
                audio.save('msg.mp3')
                playsound('msg.mp3')
                print(frase)
                audio = rec.listen(mic)
                print("reconhecendo...")
                texto = rec.recognize_google(audio, language='pt')
                print(texto)
