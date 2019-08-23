import os
import pyttsx3
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    if hour>=0 and hour<12:
        speak("Good Morning! Have a Good Day Ahead.")
    elif hour>12 and hour<18: 
        speak("Good Afternoon! Hope you are having a Good Day.")
    elif hour>=18 and hour<0:
        speak(" Good Evening! Hope you had a Good Day.")

    speak("Hello Sir! I am Jarvis, How may I help you?")

def takeCommand():
    # Takes mic input from the user and returns as a string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # durarion of listening 
        audio = r.listen(source)    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"    
    return query

if __name__ =="__main__":
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        #query = 'wikipedia Where is Kerala?'
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            music_dir = "F:\\Abhi's\\Phone Data\\WhatsApp Audio"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\AbhishekEmmanuel\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        

            #photoshopPath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"



