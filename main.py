import time
import random

print ("Built Like Generator - v0.9")
time.sleep(1)

while True:
  input ("Press ENTER ")
  builtl = ['a chicken wing', 'an abandoned arbys', 'a javascript variable', 'a McDonalds chicken nugget', 'a string bean', 'the first youtube video', 'carter ellis', 'a popeyes biscuit', '']
  randb = random.choice(builtl)
  print ("Your built like " + randb)