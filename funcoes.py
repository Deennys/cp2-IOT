import os
import subprocess
import requests
import webbrowser
import shutil
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import frases
import datetime
import geocoder

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
    hora = agora.strftime("%H")
    minutos = agora.strftime("%M")
    if minutos == "00":
      return f'Agora são {hora} Horas em ponto'
    else:
      return f'Agora são {hora} horas e {minutos} minutos'

def obter_localizacao_atual():
    g = geocoder.ip('me')
    
    if g.ok:
        cidade = g.city
        return cidade
    else:
        return None

    # Exemplo de uso
    # localizacao = obter_localizacao_atual()
    # print(localizacao)

def obter_clima():
    cidade = obter_localizacao_atual()
    if cidade:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=97fe458ffc200a1a50f0bcabdd8d8166&units=metric&lang=pt_br"
        
        try:
            response = requests.get(url)
            dados_clima = response.json()
            
            if response.status_code == 200:
                temperatura = dados_clima["main"]["temp"]
                descricao = dados_clima["weather"][0]["description"]
                
                resultado = f"Em {cidade}, a temperatura atual é de {temperatura}°C com {descricao}."
                return resultado
            else:
                return "Não foi possível obter as informações de clima, Desculpe"
        except requests.exceptions.RequestException as e:
            return "Ocorreu um erro ao fazer a solicitação à API de clima, Desculpe!"
    else:
        return "Não foi possível obter a sua localização, Desculpe!"

def limpar_pasta(pasta):
    if os.path.exists(pasta):
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            try:
                if os.path.isfile(caminho_arquivo):
                    os.unlink(caminho_arquivo)
            except Exception as e:
                print(f"Erro ao excluir {caminho_arquivo}: {e}")

def fazer_limpeza():
    # Limpar diretório "temp"
    limpar_pasta('C:\\Temp')

    # Limpar diretório "%temp%"
    limpar_pasta(os.environ['TEMP'])

    # Limpar diretório "recent"
    limpar_pasta(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Recent'))

    # Executar o utilitário Cleanmgr (Limpador de Disco)
    subprocess.run(['cleanmgr', '/sagerun:1'], shell=True)

    # Exemplo de uso
    # fazer_limpeza()


def desligar_com_verificacao(reconhecedor, microfone):
    # Verificar se há algum processo em execução
    processos_abertos = subprocess.check_output('tasklist', shell=True)
    
    if b'explorer.exe' in processos_abertos:
        resposta = base(reconhecedor, microfone, "Existem programas em execução. Deseja forçar o desligamento?")
        if resposta.upper() in frases.afirmativo:
            os.system('shutdown /s /f /t 0')
        else:
            flaFrase("O desligamento foi cancelado.")
    else:
        os.system('shutdown /s /t 0')

    # Exemplo de uso
    #desligar_com_verificacao()

def pesquisar_google(termo_pesquisa):
    pesquisa_url = f"https://www.google.com/search?q={termo_pesquisa}"
    webbrowser.open(pesquisa_url)
    resposta = f"Abrindo resultados da pesquisa para '{termo_pesquisa}'."
    flaFrase(resposta)

def abrir_visual_studio_code():
    try:
        subprocess.Popen(["code"])
    except FileNotFoundError:
        flaFrase("O Visual Studio Code não está instalado ou o comando 'code' não está configurado corretamente.")


def obter_noticias_do_dia():

    url = "https://newsapi.org/v2/top-headlines?country=br&apiKey=2e3baa5814424dc1b7ae6b21d3b2945f"
    
    try:
        response = requests.get(url)
        dados_noticias = response.json()
        
        if response.status_code == 200:
            noticias = dados_noticias["articles"]
            resultado = "Notícias do dia:\n"
            
            for i, noticia in enumerate(noticias):
                resultado += f"{i+1}. {noticia['title']}\n"
            
            return resultado
        else:
            return "Não foi possível obter as notícias do dia. Verifique a chave da API."
    except requests.exceptions.RequestException as e:
        return "Ocorreu um erro ao fazer a solicitação à API de notícias."