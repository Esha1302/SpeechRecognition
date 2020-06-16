from word2number import w2n
from Functions import *
import time

p = 1
while(True and p!=0):
    time.sleep(5)
    result, datai = get_configInside()
    if result == 0:
        playsound("file not found message", datai)
        continue
    else:
        number_of_floors = datai['wake']['number of floors']
        while(True):
            audio1 = takeinput() #to listen to the wake word
            try:
                text1 = recognizeSphinx(audio1)
                add_prediction(text1)
                k = 0
                if(datai['wake']['keyphrase'] in text1):
                    playsound("floor choice message",datai)
                    while(k == 0):
                        audio2 = takeinput()
                        try:
                            text2 = recognizeDS(audio2)
                            add_prediction(text2)
                            try:
                                n = w2n.word_to_num(text2)
                                if(n == datai['wake']['current floor']):
                                    playsound("same floor message",datai)
                                    continue
                                else:
                                    floorchange(n)
                                    k = 1
                            except ValueError as e:
                                logger(e)
                                playsound("choice again messgae", datai)
                                continue
                        except sr.UnknownValueError as e:
                            logger(e)
                            playsound("error message", datai)
                            playsound("choice again message", datai)
                elif(datai['wake']['stopphrase'] in text1):
                    p = 0
                    break;
                else:
                    playsound("choice again messgae", datai)

            except sr.RequestError as e:
                logger(e)
                playsound("error message", datai)
                playsound("choice again message", datai)
