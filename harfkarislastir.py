## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

ilkMetin = "abaacdefgğg31443141df"
ikinciMetin = "kfdkfjdhdyqewt7312"

fark = ""

for harf in ilkMetin:
    if not harf in ikinciMetin:
        if not harf in fark:
            fark += harf
            
print(fark)
