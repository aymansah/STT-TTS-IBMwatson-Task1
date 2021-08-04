# NOTE: install SpeachRecognition

import speech_recognition as sr

# obtain audio from the microphone (NOTE install pyaudio using pipwin for windows)
recognize = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = recognize.listen(source, timeout=None, phrase_time_limit=None, snowboy_configuration=None)

# IBM Speech to Text

IBM_USERNAME = "apikey"  
IBM_PASSWORD = "INSERT UR API KEY HERE"
result= recognize.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)

try:
    print("IBM Speech to Text captured: " + result)
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

# save (write) captured audio to a txt file
with open('stt-output.txt',mode ='w') as file: 
   file.write(result) 
print("txt file saved!")
