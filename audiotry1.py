import speech_recognition as sr
r = sr.Recognizer()


with sr.Microphone() as source:
    print("Start talking: ")
    audio =r.listen(source)
    print("Stop talking.")

try:
    text = r.recognize_sphinx(audio)
    print("in the try block")
    print (text)
except sr.RequestError as e:
    print("I am here")
    print(e)