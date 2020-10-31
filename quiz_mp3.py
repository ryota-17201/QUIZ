import csv
import re
from gtts import gTTS as gtts

with open('クイズ.csv', encoding="utf_8") as file:
    reader = csv.reader(file)
    word=[]
    for row in reader:
        A=row[0]
        B=row[1]
        A=re.sub("\(.+?\)", "",A)
        A=re.sub("\（.+?\）", "",A)
        B=re.sub("\(.+?\)", "",B)
        B=re.sub("\（.+?\）", "",B)
        word.append(A)
        word.append(B+"\n\n\n")

txt="    ".join(word)
mp3_txt=gtts(txt,lang='ja')
mp3_txt.save('クイズ.mp3')
