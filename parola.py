## Github: https://github.com/zorbey-qcow2
## Web: https://zorbey.dogangunes.net

for i in range(3):
    parola = input("Parola Belirleyin: ")
    if not parola:
        print("Parola boş bırakılmaz manyak mısın sen")
        del parola
    elif len(parola) < 5 or len(parola) > 10:
        print("Parola 5 karakterden küçük, 10 karakterden büyük olamaz")
        del parola
    elif not len(parola) < 5 or len(parola) > 10:
        print("Parola tanımlandı tatlım")
        break
    if i == 2:
        print("\n3 kere denedin olmadı, yarım saat sonra tekrar gel")
        if 'parola' in globals():
            del parola
        
if 'parola' in globals():
    print("\nParola:" , parola)
