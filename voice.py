from gtts import gTTS # pip install gTTS
from playsound import playsound # pip install playsound
i = input('ENTRE YOUR NAME :')
x = 'hey '+i+ 'welcome to my tool, i hope you like it'
la = 'en'
g = gTTS(text=x,lang=la,slow=False)
out = g.save('voice.mp3')
playsound('voice.mp3')
