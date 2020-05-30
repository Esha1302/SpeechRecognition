import json
import speech_recognition as sr
from playsound import playsound
import Functions
import os

with open('./jsondata.txt') as o1:
      data = json.loads(o1.read())

while(True):

    audio1 = Functions.takeinput() #to listen to the wake word

    text1 =  Functions.recognize(audio1)
    #print("you said:" + text1)
    k = 0

    if(text1 == data['wake']['keyphrase'] or 'open' in text1):

        playsound(data['mp3 tracks']['upordown'])

        while(k == 0):

            audio2 = Functions.takeinput()
            text2 = Functions.recognize(audio2)

            try:
                #print("Sphinx thinks you said " + text2)
                if 'up' in text2 or text2 in data['up']:
                    k = 1
                    Functions.liftgoesup()#pseudo function
                elif 'down' in text2 or text2 in data['down']:
                    k = 1
                    Functions.liftgoesdown()#pseudo function
                else:
                    #print("Sphinx thinks you said " + text2)
                    playsound(data['mp3 tracks']['choice again'])

            except sr.UnknownValueError:
                playsound(data['mp3 tracks']['errormessage'])

            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

    elif(text1==data['wake']['stopphrase'] or 'stop' in text1):
        break;

    else:
        playsound(data['mp3 tracks']['errormessage'])
        playsound(data['mp3 tracks']['choice again'])





