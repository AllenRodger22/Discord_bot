import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()


# ----------MICROPHONE-------------

def MicRecogniton():
    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration= 0.2)
                audio = r.listen(mic)
                text = r.recognize_google(audio,language = 'pt-BR')
                text = text.lower()
                print("Recognized text:"+ text)


        except sr.UnknownValueError():
            r = sr.Recognizer()
            continue

#------------AUDIO FILES-----------
def AudioRecogition(file):
    audio = sr.AudioFile(file)
    with audio as source:
        track = r.record(source)
        text = r.recognize_google(track, language='pt-BR')
        text = text.lower()
        print(text)


AudioRecogition('audio_whatsapp_alisson.wav')