import json
import speech_recognition as sr
from playsound import playsound
r = sr.Recognizer()

def logger(error_string):
    with open("./log.txt","a+") as log_:
        log_.write(error_string +'\n')

def get_configOutside():
    try:
        with open('./jsondata.txt') as o1:
            dataoutside = json.loads(o1.read())
            return 1,dataoutside
    except Exception as e:
        logger("error - {}".format(e))
        print("error - {}".format(e))
        return 0,0

def takeinput():
    with sr.Microphone() as source:
        playsound(get_configOutside()[1]['mp3 tracks']['Speak now'])
        audio = r.listen(source)
    return audio

def recognize(audio1):
    return r.recognize_sphinx(audio1)

def liftgoesup():#pseudo func
    playsound(get_configOutside()[1]['mp3 tracks']['upmessage'])

def liftgoesdown():#psuedo func
    playsound(get_configOutside()[1]['mp3 tracks']['downmessage'])

def get_configInside():
    try:
        with open('./jsondatainside.txt') as o1:
            datainside = json.loads(o1.read())
            return 1,datainside
    except Exception as e:
        logger("error - {}".format(e))
        print("error - {}".format(e))
        return 0,0

def floorchange(n):
    print('changing floor to: ',n)
    playsound(get_configInside()[1]['mp3 tracks']['changing floor message'])
