# kullanıcıya bir parola belirletirken, belirlenecek parolanın 8 karakterden uzun, 3 karakterden kısa olmamasını sağlayalım.
## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

while True:
	sifre = input("Şifre gir bakalım: ")
	if 3 > len(sifre) and 8 > len(sifre):
		print("Bu iş böyle olmaz..")
	else:
		print("Şifre tanımlandı")
		break
