
import speech_recognition as sr
import pyttsx3 as lito
import requests 

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
        if "tchau" in response:
            fala("Tchau !!!")
            
            break
        if 'good' in response:
            response_r = requests.get('http://localhost:8000/blog/nigth/')
            if response_r.status_code == 200: 
                response_r_text = response_r.text
                fala(response_r_text)
        
        #ativar spotify
        if  "música" in response:
            fala("Tocando música")
           


    except sr.UnknownValueError:
       fala("O Lito não te escutou")
       
    except sr.RequestError as e:
        print(f"Eita deu Ruim, o Lito caiu; {e}")
