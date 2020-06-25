import pyttsx3
import datetime
import speech_recognition as sr
import os
import pyautogui
import time
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('volume',0.5)
engine.setProperty('rate', 155)

def takeCommand():
    # It takes microphone input from the usr and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source2:
        print("Listening...")
        r.adjust_for_ambient_noise(source2, duration=1)
        r.pause_threshold = 2

        audio = r.listen(source2)
        print("running")

    try:
        print("recognising...")
        querry = r.recognize_google(audio, language='en-in')
        print(f"User said : {querry}\n")
    except Exception as e:
        print("Say that again please...")
        return 'None'
    return querry


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takescreenshot():
    screenshot=pyautogui.screenshot()
    folder="./screenshot/"

    #it creates folder if it already not exist

    if not os.path.exists(folder):
        os.makedirs(folder)
    while True:
        r = random.randint(1, 100)
        l=[0]
        for filename in os.listdir(folder):
            new_name = os.path.splitext(filename)[0]
            l.append(int(new_name))
        next=max(l)+1
        # save screenshot in series

        screenshot.save(f'{folder}{next}.png')
        break
    speak('screen captured')

if __name__ == '__main__':
    querry=takeCommand().lower()
    if 'screenshot' in querry:
        takescreenshot()


