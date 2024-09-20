import string
import time

text = "hello lybi odnohrypniki"
temp = ""

for ch in text:
    if ch in string.printable:
       if ch == '':
           time.sleep(0.02)
           print (temp+ch)
           temp+= ch
           break
       else:
           time.sleep(0.02)
           print(temp + ch)
           temp += ch