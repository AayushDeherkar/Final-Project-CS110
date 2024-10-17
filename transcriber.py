#Author: Aayush Deherkar, rashi Jain
#Email: adeherkar@umass.edu, rashijain@umass.edu
#Spire ID:34759120 34559888
import speech_recognition as sr

def main(audfile):
    aud = sr.Recognizer()
    sound = audfile
    
    #read the audio file
    with sr.AudioFile(sound) as source:
        print("Listening to the audio...")
        audio_data = aud.record(source)  # Record the audio
    
    try:
        #Speech to text
        text = aud.recognize_google(audio_data)
        print("Converted audio is: " + text)
    except:
        print("file not found")


main("aud1.WAV")
