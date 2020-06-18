from word2number import w2n #to convert strings in numerical digits
from Functions import *
import time

p = 1 #control variable to break out of main loop
while(True and p!=0): #as voice assistant keeps looking for the occcurance of the wake word
    time.sleep(5) #for it to find the file every 5 seconds
    result, datai = get_configInside() #loading file
    if result == 0: #if file isn't found
        playsound("file not found message", datai) #giving user the desired message
        continue
    else:
        number_of_floors = datai['wake']['number of floors'] #storing number of floors in the building
        while(True):
            audio1 = takeinput(datai) #to listen to the wake word
            try: #if it's able to convert wake word into string without error
                text1 = recognizeSphinx(audio1) #stored result in text1
                add_prediction(text1) #to add prediction in txt file
                k = 0 #control variable to break out of second while loop
                if(datai['wake']['keyphrase'] in text1): #if wake word is present in text1
                    playsound("floor choice message",datai) #tells user to choose the floor number
                    while(k == 0):
                        audio2 = takeinput(datai) #to take input of his choice
                        try: #if it's able to recognize choice without error
                            text2 = recognizeDS(audio2) #stored result in text2
                            add_prediction(text2) #to add prediction in txt file
                            try: #if it's able to convert string into numerical digit without error
                                n = w2n.word_to_num(text2) #storing result in n
                                if(n == datai['wake']['current floor']): #if the choice matches the floor on the which the lift is currently on
                                    playsound("same floor message",datai) #playing desired message
                                    playsound("choice again message", datai) #telling user to make the floor choice again
                                    continue
                                else:
                                    floorchange(n,datai) #else calling the pseudo function
                                    k = 1
                            except ValueError: #if error occurs in conversion to digit
                                playsound("choice again message", datai) #user is told to make the choice again
                                continue
                        except sr.UnknownValueError as e: #if deepspeech is unable to convert speech to text
                            logger(e) #add error in txt file
                            playsound("error message", datai) #playing error message
                            playsound("choice again message", datai) #telling user to make the floor choice again

                elif(datai['wake']['stopphrase'] in text1): #if user wants to stop execution of program
                    p = 0
                    break;
                else: #if text1 is neither wake word nor the stop phrase
                    playsound("choice again message", datai) #tells user to make choice again

            except sr.RequestError as e: #if conversion from speech doesn't take place
                logger(e) #adding error in txt file
                playsound("error message", datai) #playing error message
                playsound("choice again message", datai) #tells user to make the choice again
