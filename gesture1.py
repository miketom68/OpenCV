import speech_recognition as sr 
from gtts import gTTS 
lang='en'
r1=sr.Recognizer()
res=['how are you','']
def speak():
    output=gTTS()
while 1:
    try:
        with sr.Microphone() as source:
            r1.adjust_for_ambient_noise(source,duration=0.2)
            audio=r1.listen(source)
            text=r1.recognize_google(audio)
            text=text.lower()
            print(text)
    except sr.UnknownValueError():
        r1=sr.Recognizer()
        continue


