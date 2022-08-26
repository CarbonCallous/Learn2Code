import speech_recognition as sr #pip install SpeechRecognition
import webbrowser
import pyttsx3  #pip install pyttsx3
import pyjokes  #pip install pyjokes 
                #pip install beautifulsoup4
from ecapture import ecapture as ec   #pip install ecapture


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
            
            speak("How can I help you today?")

            r = sr.Recognizer()
            with sr.Microphone() as source:

                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio,language='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                print(e)
                print("Unable to Recognize your voice.")
                return "None"

            return query

if __name__ == '__main__':
    while True:
        
        query = takeCommand().lower()

        if 'weather' in query:
            speak("Opening local weather\n")
            webbrowser.open("weather.com")
            

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'picture' in query:
            speak("Say cheese!)")
            ec.capture(0,"false", "1.png")



        elif 'exit' in query:
            speak('Goodbye)')
            exit()


