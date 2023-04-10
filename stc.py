import speech_recognition as sr 
import pyfirmata 
import time
port='COM3'
board=pyfirmata.Arduino(port)
time.sleep(2.0)
r1=sr.Recognizer()
while 1:
    try:
        with sr.Microphone() as source:
            r1.adjust_for_ambient_noise(source,duration=0.1)
            audio=r1.listen(source)
            text=r1.recognize_google(audio)
            text=text.lower()
            if 'on' in text:
                board.digital[9].write(1)
                print(text)
            elif 'reduce':
                board.digital[9].write(0.4)
                print(text)
            elif 'dim':
                board.digital[9].write(0.2)
                print(text)
            elif 'off' in text:
                board.digital[9].write(0)
                print(text)
    except sr.UnknownValueError():
        r1=sr.Recognizer()
        continue


