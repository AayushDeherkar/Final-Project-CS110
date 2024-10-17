import speech_recognition as sr

def main():
    aud = sr.Recognizer()
    sound = "aud1.WAV"
    
    #read the audio file
    with sr.AudioFile(sound) as source:
        print("Listening to the audio...")
        audio_data = aud.record(source) 
    
    try:
        # Convert the speech to text
        text = aud.recognize_google(audio_data)
        open 
        print("Converted audio is: " + text)
    except:
        print("file not found")
