
import emoji
import numpy as np
import datetime
print (np.floor(0.6)) #اكبر عدد صحيح اقل او يساوي الرقم المعطي
print(np.ceil(0.6)) # اقل عدد صحيح اكبر او يساوي الرقم المعطي 
# ============================================================================= 
e=print(emoji.emojize(':rose:'*20))
# =============================================================================
open_file=open('student.txt','w')
open_file.write('''name\t age\t subjects\tdate of birth 
yasser\t 19\t est\t\t 2001
bader\t 20\t est\t\t 2000
Ahmad\t 18\t est\t\t 2002
Hassan\t 21\t est\t\t 1998
Omar\t 22\t est\t\t 1997
Mahmud\t 24\t est\t\t 1995
Mazen\t 30\t est\t\t 1990
Ossama\t 23\t est\t\t 1996
shabaan\t 25\t est\t\t 1994
jelal\t 26\t est\t\t 1993''')
open_file=open('student.txt','r')
print(open_file.read())
print('\n')
e=print(emoji.emojize(':rose:'*20))

now=datetime.datetime.now()
print(now)

