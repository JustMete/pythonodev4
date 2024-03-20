maas=float(input("Mevcut maaşı girin :"))
zam_orani=float(input("Zam  oranını yüzde olarak  giriniz :"))

yeni_maas=((maas/100)*zam_orani)+maas
print(yeni_maas)