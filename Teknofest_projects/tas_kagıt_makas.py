import random

puan = 0
hak = 0


def kazanan_bul(oyuncu, bilgisayar):
    global puan
    if oyuncu == bilgisayar:
        return "Berabere"
    elif (
        (oyuncu == "tas" and bilgisayar == "makas")
        or (oyuncu == "kagit" and bilgisayar == "tas")
        or (oyuncu == "makas" and bilgisayar == "kagit")
    ):
        puan += 3
        return f"Tebrikler bu eli kazandiz"
    else:
        return "Bilgisayar kazandi!"


while hak < 5:  # 5 hak dolunca döngü kırılıyor
    secenekler = ["tas", "kagit", "makas"]

    oyuncu_secim = (
        input("Taş, kagit, makas? (Çikiş için 'e' basin): ")
        .lower()
        .replace("ç", "c")
        .replace("ş", "s")
        .replace("ğ", "g")
        .replace("ı", "i")
    )
    if oyuncu_secim == "e":
        break

    # bu kullanıcı tas-kagit-makas dişinda seçim yaptığı zaman bilgisayaranın seçimini değiştirmemesini sağlar
    if oyuncu_secim in secenekler:
        hak += 1
        bilgisayar_secim = random.choice(secenekler)
        sonuc = kazanan_bul(
            oyuncu_secim, bilgisayar_secim
        )  # kazanan_bul fonksiyonunda return ettiği yazıyı"str" sonuca aktarır
        print(sonuc)

    else:
        print("Geçersiz bir seçim yaptiniz. Lütfen 'tas', 'kagit' veya 'makas' seçin.")

# max ve min puana özel
if puan == 15:
    print("MAX WİN")
elif puan == 0:
    print("TOO BAD LUCK")

print(f"Oyun bitti! Toplam puaniniz: {puan}")
