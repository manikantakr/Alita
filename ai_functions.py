import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import time
import os
import cv2
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\rListening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=15)

    try:
        print("\rRecognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        return query.lower()

    except Exception as e:
        speak("Say that again please...")
        return "none"

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Master")
    elif 12 <= hour < 18:
        speak("Good Afternoon Master")
    else:
        speak("Good Evening Master")
    speak("I'm Alita....Your Personal AI Assistant...Please tell me How can I help you")

def play_youtube(query):
    pywhatkit.playonyt(query)

def search_google(query):
    speak(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={'+'.join(query.split())}"
    webbrowser.open(url, new=2)
    time.sleep(2)
    speak("Here are the search results from Google. I hope you find them useful.")

def send_whatsapp_message(query):
    speak(f"sending whatsapp message")
    phone_number = "+916361507269"
    pywhatkit.sendwhatmsg_instantly(phone_number, query)
