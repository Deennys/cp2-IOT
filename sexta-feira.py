import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import frases
import funcoes as fn

microfone = sr.Microphone()
rec = sr.Recognizer()

#Loop para aguardar a palavra chave
while texto.upper() not in frases.gat_sair:
    #inicializa o microfone
    with microfone as mic:
        # A sexta-feira pede para você acionar ela
        texto = fn.base(rec, mic, "Diga 'Ok sexta-feira'")
        # Caso for dito o gatilho a Sexta-feira é ativada
        if texto.upper() in frases.gat_inicial:
            # A Sexta-feira pergunta o que o mestre deseja fazer
            texto = fn.base(rec, mic, random.choice(frases.fra_inicial))
            # flag de controle para saber se a sexta_feira entendeu
            flag = 0
            # Se ela não entender o comando ela tenta novamente
            while texto != "" or texto.upper() in frases.gat_sair:
                # If para caso ela não entender o que disse 
                if flag == 1:
                    texto = fn.base(rec, mic, random.choice(frases.fra_nEntendi))
                flag = 1
                # Caso seja pedido para cadastrar novo evento entrara nesse if
                if texto.upper() in frases.gat_agenda:
                    # A Sexta-feira pergunta o que deseja adicionar na agenda
                    texto = fn.base(rec, mic, random.choice(frases.fra_agenda))
                    # Abre a agenda para adicionar o evento
                    with open("Agenda.txt", "a") as arquivo:
                        # adiciona o evento no final da agenda
                        arquivo.write(f"{texto}\n")
                    fn.flaFrase(random.choice(frases.fra_agendado))
                    texto = ""
                elif texto.upper() in frases.gat_lerAgenda:
                    with open("Agenda.txt", "a") as arquivo:
                        texto = arquivo.read()
                        if not texto:
                            fn.flaFrase(random.choice(frases.fra_lerAgenda))
                            fn.flaFrase(texto)
                        else:
                            fn.flaFrase(random.choice(frases.fra_agendaVazia))
                    texto = ""
                elif texto.upper() in frases.gat_horas:
                    fn.flaFrase(fn.informar_horas())
                    texto = ""
                elif texto.upper()

