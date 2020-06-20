# SpeechRecognition
<h1>What is speech recognition?</h1>

•	Speech recognition is identifying the speech inputted by the user, understanding the syllables used, recognizing the patterns, checking the pattern with the various combinations possible, and printing the most matched one. 

•	The first component of speech recognition is speech. Speech must be converted from physical sound to an electrical signal with a microphone, and then to digital data with an analog-to-digital converter. 

<h3>Now, let’s search for the packages that can be used for speech to text conversion, and separate out the ones which work offline on a local system. </h3>

Online:
1.	Google Speech Recognition
2.	Google Cloud Speech API
3.	Wit.ai
4.	Microsoft Bing Voice Recognition
5.	Houndify API
6.	IBM Speech to Text

Offline:
1. CMU Sphinx & SpeechRecognition
2. Snowboy Hotward Detection
3. Porcupine

Out of the three offline packages available, CMU Sphinx, also called Pocketsphinx, was the only one available as an open source and could be run on all three platforms – **Windows, Linux and Mac,** hence I chose to proceed with working on my project using this package. 

<h3> Requirements: </h3>
 Before you get started, you’ll need libraries, APIs to build your code. You’ve already chosen your API, but how will you capture input from the user and link it into your code, well that’s where **PyAudio and Speech Recognition** libraries come to the rescue!
 
<h3> Installations: </h3>

<h5>Step 1: </h5>

Download pycharmIDE from the net:

a) For windows, just install the .exe file
b) For linux, download the tar file --> extract the tar --> open pycharm folder which will be in your downloads section --> open bin --> then open it in terminal --> and type “./pycharm.sh”

<h5>Step 2: </h5> 

Create a new project, and it’s better if you choose Python 3.6 as your interpreter as PyAudio is not compatible with higher python versions. Python 3.6 is downloadable from the official python site. For windows, just choose the .exe file while choosing an interpreter in pycharm. 

For linux, the process of installation is easier; the following commands are to be typed on the terminal: 
-	sudo apt-apt-repository ppa:deadsnakes/ppa
-	sudo apt update
-	sudo apt install python3.6

<h5>Step 3: </h5>

Let’s get started with installing libraries now, the easiest one to install is SpeechRecognition. Go to settings --> Choose Project name --> Project Interpreter --> Click on ‘+’ sign on the left --> In the search box, type in SpeechRecognition, and in the drop down choose it --> Click on install. Alternatively, just type this command on the terminal: _pip install speechrecognition_

<h5>Step 4: </h5>

To install PyAudio: 

a) In windows, you first have to install Microsoft Visual Studio and its C++ build tools --> install gcc like you did speechrecognition --> install pyaudio either by step 3 or you can write on the terminal of pycharm – pip install pyaudio

b) For linux, c++ tools are already built in, so the following steps are to be taken on the terminal window of pycharm:
-	sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
-	sudo apt-get install python3-pyaudio
-	sudo apt-get install python3.6-dev
-	sudo apt-get install gcc
-	pip3 install pyaudio

<h5>Step 5: </h5> 

To install pocketsphinx:

a) In windows, first install the swig package --> install pocketsphinx

b) In linux: 
-	sudo apt-get install swig
-	sudo apt-get update
-	sudo apt-get install libpulse-dev
-	pip3 install pocketsphinx

 <h5> Step 6: </h5>
 
 To install deepspeech: (isn't compatible with windows)
 - Use the following commands to install deep speech models :     
 
   curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.pbmm     
   
   curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.7.3/deepspeech-0.7.3-models.scorer
   
 - pip3 install deepspeech
