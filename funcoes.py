import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import frases
import datetime
import geocoder
import subprocess

def base(reconhecedor, microfone, frase):
    reconhecedor.adjust_for_ambient_noise(microfone)
    flaFrase(frase)
    audio = reconhecedor.listen(microfone)
    print("reconhecendo...")
    texto = reconhecedor.recognize_google(audio, language='pt-BR', encoding = "utf-8")
    print(texto)
    return texto

def flaFrase(frase):
    audio = gTTS(frase, lang='pt')
    audio.save('msg.mp3')
    playsound('msg.mp3')
    print(frase)

def informar_horas():
    agora = datetime.datetime.now()
    hora_atual = agora.strftime("%H:%M")
    return f"Agora são {hora_atual}."

def obter_localizacao_atual():
    g = geocoder.ip('me')
    
    if g.ok:
        endereco = g.address
        return f"A localização atual é: {endereco}."
    else:
        return "Não foi possível obter a localização atual."

    # Exemplo de uso
    # localizacao = obter_localizacao_atual()
    # print(localizacao)

def fazer_limpeza():
    # Limpar diretório "temp"
    subprocess.run('del /F /Q C:\\Temp\\*.*', shell=True)

    # Limpar diretório "%temp%"
    subprocess.run('del /F /Q %temp%\\*.*', shell=True)

    # Limpar diretório "recent"
    subprocess.run('del /F /Q %userprofile%\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\*.*', shell=True)

    # Executar o utilitário Cleanmgr (Limpador de Disco)
    subprocess.run('cleanmgr /sagerun:1', shell=True)

# Exemplo de uso
fazer_limpeza()


def desligar_com_verificacao():
    # Verificar se há algum processo em execução
    processos_abertos = subprocess.check_output('tasklist', shell=True)
    
    if b'explorer.exe' in processos_abertos:
        resposta = input("Existem programas em execução. Deseja forçar o desligamento? (s/n): ")
        if resposta.lower() == 's':
            os.system('shutdown /s /f /t 0')
        else:
            print("O desligamento foi cancelado.")
    else:
        os.system('shutdown /s /t 0')

# Exemplo de uso
desligar_com_verificacao()