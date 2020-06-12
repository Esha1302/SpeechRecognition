import json
from deepspeech import Model
import numpy as np
import speech_recognition as sr
import os
import datetime

r = sr.Recognizer()


def logger(error_string):
    with open("Log error files/log.txt", "a+") as log_:
        log_.write(error_string + '\n')

def add_prediction(predicted_string):
    with open("Log error files/Word prediction files.txt","a+") as pred_:
        pred_.write(displaytimedate())
        pred_.write("String precited is : ",predicted_string + '\n')

def displaytimedate():
    now = datetime.datetime.now()
    return("Current date and time : ",now.strftime("%Y-%m-%d %H:%M:%S"))


def get_configOutside():
    try:
        with open('Config files/jsondata.txt') as o1:
            dataoutside = json.loads(o1.read())
            return 1, dataoutside
    except Exception as e:
        logger("error - {}".format(e))
        print("error - {}".format(e))
        return 0, 0


def takeinput(datao):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #playsound("Speak now message", datao)
        print("speak now")
        audio = r.listen(source)
    return audio


def recognizeDS(audio1):
    beam_width = 500
    model_name = "Models/deepspeech-0.7.3-models.pbmm"
    ds = Model(model_name)
    ds.setBeamWidth(beam_width)
    audio1 = np.frombuffer(audio1.frame_data, np.int16)
    return (ds.stt(audio1))


def recognizeSphinx(audio1):
    print("hello")
    return r.recognize_sphinx(audio1)

def liftgoesup(datao):  # pseudo func
    playsound("up message",datao)


def liftgoesdown(datao):  # psuedo func
    playsound("down message",datao)


def get_configInside():
    try:
        with open('Config files/jsondatainside.txt') as o1:
            datainside = json.loads(o1.read())
            return 1, datainside
    except Exception as e:
        logger("error - {}".format(e))
        print("error - {}".format(e))
        return 0, 0

def floorchange(n, datai):  # pseudo func
    print('changing floor to: ', n)
    playsound("changing floor message",datai)


def playsound(message,data):
    str = data['mp3 tracks'][message]
    os.system("mpg123 " + str)

