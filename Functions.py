import json
from deepspeech import Model
import numpy as np
import speech_recognition as sr
import playsound


def logger(error_string):
    with open("./log.txt","a+") as log_:
        log_.write(error_string +'\n')

def get_configOutside():
    try:
        with open('jsondata.txt') as o1:
            dataoutside = json.loads(o1.read())
            return 1,dataoutside
    except Exception as e:
        logger("error - {}".format(e))
        print("error - {}".format(e))
        return 0,0

def takeinput():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=16000) as source:
        playsound(get_configOutside()[1]['mp3 tracks']['Speak now message'])
        audio = r.listen(source)
    return audio

def recognize(audio1):
    beam_width = 500
    model_name = "deepspeech-0.7.3-models.pbmm"
    if __name__ == '__main__':
        ds = Model(model_name)
        ds.setBeamWidth(beam_width)
        audio1 = np.frombuffer(audio1.frame_data, np.int16)

    return(ds.stt(audio1))

def liftgoesup():#pseudo func
    playsound("Yes, lift is going up")

def liftgoesdown():#psuedo func
    playsound("Yes, lift is going down")

def get_configInside():
    try:
        with open('jsondatainside.txt') as o1:
            datainside = json.loads(o1.read())
            return 1,datainside
    except Exception as e:
        logger("error - {}".format(e))
        print("error - {}".format(e))
        return 0,0

def floorchange(n):#pseudo func
    print('changing floor to: ',n)
    playsound(get_configInside()[1]['mp3 tracks']['changing floor message'])




