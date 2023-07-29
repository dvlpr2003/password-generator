import password
from character import *


import random 
import os
string = ""

ps = password.Password(Capitals,Smaller,symbols)
ps.generate()

random.shuffle(ps.pas)
for _ in ps.pas:
    string += _
os.system("clear")
print(f'your password is : {string}')






