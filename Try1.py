
from deepspeech import Model
import numpy as np
import speech_recognition as sr

def recognizer():
    sample_rate = 16000
    beam_width = 500

    model_name = "Models/deepspeech-0.7.3-models.pbmm"

    if __name__ == '__main__':
        ds = Model(model_name)

        r = sr.Recognizer()

        with sr.Microphone(sample_rate=sample_rate) as source:
            print("Say Something")
            audio = r.listen(source)
            fs = audio.sample_rate
            #print(fs)
        audio = np.frombuffer(audio.frame_data, np.int16)
            #print(audio.)

    print(ds.stt(audio))
    #print("str", str)

recognizer()