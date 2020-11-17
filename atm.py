import time
import os
bky=0
a=int(input("Yapmak istediğini işlemi aşağıdan seçiniz.\n[1]Bakiye Sorma\n[2]Para Çekme\n[3]Para Yatırma\n\n[4]Çıkış\n"))


while True:

    if a == 1:
        print("\n\nBakiyeniz {} TL'dir.\n-----------------------\n".format(bky))
        os.system('cls')
        a=int(input("TARIK BANKASI'na hoş geldiniz, yapmak istediğini işlemi aşağıdan seçiniz.\n[1]Bakiye Sorma\n[2]Para Çekme\n[3]Para Yatırma\n\n[q]Çıkış\n"))
        
        
    

    if a == 2:
        b=int(input("Kaç lira çekmek istersiniz"))
        if b > bky:
            print("\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print("Yetersiz bakiye\n---------------------------\n")
            os.system('cls')
            a=int(input("\nYapmak istediğini işlemi aşağıdan seçiniz.\n[1]Bakiye Sorma\n[2]Para Çekme\n[3]Para Yatırma\n\n[q]Çıkış\n"))
            

        else:
            bky=bky - b
            print("\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\")
            print("Kalan bakiye {} TL".format(bky))
            print("----------------------------------")
            os.system('cls')
            a=int(input("\n\nYapmak istediğini işlemi aşağıdan seçiniz.\n[1]Bakiye Sorma\n[2]Para Çekme\n[3]Para Yatırma\n\n[q]Çıkış\n"))

    if a == 3:
        c=int(input("Kaç TL yatırmak istersiniz"))
        bky=bky + c
        print("\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print("Bakiye {} TL'dir".format(bky))
        print("----------------------------------")
        os.system('cls')
        a=int(input("\n\nYapmak istediğini işlemi aşağıdan seçiniz.\n[1]Bakiye Sorma\n[2]Para Çekme\n[3]Para Yatırma\n\n[q]Çıkış\n"))

    if a ==  4:
       print("Çıkış yapılıyor...")
       print("TARIK BANKASI'NI TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ, yine Bekleriz")
       time.sleep(2)
       quit
       
