import json
import speech_recognition as sr
from playsound import playsound
from word2number import w2n
import Functions

with open('./jsondatainside.txt') as o1:
      data = json.loads(o1.read())

number_of_floors = data['wake']['number of floors']
print(number_of_floors)

while(True):
    audio1 = Functions.takeinput() #to listen to the wake word
    text1 = Functions.recognize(audio1)
    print("you said:" + text1)
    k = 0

    if(text1 == data['wake']['keyphrase']):
        playsound(data['mp3 tracks']['make floor choice'])
        while(k == 0):
            audio2 = Functions.takeinput()
            text2 = Functions.recognize(audio2)
            try:
                print("Sphinx thinks you said " + text2)
                try:
                    n = w2n.word_to_num(text2)
                    Functions.floorchange(n)
                    k = 1
                except ValueError:
                    playsound(data['mp3 tracks']['choice again'])
            except sr.UnknownValueError:
                playsound(data['mp3 tracks']['error message'])
                playsound(data['mp3 tracks']['choice again'])
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

    elif(text1==data['wake']['stopphrase'] or 'stop' in text1):
        break;
    else:
        playsound(data['mp3 tracks']['error message'])
        playsound(data['mp3 tracks']['choice again'])



