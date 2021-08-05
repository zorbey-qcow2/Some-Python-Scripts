## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

isim1 = open('isimler1.txt', 'r')
isim2 = open('isimler2.txt', 'r')
isimFark = open('isimfark.txt', 'w')

fark = ""

for isim in isim1:
    if not isim in isim2 and not isim in fark:
        fark += isim
        

isimFark.write(fark)

isim1.close()
isim2.close()
isimFark.close()
