import json #for loading json data files
from deepspeech import Model #deepspeech api
import numpy as np #convert audio frame data into numpy data
import speech_recognition as sr #wrapper library
import os
import datetime

r = sr.Recognizer()

def playsound(message,data): #to play saved audio tracks
    str = data['mp3 tracks'][message]
    os.system("mpg123 " + str)

def logger(error_string): #to append date, time and the error that occured
    with open("Log error files/log.txt", "a+") as log_:
        log_.write(displaytimedate()[0] + " " +displaytimedate()[1])
        log_.write(" Error: " + error_string + '\n')

def add_prediction(predicted_string): #to append date, time and predicted string
    try:
        with open("Log error files/Word prediction file.txt","a+") as pred_:
            pred_.write(displaytimedate()[0]+" "+displaytimedate()[1])
            pred_.write(" String predicted is : " + predicted_string + '\n')
    except Exception as e:
        logger("error - {}".format(e))

def displaytimedate(): #returns date and time to function call
    now = datetime.datetime.now()
    return("Current date and time : ",now.strftime("%Y-%m-%d %H:%M:%S"))


def get_configOutside(): #loads file for WakeOutside.py
    try:
        with open('Config files/jsondataoutside.txt') as o1:
            dataoutside = json.loads(o1.read())
            return 1, dataoutside
    except Exception as e:
        logger("error - {}".format(e)) #calls logger function and passes error string
        return 0, 0

def take_input(data): #takes audio input using pyaudio and speech recognition
    with sr.Microphone(sample_rate=16000, device_index=data['wake']['device_index']) as source: #16khz is the sample rate expected by models
        r.adjust_for_ambient_noise(source) #adjusting to background noise
        playsound("Speak_now_message", data) #tells user to speak now
        audio = r.listen(source)
    return audio #returns audio input


def recognize_DS(audio1, data):
    beam_width = 500 #how many different word sequences will the model take into account
    model_name = data['wake']['model name']
    ds = Model(model_name)
    ds.setBeamWidth(beam_width)
    audio1 = np.frombuffer(audio1.frame_data, np.int16) #converts into numpy array
    return (ds.stt(audio1)) #returning predicted audio


def recognize_Sphinx(audio1):
    return r.recognize_sphinx(audio1) #returning audio via pocketsphinx

def liftgoesup(datao):  # pseudo func
    playsound("up_message",datao)

def liftgoesdown(datao):  # psuedo func
    playsound("down_message",datao)

def get_configInside(): #loads file for WakeInside.py
    try:
        with open('Config files/jsondatainside.txt') as o1:
            datainside = json.loads(o1.read())
            return 1, datainside
    except Exception as e:
        logger("error - {}".format(e)) #calls logger function and passes error string
        return 0, 0


def floor_change(n, datai):  # pseudo func
    print('changing floor to: ', n)
    playsound("changing_floor_message",datai)


