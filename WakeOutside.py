import time
from Functions import *


p = 1 #control variable to break out of main loop
while (True and p != 0): #as voice assistant keeps looking for the occcurance of the wake word
    time.sleep(5) #for it to find the file every 5 seconds
    result, datao = get_configOutside() #loading file
    if result == 0: #if file isn't found
        playsound("file_not_found_message", datao) #giving user the desired message
        continue
    else: #if file is found
        while (True):
            audio1 = take_input(datao)  # to listen to the wake word
            try: #if it's able to convert wake word into string without error
                text1 = recognize_Sphinx(audio1) #stored result in text1
                add_prediction(text1) #to add prediction in txt file
                k = 0 #control variable to break out of second while loop
                if (datao['wake']['keyphrase'] in text1): #if wake word is present in text1
                    playsound("upordown_message", datao) #tells user to choose whether he wants to go up or down
                    while (k == 0):
                        audio2 = take_input(datao) #to take input of his choice
                        try: #if it's able to recognize choice without error
                            text2 = recognize_Sphinx(audio2) #stored result in text2
                            add_prediction(text2) #to add prediction in txt file
                            if 'up' in text2 or text2 in datao['up']: #if choice is up
                                k = 1
                                liftgoesup(datao)  # pseudo function
                            elif 'down' in text2 or text2 in datao['down']:#if choice is down
                                k = 1
                                liftgoesdown(datao)  # pseudo function
                            else: #if it's neither up nor down
                                playsound("choice_again_message", datao) #tells user to make the choice again

                        except sr.UnknownValueError as e: #if sphinx is unable to recognize choice
                            logger(e) #add error in txt file
                            playsound("error_message", datao) #playing error message
                            playsound("choice_again_message", datao) #tells user to make the choice again


                elif (text1 == datao['wake']['stopphrase'] or 'stop' in text1): #if user wants to stop execution of program
                    p = 0
                    break; #breaking out of main loop
                else: #if the user speaks neither wake word nor stop phrase
                    playsound("choice_again_message", datao) #tells user to make choice again

            except sr.RequestError as e: #if conversion from speech doesn't take place
                logger(e) #adding error in txt file
                playsound("error_message", datao)  #playing error message
                playsound("choice_again_message", datao) #tells user to make the choice again
