
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('api key goes here')
tts = TextToSpeechV1(authenticator=authenticator)

#Insert URL in place of 'API_URL' 
tts.set_service_url('api url goes here')

# recognize text using IBM Text to Speech from txt file
# save TTS as mp3 file
with open('stt-output.txt', 'r') as txt:
    text = txt.read()
    
with open('./tts-output.mp3', 'wb') as audio_file:
     res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content) #write the content to the audio file 

print("Process completed >> File saved")

