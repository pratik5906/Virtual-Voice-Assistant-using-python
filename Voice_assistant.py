import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date
engine=pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [1].id)
recognizer=sr.Recognizer()
def engine_talk(text):
 engine.say(text)
 engine.runAndWait()
def run_alexa():
 with sr.Microphone() as source:
  recognizer.adjust_for_ambient_noise(source,duration=1)
  print('\n')
  print("Start Speaking!!")
  engine_talk("Start Speaking")
  engine_talk('listening.. ')
  recordedaudio=recognizer.listen(source)

 try:
  command=recognizer.recognize_google(recordedaudio,language='en-in')
  command = command.lower()

  if 'alexa' in command :
       command = command.replace('alexa', '')
       print('you said'+command)
  else :

     print('you said : '+command)
  if 'hello' in command :
     print('hello how can i helpp you ??')
     engine_talk('hello, how can i help you ??')
  elif 'who are you' in command :
     print('I am mini alexa a k a your virtual assistant master.how can i help you ??')
     engine_talk('I am mini alexa a k a your virtual assistant master. how can i help you ??')
  elif 'What can you do' in command :
     print('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
           open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??''')
     engine_talk('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
           open different websites like insta gram, youtube,gmail, git hub, stack overflow and searches on google. How may i help you ??''')

  elif 'play' in command:
      song = command.replace('play', '')
      print('Playing' +song)
      engine_talk('Playing' +song)
      pywhatkit.playonyt(song)
  elif 'date and time' in command :
      today = date.today()
      time = datetime.datetime.now().strftime('%I:%M %p')
# Textual month, day and year
      d2 = today.strftime("%B %d, %Y")
      print("Today's Date is ", d2, 'Current time is', time)
      engine_talk('Today is : '+ d2)
      engine_talk('and current time is '+ time)
  elif 'time and date' in command :
      today = date.today()
      time = datetime.datetime.now().strftime('%I:%M %p')
# Textual month, day and year
      d2 = today.strftime("%B %d, %Y")
      print("Today's Date is ", d2, 'Current time is', time)
      engine_talk( 'Current time is '+ time)
      engine_talk('and Today is : '+ d2)

  elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      print('The current time is' +time)
      engine_talk('The current time is')
      engine_talk(time)
  elif 'date' in command:
      today = date.today()
      print("Today's date:", today)
# Textual month, day and year
      d2 = today.strftime("%B %d, %Y")
      print("Today's Date is ", d2)
      engine_talk('The todays date is')
      engine_talk(d2)
  elif 'tell me about' in command:
      name = command.replace('tell me about' , '')
      info = wikipedia.summary(name, 1)
      print(info)
      engine_talk(info)
  elif 'wikipedia' in command:
      name = command.replace('wikipedia' , '')
      info = wikipedia.summary(name, 1)
      print(info)
      engine_talk(info)
  elif 'what is' in command:
      name = command.replace('what is ' , '')
      info = wikipedia.summary(name, 1)
      print(info)
      engine_talk(info)
  elif 'who is ' in command:
      name = command.replace('who is' , '')
      info = wikipedia.summary(name, 1)
      print(info)
      engine_talk(info)
  elif 'what is ' in command :
      search = 'https://www.google.com/search?q='+command
      print(' Here is what i found on the internet..')
      engine_talk('searching... Here is what i found on the internet..')
      webbrowser.open(search)
  elif 'joke' in command:
      _joke = pyjokes.get_joke()
      print(_joke)
      engine_talk(_joke)
  elif 'search' in command :
       search = 'https://www.google.com/search?q='+command
       engine_talk('searching... ')
       webbrowser.open(search)
  elif "my location" in command:
       url = "https://www.google.com/maps/search/Where+am+I+?/"
       webbrowser.get().open(url)
       engine_talk("You must be somewhere near here, as per Google maps")
  elif 'open google' in command :
       print('opening google ...')
       engine_talk('opening google..')
       webbrowser.open_new('https://www.google.co.in/')
  elif 'gmail' in command :
       print('opening gmail ...')
       engine_talk('opening gmail..')
       webbrowser.open_new('https://mail.google.com/')
  elif 'open youtube' in command :
        print('opening you tube ...')
        engine_talk('opening you tube..')
        webbrowser.open_new('https://www.youtube.com/')
  elif 'open instagram' in command :
        print('opening instagram ...')
        engine_talk('opening insta gram...')
        webbrowser.open_new('https://www.instagram.com/')
  elif 'open stack overflow' in command :
        print('opening stackoverflow ...')
        engine_talk('opening stack overflow...')
        webbrowser.open_new('https://stackoverflow.com/')
  elif "who made you" in command or "who created you" in command:
      print("I have been created by Mister Pratik.")
      engine_talk("I have been created by Mister Pratik.")
  elif 'open github' in command :
        print('opening git hub ...')
        engine_talk('opening git hub...')
        webbrowser.open_new('https://github.com/')
  elif 'bye' in command:
        print('good bye, have a nice day !!')
        engine_talk('good bye, have a nice day !!')
        sys.exit("Exit")
  elif 'thank you' in command :
        print("your welcome")
        engine_talk('your welcome')
  elif 'stop' in command:
        print('good bye, have a nice day !!')
        engine_talk('good bye, have a nice day !!')
        sys.exit()
  elif 'tata' in command:
        print('good bye, have a nice day !!')
        engine_talk('good bye, have a nice day !!')
        sys.exit()
  else:
        print(' Here is what i found on the internet..')
        engine_talk('Here is what i found on the internet..')
        search = 'https://www.google.com/search?q='+command
        webbrowser.open(search)
 except Exception as ex:
     print("Unable to Recognize your voice.")
     engine_talk("Unable to Recognize your voice.")


print('Clearing background noise...Please wait')
engine_talk('Clearing background noise...Please wait')
print('\n')
print("hello, i am mini alexa how can i help you ??")
engine_talk ("hello i am mini alexa how can i help you ")

while True:
 run_alexa()