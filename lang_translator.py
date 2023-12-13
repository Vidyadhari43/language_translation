from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import os
import pyaudio

mic=sr.Microphone(device_index=20)
recognition=sr.Recognizer()

with mic as source:
    print("Say 'Hello' to intiate")
    recognition.adjust_for_ambient_noise(source,0.5)
    audio1=recognition.listen(source)
    text1=recognition.recognize_google(audio1)
    text1=text1.lower()
if  'hello'  in  text1:
    trans=Translator()
    with mic as source:
        print("say the sentence to translate")
        recognition.adjust_for_ambient_noise(source,0.5)
        audio2=recognition.listen(source)
        text2=recognition.recognize_google(audio2)
        try:
            text2 = trans.translate(text2, src='en', dest='hi')
            speech2 = gTTS(text=text2.text, lang='hi', slow=False)
            speech2.save("translated.mp3")
            os.system("xdg-open translated.mp3") #os.system(start translated.mp3) for windows
        except sr.UnknownValueError:
            print("Unable to Understand the input")
        except sr.RequestError as re:
            print("Unable to provide the required output: {}".format(re))
