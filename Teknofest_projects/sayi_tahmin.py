import random

# 3 taene zorluk seviyesi vardır. 
def zorluk_seviye(zorluk):
    if zorluk == "1":
        return random.randint(1, 10) 
    elif zorluk == "2":
        return random.randint(1, 100)
    elif zorluk == "3":
        return random.randint(1, 1000)
    else:
        print("Geçersiz zorluk seviyesi!")

# kullanıcının girdiği sayıyı kontrol eden fonksiyon
def tahmin_kontrol(zorluk_seviyesi):
    sayi = zorluk_seviye(zorluk_seviyesi)
    while True:
        tahmin = int(input("Tahmininiz: "))
        if tahmin == sayi:
            print("Tebrikler! Doğru tahmin ettiniz.")
            break
        elif tahmin < sayi:
            print("Daha büyük bir sayı tahmin edin.")
        else:
            print("Daha küçük bir sayı tahmin edin.")



zorluk = input("Zorluk seviyesini seçiniz (1-2-3): ")
tahmin_kontrol(zorluk)
