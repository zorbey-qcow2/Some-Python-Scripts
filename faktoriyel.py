## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

fuckAl = int(input("Fucktorielini almak istediğiniz rakamı girin: "))
fuckKey = 1

if fuckAl == 0:
    print("Sonuç: 1")
elif fuckAl < 0:
    print("Bunun sonucu yok")
else:
    for i in range(1,fuckAl + 1):
        fuckKey = fuckKey*i

print(fuckKey)

