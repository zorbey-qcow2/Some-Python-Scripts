## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

print("""
Yapmak istediğiniz işlemi girin:
(1) Toplama
(2) Çıkartma
(3) Bölme
(4) Çarpma
(5) Kalan
(6) Üssü
(7) Karekök
""")

islem = int(input("> "))

if islem == 1 :
	print("Toplanacak sayıları sırasıyla girin")
	topLa = input("> ")
	topLa2 = input("> ")
	if bool(topLa or topLa2) == False:
		print("Boş bırakma piç")
	if bool(topLa) == True:
		print("Sonuç", ":", int(topLa) + int(topLa2))
else :
	print("Değer girilmedi")
