#!/usr/bin/env python
# coding: utf-8

# In[1]:
import time
from random import randint
import sys
from pygame import mixer

# In[2]:
mixer.init()
mixer.music.load("Feliz_cumple_rola.mp3")
mixer.music.play()

# In[3]:

for i in range(1,85):
    print('')

space = ''

for i in range(1,1000):
    count = randint(1, 100)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + "😊Gracias por tu amistad")
    elif(i%9 == 0):
        print(space + "🚀Éxitos en tus proyectos")
    elif(i%5==0):
        print(space +"🎉Feliz cumple, bro")
    elif(i%8==0):
        print(space + "🥳🥳🥳")
    elif(i%7==0):
        print(space + "🤩Eres una gran persona")
    elif(i%6==0):
        print(space + "😎Los mejores deseos en tu camino!")
    else:
        print(space + "🎇🎈")

    space = ''
    time.sleep(0.3)