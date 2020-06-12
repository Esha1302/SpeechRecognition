import time
from DeepSpeech.Functions import *


p = 1
while (True and p != 0):
    time.sleep(5)
    result, datao = get_configOutside()
    if result == 0:
        print("File not found")
        str = playsound("file not found message", datao)
        continue
    else:
        while (True):
            audio1 = takeinput(datao)  # to listen to the wake word
            try:
                text1 = recognizeSphinx(audio1)
                print(text1)
                add_prediction(text1)
                k = 0
                if (text1 == datao['wake']['keyphrase'] or 'open' in text1):
                    playsound("upordown message", datao)
                    while (k == 0):
                        audio2 = takeinput(datao)
                        try:
                            text2 = recognizeSphinx(audio2)
                            add_prediction(text2)
                            if 'up' in text2 or text2 in datao['up']:
                                k = 1
                                liftgoesup(datao)  # pseudo function
                            elif 'down' in text2 or text2 in datao['down']:
                                k = 1
                                liftgoesdown(datao)  # pseudo function
                            else:
                                playsound("choice again messgae", datao)

                        except sr.UnknownValueError:
                            playsound("error message", datao)

                elif (text1 == datao['wake']['stopphrase'] or 'stop' in text1):
                    p = 0
                    break;

            except:
                playsound("error message", datao)
                playsound("choice again message", datao)
