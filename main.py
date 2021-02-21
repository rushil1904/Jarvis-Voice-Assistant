import speech_recognition as sr
from os.path import commonpath
import pyttsx3
import pywhatkit
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
        except Exception as e:
            print('I am sorry. I cannot hear you')
            return 'None'


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    else:
        talk('Please say the command again.')

while True:
    run_jarvis()
