import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  
engine.setProperty('rate', 170)  

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query
    except:
        speak("Sorry, I didn't understand that.")
        return "None"

if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        query = listen().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except:
                speak("Sorry, I couldn't find information on that.")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "date" in query:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif "shutdown" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 1")

        elif "stop" in query or "exit" in query or "quit" in query:
            speak("Goodbye! Have a great day.")
            break
