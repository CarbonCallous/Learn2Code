import speech_recognition as sr #pip install SpeechRecognition
import webbrowser
import datetime
import calendar
import pyttsx3  #pip install pyttsx3
import pyjokes  #pip install pyjokes 
                #pip install beautifulsoup4
from ecapture import ecapture as ec   #pip install ecapture

#setting up the voice engine for text to speak
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
rate = engine.getProperty('rate') #slowing down the rate of speech for better recognition
engine.setProperty('rate', rate-35)

def speak(audio):#setting machine to listen for user to speak
    engine.say(audio)
    engine.runAndWait()

def getDate(): #setting date and time
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ', ' + monthNames[monthNum -1] + ' the ' + ordinalNumbers[dayNum -1]

def takeCommand(): #take command to start the assistant
            
            speak("How can I help you today?") #initial question

            r = sr.Recognizer()
            with sr.Microphone() as source: #initialize and start microphone

                print("Listening...")
                r.pause_threshold = 1   
                audio = r.listen(source)    #set machine to listen to microphone

            try:
                print("Recognizing...")
                query = r.recognize_google(audio,language='en-in')  #recognizing user voice data
                print(f"User said: {query}\n")

            

            except Exception as e:
                print(e)
                print("Unable to Recognize your voice.") #exception if the voice cannot be understood
                return "None"

            return query

if __name__ == '__main__':
    while True:
        
        query = takeCommand().lower() #calls the prompt for user input

        if 'weather' in query: #weather
            speak("What city?")
            print("City Name: ")
            city = takeCommand()
             = http://platform.bing.com/geo/spatial/v1/public/Geodata?
            #needs geocaching (Lat/long) to work with free weather api

            api_key = " "
            baseURL = "https://api.weather.gov/points/"
            compURL = baseURL + "latLong"
            response = requests.get(compURL)
            x = response.json()

            if x["code"] != "404":
                y = x["main"]
                current_temp = y["temp"]
                current_press = y["press"]
                current_humid = y["humid"]
                z = x["weather"]
                weatherDesc = z[0]["description"]
                print(" Temperature in ")

            else:
                speak("Sorry, cannot find your city")


            

        elif 'music' in query:
            speak("Opening Spotify")
            webbrowser.open("www.spotify.com")

        elif 'created' in query:
            speak("To quietly observe and gather information for Skynet")

        elif 'google' in query:
            speak("opening Google")
            webbrowser.open("www.google.com")
            

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'picture' in query:
            speak("Say cheese!)")
            ec.capture(0,"false", "image.png")

        elif 'date' in query:
            get_date = getDate()
            speak(get_date)
            

        elif 'exit' in query or "dont need" in query or "done" in query:
            speak('Goodbye)')
            exit()

        else:
            speak('I did not understand')



