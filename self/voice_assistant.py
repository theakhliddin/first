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