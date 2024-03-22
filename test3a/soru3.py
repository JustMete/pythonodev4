#3.soru
sayi1=float(input("1.sayiyi giriniz"))
sayi2=float(input("2.sayiyi giriniz"))
sayi3=float(input("3.sayiyi giriniz"))

en_buyuk = sayi1

if sayi2 > en_buyuk:
    en_buyuk = sayi2

if sayi3 > en_buyuk:
    en_buyuk = sayi3
print("En büyük sayı:", en_buyuk)