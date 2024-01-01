def fizbuzz():
    for i in range(1,151):                 # 1den 150 ye kadar ki sayıalrı tek tek alır 

        if i % 3 == 0  and i % 5 == 0:     # 3e ve 5e bölünme durumu kontrol edilir
            print("fizzbuzz")

        elif i % 3 ==0:                    # 3e bölünme durumu kontrol edilir
            print("fizz")

        elif i % 5 == 0:                   # 5e bölünme durumu kontrol edilir
            print("buzz")

        else:               
            print(i)
    

if __name__ == "__main__":
    fizbuzz()


