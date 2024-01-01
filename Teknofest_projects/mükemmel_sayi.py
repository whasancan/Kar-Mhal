def bolenleri_bul(sayi):
    bolen_listesi = []  # sonuçların tutulacağı liste
    for i in range(1, sayi + 1):  # 1 den girilen sayiya kadar
        if sayi % i == 0:  # kalan yoksa alt tarafata listeye ekle çaloışır
            bolen_listesi.append(i)
    return bolen_listesi


while True:
    sayi = input("Bölenlerini bulmak istediğiniz sayiyi giriniz (Çikmak için 'ç'):")
    if sayi.lower() == "ç":
        print("Programdan Çikiliyor...")
        break
    else:
        sayi = int(sayi)
        bolenler = bolenleri_bul(sayi)
        print(bolenler)
        kosul = (
            sum(bolenler) - sayi
        )  # sayının kendisi hariç pozitif bölenlerinin toplamınının değeri
        if kosul == sayi:
            print(f"{sayi} mükemmel sayidir.")
        else:
            print(f"{sayi} mükemmel sayi değil.")
