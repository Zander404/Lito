
import speech_recognition as sr
import pyttsx3 as lito

# Pegar o som do Microfone
microfone = sr.Recognizer()
fala = lito.speak
# speaker = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Fale para o Lito, vai!")
        audio = microfone.listen(source)

    #Reproduzir oq foi dito
    try:
        response = microfone.recognize_google(audio_data=audio, language="pt-BR")
        print("O Lito escutou:  " + response)

        #condição de saida da Aplicação
        if response == "tchau":
            fala("Tchau !!!")
            
            break
        
        #ativar spotify
        if response == "música":
            fala("Tocando música")
           


    except sr.UnknownValueError:
       fala("O Lito não te escutou")
       
    except sr.RequestError as e:
        print("Eita deu Ruim, o Lito caiu; {0}".format(e))
