import speech_recognition as sr
import datetime
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

listner = sr.Recognizer()
motu = pyttsx3.init()
voices = motu.getProperty('voices')
motu.setProperty('voice', voices[1].id)
motu.say('Hi How can i help you.')
motu.runAndWait()

def talk(text):
    motu.say(text)
    motu.runAndWait()


def takeCommend():
    try:
        with sr.Microphone() as source:
            print('Listning...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'motu' in command:
                command = command.replace('motu', ' ')
    except:
        pass
    return command


def run_motu():
    command = takeCommend()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time )
    elif 'play' in command:
        song = command.replace('play', ' ')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        searchRep = command.replace('search', ' ')
        talk('searching' + searchRep)
        pywhatkit.search(searchRep)
    else:
        talk('i found somthing in google')
        pywhatkit.search(command)


while True:
    run_motu()



## #######################################################################################
#   Disable 
## #######################################################################################
