import time
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understood")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "hi sumit" in sptext().lower() :
        while True :
            data1 = sptext().lower()

            if "your name" in data1:
                name = " my name is sumit"
                speechtx(name)

            elif "how old are you" in data1:
                age = "i am two years old"
                speechtx(age)

            elif 'now time' in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(current_time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif 'play song' in data1:
                add = r'D:\d2\a'
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))

            elif "exit" in data1:
                speechtx("thank you")
                break

            time.sleep(5)
    else:
        print("thanks")
