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
                    # Ela pede para você repetir o comando pois não entendeu
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
                # Caso seja pedido para ler agenda entra nesse if
                elif texto.upper() in frases.gat_lerAgenda:
                    # Abre a agenda
                    with open("Agenda.txt", "a") as arquivo:
                        # Transfere a agenda para uma variavel
                        texto = arquivo.read()
                        # Checa se tem algo na agenda
                        if texto != "":
                            # Diz que vai ler a agenda
                            fn.flaFrase(random.choice(frases.fra_lerAgenda))
                            # Lê a agenda
                            fn.flaFrase(texto)
                        # Caso não tenha nada na agenda entra no else
                        else:
                            # Ela diz que não tem nada na agenda
                            fn.flaFrase(random.choice(frases.fra_agendaVazia))
                    texto = ""
                # Caso seja pedido a horas entra nesse if
                elif texto.upper() in frases.gat_horas:
                    fn.flaFrase(fn.informar_horas())
                    texto = ""
                elif texto.upper() in frases.gat_clima:
                    fn.flaFrase(fn.obter_clima())
                    texto = ""
                elif texto.upper() in frases.gat_limpeza:
                    fn.flaFrase(random.choice(frases.fra_fazerLimpeza))
                    fn.fazer_limpeza()
                    texto = ""
                elif texto.upper() in frases.gat_desligar:
                    fn.flaFrase(random.choice(frases.fra_desligar))
                    fn.desligar_com_verificacao(rec, mic)
                    texto = ""
                elif "PESQUISAR" in texto.upper():
                    texto = texto.replace("pesquisar", "").strip()
                    fn.pesquisar_google(texto)
                    texto = ""
                elif texto.upper() in frases.gat_visual:
                    fn.flaFrase(random.choice(frases.fra_visual))
                    fn.abrir_visual_studio_code()
                elif texto.upper()

                

