import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")   

    else:
        speak("Good Evening!")
        print("Good Evening!")  

    speak("I am friday Sir. Please tell me how may I help you")
    print("I am friday Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=7)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    query = query.lower()
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
def TaskExecution():
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening, sir")

        elif 'play songs on youtube' in query:
            speak("what song should i play")
            ytc = takeCommand().lower()

            kit.playonyt(f"{ytc}")
            speak("opening, sir")

        elif 'open google' in query:
            speak("what should i seaerch on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening, sir")

        elif 'open stackoverflow' in query:
            speak("opening, sir")
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak("opening, sir")
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            speak("opening, sir")
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'leave it' in query or 'leave now' in query:
            speak("ok sir")
            
        elif 'hello' in query or 'hey' in query:
            speak("hello sir, may i help you with something.")
        
        elif 'how are you' in query or 'hey how are you' in query:
            speak("i am fine sir, what about you.")

        elif 'also good' in query or 'fine' in query:
            speak("that's great to hear from you.")

        elif 'thankyou' in query or 'thanks' in query: 
            speak("it's my pleasure sir.")


        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime.")

            break

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            speak("thanks for using me sir, have a good day")
            sys.exit()
