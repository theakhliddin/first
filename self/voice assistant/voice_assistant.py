import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour())
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    assname = ("Jarvish 1 point o")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What I should I call you?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("##########".center(columns))
    print("Welcome Mr. ", uname.center(columns))
    print("##########".center(columns))

    speak("How can i help you? ")
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("REcognizing! ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice. Please try again.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login("your email id", 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Here you go to Youtube \n")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Here you go to Google \n")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow \n")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query or "play song" in query:
            speak("Here we go to music \n")
            music_dir = 'C:\\Users\\HP\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")
        elif 'open chrome' in query:
            codePath = r"C:\\Program Files\\Google\\Chrome\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Reciever email address"
                sendEmail(to, content)
                speak("Email has been snet!")
            except Exception as e:
                print(e)
                speak("Unable to send the email. Please try again.")
        elif 'send a mail' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                speak("Whom should I send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email. Please try again.")
        elif 'how are you' in query:
            speak("I am fine, thank you for asking!")
            speak("How are you?")
        elif 'fine' in query or "good" in query:
            speak("Its good to know that your fine")
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
        elif "change name" in query:
            speak("What would you like me to call you")
            assname = takeCommand()
            speak("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif "who made you" in query or "Who created you" in query:
            speak("I have been created by Aladin")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif "calculate" in query:
            app_id = "Wolframalpaha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        elif "who i am" in query:
            speak("If you talk then definitely your human")
        elif "why you came to world" in query:
            speak("Thanks for the developers")
        elif 'power point presentation' in query:
            speak("Opening power point presentation")
            power = r"C:\\Users\\HP\Documents\\PowerPoint Presentations"
            os.startfile(power)
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other sences")
        elif "who are you" in query:
            speak("I am a virtual assistant")
        elif "reason for you" in query:
            speak("I was created because professors neveer teach us proper things and projects")
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
        elif 'open telegram' in query:
            appli = r"C:\\Users\\akhli\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(appli)
        elif 'news' in query:
            try:
                jsonObj = urlopen(https://www.thetimes.com/)
                data = json.load(jsonObj)
                i = 1
                speak("here are some news")
                print("The Times" + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + item['description'])
                    i += 1
            except Exception as e:
                print(str(e))
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("shutting down the system")
            subprocess.call('shutdown / p / f')
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle bin Recycled")
        elif "don't listen" in query or "stop listening" in query:
            speak("how much time you want to stop me from listening")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif 'where is' in query:
            query = query.replace("Where is", "")
            location = query
            speak("User asked to locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        elif 'camera' in query or "take a photo" in query:
            ec.capture(0, "Jarvish camera", "img.jpg")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            speak("Hebernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            speak("Shuttign down")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "write a note" in query:
            speak("What should i write in the note")
            note = takeCommand()
            file = open("jarvis.txt", "w")
            speak("Sir, I am writing the note")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = "https://github.com/theakhliddin/first/tree/master/self"
            r = requests.get(url, stream = True)
            with open("self.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size=2391975), expected_size = (total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)
        elif 'aladin' in query:
            wishMe()
            speak("Aladin in your service")
            speak(assname)
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif "good morning" in query:
            speak("Good morning sir")
            speak("How are you today?")
            speak(assname)