# necessária a instalação da biblioteca pip install SpeechRecognition pyttsx3 pyaudio

import speech_recognition as sr
import pyttsx3
import datetime

# Inicializando o mecanismo de fala
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        comando = reconhecedor.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao se conectar ao serviço de reconhecimento de voz.")
        return ""

def executar_comando(comando):
    comando = comando.lower()

    if 'olá' in comando:
        falar("Olá! Como posso ajudar você?")
    elif 'hora' in comando:
        hora_atual = datetime.datetime.now().strftime("%H:%M")
        falar(f"A hora atual é {hora_atual}.")
    elif 'seu nome' in comando:
        falar("Eu sou um assistente virtual criado em Python.")
    elif 'sair' in comando:
        falar("Até logo!")
        return False
    else:
        falar("Desculpe, não entendi o comando.")
    
    return True

def main():
    while True:
        comando = ouvir()
        if comando:
            if not executar_comando(comando):
                break

if __name__ == "__main__":
    main()