import speech_recognition as sr

def main():
    # Create a Recognizer object
    aud = sr.Recognizer()
    
    # The path to your audio file
    sound = "aud1.WAV"
    
    # Use sr.AudioFile to read the audio file
    with sr.AudioFile(sound) as source:
        print("Listening to the audio...")
        audio_data = aud.record(source)  # Record the audio
    
    try:
        # Convert the speech to text using Google Cloud Speech-to-Text
        text = aud.recognize_google(audio_data)
        print("Converted audio is: " + text)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Cloud Speech service; {e}")

main()
