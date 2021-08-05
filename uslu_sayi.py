## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net


altSayi = int(input("Sayıyı girin: "))
ustSayi = int(input("Üssünü girin: "))

uslusayiKey = 1

if altSayi == 0 and ustSayi == 0:
    print("Sonuç: Belirsiz")
elif altSayi != 0  and ustSayi == 0:
    print("Sonuç: 1")
else:
    for i in range(ustSayi):
        uslusayiKey = uslusayiKey * altSayi
print("Sonuç: ", uslusayiKey)
