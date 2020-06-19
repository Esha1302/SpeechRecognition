from word2number import w2n #to convert strings in numerical digits
from Functions import *
import time

p = 1 #control variable to break out of main loop
while(True and p!=0): #as voice assistant keeps looking for the occcurance of the wake word
    time.sleep(5) #for it to find the file every 5 seconds
    result, datai = get_configInside() #loading file
    if result == 0: #if file isn't found
        playsound("file_not_found_message", datai) #giving user the desired message
        continue
    else:
        number_of_floors = datai['wake']['number_of_floors'] #storing number of floors in the building
        while(True):
            audio1 = take_input(datai) #to listen to the wake word
            try: #if it's able to convert wake word into string without error
                text1 = recognize_Sphinx(audio1) #stored result in text1
                add_prediction(text1) #to add prediction in txt file
                k = 0 #control variable to break out of second while loop
                if(datai['wake']['keyphrase'] in text1): #if wake word is present in text1
                    playsound("floor_choice_message",datai) #tells user to choose the floor number
                    while(k == 0):
                        audio2 = take_input(datai) #to take input of his choice
                        try: #if it's able to recognize choice without error
                            text2 = recognize_DS(audio2, datai) #stored result in text2
                            add_prediction(text2) #to add prediction in txt file
                            text2_split = text2.split(" ") #take the number following floor
                            try: #if it's able to convert string into numerical digit without error
                                n = w2n.word_to_num(text2_split[1]) #taking second element of array that contains number and changing it into digit
                                if(n == datai['wake']['current_floor']): #if the choice matches the floor on the which the lift is currently on
                                    playsound("same_floor_message",datai) #playing desired message
                                    playsound("choice_again_message", datai) #telling user to make the floor choice again
                                    continue
                                else:
                                    floor_change(n,datai) #else calling the pseudo function
                                    k = 1
                            except ValueError: #if error occurs in conversion to digit
                                playsound("choice_again_message", datai) #user is told to make the choice again
                                continue
                        except sr.UnknownValueError as e: #if deepspeech is unable to convert speech to text
                            logger(e) #add error in txt file
                            playsound("error_message", datai) #playing error message
                            playsound("choice_again_message", datai) #telling user to make the floor choice again

                elif(datai['wake']['stopphrase'] in text1): #if user wants to stop execution of program
                    p = 0
                    break;
                else: #if text1 is neither wake word nor the stop phrase
                    playsound("choice_again_message", datai) #tells user to make choice again

            except sr.RequestError as e: #if conversion from speech doesn't take place
                logger(e) #adding error in txt file
                playsound("error_message", datai) #playing error message
                playsound("choice_again_message", datai) #tells user to make the choice again
