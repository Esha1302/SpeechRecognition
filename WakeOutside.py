import time
from DeepSpeech.Functions import *
import playsound
p = 1
while(True and p!=0):
    time.sleep(5)
    result, datao = get_configOutside()
    if result == 0:
        print("File not found")
        continue
    else:
        while(True):
            audio1 = takeinput() #to listen to the wake word
            text1 =  recognize(audio1)
            print("you said:" + text1)
            k = 0
            if(text1 == datao['wake']['keyphrase'] or 'open' in text1):
                playsoundVoice(datao['mp3 tracks']['upordown message'])
                while(k == 0):
                    audio2 = takeinput()
                    text2 = recognize(audio2)
                    try:
                        print("Sphinx thinks you said " + text2)
                        if 'up' in text2 or text2 in datao['up']:
                            k = 1
                            liftgoesup()#pseudo function
                        elif 'down' in text2 or text2 in datao['down']:
                            k = 1
                            liftgoesdown()#pseudo function
                        else:
                            #print("Sphinx thinks you said " + text2)
                            playsound(datao['mp3 tracks']['choice again message'])

                    except sr.UnknownValueError:
                        playsound(datao['mp3 tracks']['error message'])

                    except sr.RequestError as e:
                        print("Sphinx error; {0}".format(e))
            elif(text1==datao['wake']['stopphrase'] or 'stop' in text1):
                p = 0
                break;
            else:
                playsoundVoice(datao['mp3 tracks']['error message'])
                playsoundVoice(datao['mp3 tracks']['choice again message'])





