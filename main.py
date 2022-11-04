import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening ........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'helen' in command:
                command = command.replace('helen', '')
                print(command)

    except:
        pass
    return command


def run_helen():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('the current time is ' + time)
        talk('the current time is ' + time)
    elif 'the heck is' in command:
        person = command.replace('the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('i have an fever')
        print('i have an fever')
    elif 'are you single' in command:
        talk('i am in a relationship with samsung')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        print('say that command again')
        talk('say that command again')


while True:
    run_helen()
