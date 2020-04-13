from gtts import gTTS
import random

t = input("Message : ")

num = random.random()
number = num * 10

n = "TTS" + str(number) + ".mp3"

print(n)

t2s = gTTS(text=t, lang='en') 
t2s.save(n)