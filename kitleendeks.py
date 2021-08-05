# Vücut kitle indeksinin hesaplanması ve yorumlanması
# Formül : Vücut Kitle İndeksi (VKİ) = Vücut Ağırlığı (kg.) / Boy uzunluğunun karesi (m2.) 
# pip3 install inquirer
## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

import inquirer
import os.path
from os import path
from datetime import datetime

zaman = datetime.now()
su_an = zaman.strftime("%d/%m/%Y %H:%M:%S")
you = ("> ")
print("Şu an:", su_an)
print("Merhaba. Sana nasıl hitap edebilirim?") 
nickname = input(you)

print(f"\n{nickname} birazdan Vücut Ağıtlığı(kg) / Boy uzunluğunun karesi(m2) ile Vücut kitle indeksini hesaplayacağız\n")

print("Bunun için senden bazı bilgiler almam gerekiyor\n")

print("Kilon kaç? (sadece rakam)")

kilo = int(input(you)) 

print("Boyun kaç? (m olarak sadece rakam = Örnek; 1.75)")

boy = float(input(you))

print(f"\nHmm.. Yanlış anlamadıysam kilon {kilo} kg, boyun {boy} metre. Şimdi hesaplama yapıyorum")

vki = kilo / (boy * boy) 

yuvarla_vki = round(vki)

print("Vücut kitle endeksin: ", vki, "Hadi bunu yuvarlayalım madem:", yuvarla_vki)

def vkiliste(dusukk, normalk, fazlak, obez):
	print("\nKabul edilen standartlara göre;")
	print(f"\t* {dusukk} ve altı; Düşük kilolu")
	print(f"\t* {normalk}; Normal kilolu")
	print(f"\t* {fazlak}; Fazla kilolu")
	print(f"\t* {obez} ve üstü; Obez")

vkiliste(18.5, "18.5 - 24.9", "24.9 - 29.9", 30)

if(vki <= 18.5):
	print("\nRüzgar çıksa uçacaksın, yemek ye")

elif(18.5 <= vki <= 24.9):
	print("\nAferimm baya sağlıklısın")

elif(24.9 <= vki <= 29.9):
	print("\nAz ye artik, obez olacaksin.")

elif(vki >= 30):
	print("\nVah vahh obez olmuşsun")

bos =("\n")
print(bos)

questions = [
	inquirer.List('yedek_sor',
		message=f"Sonuçların yedeğini ister misin {nickname}?",
		choices=['Evet', 'Hayır'],
	),
]

cevap = inquirer.prompt(questions)
yedek_cevap = cevap['yedek_sor']


if(yedek_cevap == "Evet"):
	print("Yedek dosyasinin ismi ne olsun?")
	yedekdosya = input(f"Örneğin: yedek.txt - {you}")
#	print(path.exists(yedekdosya))
	if(path.exists(yedekdosya) == False):
		yedekal = open(yedekdosya, 'w+')
		yedekal.write(f"Sevgili: {nickname} \n{su_an} itibari ile \n{vki} VKİ'ye sahipsin.")
		yedekal.close()
	else:
		yedekal = open(yedekdosya, 'w')
		yedekal.write(f"Sevgili: {nickname} \n{su_an} itibari ile \n{vki} VKİ'ye sahipsin")
		yedekal.close()
else:
	print("Sen nasıl istersen. O zaman byy")
