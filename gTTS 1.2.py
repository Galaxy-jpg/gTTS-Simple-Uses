from gtts import gTTS
import random

t = input("Message : ")

save = input("Save As : ")

print(save + ".mp3")

t2s = gTTS(text=t, lang='en') 
t2s.save(save + ".mp3")