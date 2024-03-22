def asal_carpanlari_bul(sayi):
    carpanlar = []
    bolen = 2

    while sayi > 1:
        while sayi % bolen == 0:
            carpanlar.append(bolen)
            sayi //= bolen
        bolen += 1

    return carpanlar

sayi = int(input("Bir sayı girin: "))

print(sayi, "sayısının asal çarpanları:", asal_carpanlari_bul(sayi))