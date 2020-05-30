import json
import speech_recognition as sr
from playsound import playsound

r = sr.Recognizer()

with open('jsondata.txt') as o1:
      data = json.loads(o1.read())

def takeinput():
    with sr.Microphone() as source:
        playsound(data['mp3 tracks']['Speak now'])
        audio = r.listen(source)
    return audio

def recognize(audio1):
    return r.recognize_sphinx(audio1)

def liftgoesup():#pseudo func
    playsound(data['mp3 tracks']['upmessage'])

def liftgoesdown():#psuedo func
    playsound(data['mp3 tracks']['downmessage'])
