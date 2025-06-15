# this is audio library
# copy it and add your phrase in place of "i will speak this text " and it will repeat it in audio manner

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
