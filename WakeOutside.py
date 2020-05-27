import json
import speech_recognition as sr
from playsound import playsound
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
        playsound('C:/Users/Admin/Downloads/speaknow.mp3')
        audio = r.listen(source)
    return audio

def liftgoesup():#pseudo func
    playsound('C:/Users/Admin/Downloads/yesliftgoingup.mp3')

def liftgoesdown():#psuedo func
    playsound('C:/Users/Admin/Downloads/yesliftgoingdown.mp3')

r = sr.Recognizer()
audio1 = takeinput() #to listen to the wake word
print("you said:" + r.recognize_sphinx(audio1))
data = json.loads(wake_outside)

k = 0

if(r.recognize_sphinx(audio1) == data['wake']['keyphrase']):
    playsound('C:/Users/Admin/Downloads/chooseupordown.mp3')
    while(k == 0):
        with sr.Microphone() as source:
            audio2 = takeinput()
            try:
                print("Sphinx thinks you said " + r.recognize_sphinx(audio2))
                if(r.recognize_sphinx(audio2) == 'up'):
                    k = 1
                    liftgoesup()#pseudo function
                elif(r.recognize_sphinx(audio2) == 'down'):
                    k = 1
                    liftgoesdown()#pseudo function
                else:
                    playsound('C:/Users/Admin/Downloads/choice again.mp3')
            except sr.UnknownValueError:
                playsound('C:/Users/Admin/Downloads/sphinxcouldnot.mp3')
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
