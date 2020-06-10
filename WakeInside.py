from word2number import w2n
from Functions import *
import time
p = 1
while(True and p!=0):
    time.sleep(5)
    result, datai = get_configInside()
    if result == 0:
        print("File not found")
        continue
    else:
        number_of_floors = datai['wake']['number of floors']
        while(True):
            audio1 = takeinput() #to listen to the wake word
            text1 = recognize(audio1)
            print("you said:" + text1)
            k = 0
            if(text1 == datai['wake']['keyphrase']):
                playsound(datai['mp3 tracks']['make floor choice'])
                while(k == 0):
                    audio2 = takeinput()
                    text2 = recognize(audio2)
                    try:
                        print("Sphinx thinks you said " + text2)
                        try:
                            n = w2n.word_to_num(text2)
                            floorchange(n)
                            k = 1
                        except ValueError:
                            playsound(datai['mp3 tracks']['choice again'])
                            continue
                    except sr.UnknownValueError:
                        playsound(datai['mp3 tracks']['error message'])
                        playsound(datai['mp3 tracks']['choice again'])
                    except sr.RequestError as e:
                        print("Sphinx error; {0}".format(e))
            elif(text1==datai['wake']['stopphrase'] or 'stop' in text1):
                p = 0
                break;
            else:
                playsound(datai['mp3 tracks']['error message'])
                playsound(datai['mp3 tracks']['choice again'])



