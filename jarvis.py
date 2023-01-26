from winsound import PlaySound
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import vlc
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 165)

# Speak from text given in audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish whenever executed
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")

    print("I am Zira (Assistant of Arjun). How May i help You?")
    speak("I am Zira (Assistant of Arjun). How May i help You?")


def takeCommand():
    '''It takes microphone input from user and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("i'm listening...")
        speak("i'm listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("I didn't get that,  Say it again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hackmech007@gmail.com','1111arjun')
    server.sendmail('hackmech007@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=1)
                print("According to Wikipedia "+results)
                speak("According to wikipedia")
                speak(results)
            except Exception:
                print("Result Not Found")
                speak("Result Not Found")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\Arjun_Patel\\Desktop\\DeskTop\\Python Code\\Project Python\\Jarvis\\Music Demo"
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M:%S")
            timestr = time + datetime.datetime.now().strftime("%p")
            print(timestr)
            speak(timestr)

        elif 'open code' in query:
            codepath = "C:\\Users\\Arjun_Patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'send email' in query:
            try:
                speak("What is the message for Email? ?")
                content = takeCommand()
                to = "patelarjun164@gmail.com"
                sendEmail(to,content)
                print("Email has been sent!")
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                print("Fail to send email")
                speak("Fail to send email")

        elif 'rasiya' in query:
                audio = vlc.MediaPlayer("Project Python/Jarvis/Music Demo/Rasiya.mp3")
                audio.play()
                time.sleep(60)
                audio.stop()        

        if 'exit' in query:
            print("Quiting Jarvis..")
            speak("Quiting Jarvis..")
            break