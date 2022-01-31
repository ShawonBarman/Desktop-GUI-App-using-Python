#first you need to install speech recognition by using pip install SpeechRecognition command
#second you need to install text to speech converter by using pip install pyttsx3 command
#third you need to install python audio by using pip install PyAudio command
#fourth you need to install pywhatkit by using pip install pywhatkit command
#fiveth you need to install wikipedia by using pip install wikipedia command
#sixth you need to install pyjokes by using pip install pyjokes command

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #thats mean i am creating a recognizer who would be able to recognize my voice. who understand the romantic desire inside my heart
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# engine.say("I am your alexa")
# engine.say("What can I do for you")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.lister(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()