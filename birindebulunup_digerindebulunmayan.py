# AMAÇ : ilk_metin adlı değişken içinde bulunan, ama ikinci_metin adlı değişken içinde bulunmayan öğeleri ayıklamak
## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net


ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for harf in ilk_metin:
    if not harf in ikinci_metin:
        print(harf)

