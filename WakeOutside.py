import json
import speech_recognition as sr
wake_outside='''
{
"wake": {
    "keyphrase": "open",
    "threshold": 1e-30,
    "chunk_size": 960
  }
}
'''
def takeinput():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    return audio

def liftgoesup():#pseudo func
    print("yes lift is going up")

def liftgoesdown():#psuedo func
    print("yes lift is going down")

r = sr.Recognizer()
audio1 = takeinput() #to listen to the wake word
print("you said:" + r.recognize_sphinx(audio1))
data = json.loads(wake_outside)

k = 0

if(r.recognize_sphinx(audio1) == data['wake']['keyphrase']):
    print("Please choose up or down")
    while(k == 0):
        with sr.Microphone() as source:
            audio2 = takeinput()
            print("you said:" + r.recognize_sphinx(audio2))
        if(r.recognize_sphinx(audio2) == 'up'):
            k = 1
            liftgoesup()#pseudo function
        elif(r.recognize_sphinx(audio2) == 'down'):
            k = 1
            liftgoesdown()#pseudo function
        else:
            print("Please make the choice again")
