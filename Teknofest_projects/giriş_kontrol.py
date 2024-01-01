import re


# şifre kuralları
def validate_password(password):
    if not isinstance(password, str):
        return "Şifre bir dizedir."
    if not 5 <= len(password) <= 20:
        return "Şifre 5 ile 20 karakter arasinda olmalidir."
    if not re.search(r"[A-Z]", password):
        return "Şifre en az bir büyük harf içermelidir."
    if not re.search(r"[0-9]", password):
        return "Şifre en az bir sayi içermelidir."
    if re.search(r"::|&|\.|~|\s", password):
        return "Şifre iki nokta üst üste (:), bir ve işareti (&), bir nokta (.), yaklaşik işareti (~) veya bir boşluk içeremez."
    return None


# kullanıcı adı kuralları
def validate_username(username):
    if not isinstance(username, str):
        return "Şifre bir dizedir."
    if not 5 <= len(username) <= 20:
        return "Şifre 5 ile 20 karakter arasinda olmalidir."


while True:
    username = input("Kullanici adinizi giriniz: ")
    result1 = validate_username(username)
    if result1 is not None:
        print("Kullanici adi geçersiz. Sebep:", result1)
    else:
        print("Kullanici adi geçerli.")
        break


while True:
    password = input("Şifrenizi giriniz: ")
    result = validate_password(password)
    if result is not None:
        print("Şifre güvenli değil. Sebep:", result)
    else:
        print("Güvenli Şifre.")
        break  # Geçerli bir şifre girildiği için döngüden çık
