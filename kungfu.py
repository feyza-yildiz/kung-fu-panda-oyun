#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:18:35 2024

@author: feyzayildiz
"""
import random #random kütüphanesini yükleme

from PIL import Image

# Görselin adını (yolu ile birlikte) belirtin
image_path = "gorsel.jpg"  # Görsel dosyanızın adı burada belirtilmeli

# Görseli yükleyin
image = Image.open(image_path)

# Görseli gösterin
image.show()


karakter_tablosu = '''      Karakter	     |      Po       |   Tigress    |    Mantis  |       Monkey  |    Viper |   Crane    |   Shifu
      -------------------------------------------------------------------------------------------------------------------------------------
        Po	            |     -          | Kazanır      | Kaybeder    | Kazanır     |Kaybeder   |Kazanır      |Kaybeder.
        Tigress          |   Kaybeder    |  -           |  Kazanır     | Kaybeder    |Kazanır    |Kaybeder      |Kazanır 
        Mantis	        |   Kazanır     |  Kaybeder    |     -        | Kazanır     |Kaybeder   |Kaybeder     |Kazanır 
        Monkey	        |   Kaybeder    | Kazanır      | Kaybeder     |     -       |Kazanır    |Kaybeder     |Kazanır 
        Viper	        |   Kazanır     |Kaybeder      | Kazanır      | Kaybeder    |    -      |Kazanır     |Kaybeder.
        Crane            |  Kaybeder     | Kazanır      | Kazanır      | Kaybeder    |Kaybeder   |    -        |Kazanır 
        Shifu            |  Kazanır      | Kaybeder     | Kaybeder     | Kazanır     |Kazanır    |KKaybeder    |    -           ''' 
        
        #kung fu panda serisinde geçen karakterleri ikili karşılaştırıp kimin kazanıp kimin kaybedeceğini açıklayan bir tablo
             
print("Kung Fu Panda Oyunu'na hoşgeldin kullanıcı!") #oyuna karşılama metni
print("Bu oyunun kuralları çok bilinen taş kağıt makas oyunuyla paraleldir.") 
print("Bu çok sevilen animasyon film serisindeki karakterlerin kendi aralarında düello yapsalar kimin yeneceğine dayanan bir oyundur.")
print(" (Sonuçlar tamamen hayal gücüne dayalıdır :) ) "  )
print("Kurallar Tablosu: \n\n "  , karakter_tablosu)

print("\n Toplamda 3 tur oynanacak. 2 turu galibiyetle bitiren oyuncu kazanır.") 
print("Beraberlik durumunda tur sayısının artacağını unutma!") 
print("Hadi Başlayalım!") 
print( "tas_kagit_makas_FEYZA_YİLDİZ() fonksiyonunu çağırmalısın")
print ("dipnot:  oyunu daha verimli oynamak için konsolunu genişletmeni öneririm!")

 

win_conditions = {  #koşulları daha kolay kullanmak için bir dictionary 
    "po": {"tigress", "monkey", "crane"},
    "tigress": {"mantis", "viper", "shifu"},
    "mantis": {"po", "monkey", "shifu"},
    "monkey": {"viper", "crane", "shifu"},
    "viper": {"po", "mantis", "crane"},
    "crane": {"tigress", "monkey", "viper"},
    "shifu": {"po", "mantis", "monkey"}
}



def determine_winner(player, computer):#turun kazanan ve kaybedenini belirlemek için bir fonksiyon
    if player == computer:
        return "Beraberlik!"
    
    # Eğer bilgisayar seçimi player'ın kazanma koşulları arasında ise
    if computer in win_conditions.get(player, {}):
        return f"{player} kazandı!"
    else:
        return f"{computer} kazandı!"

def tas_kagit_makas_FEYZA_YİLDİZ():
    secenekler = list(win_conditions.keys()) #dictionarydaki keys değerlerine karşılık gelir.keys() fonksiyonu ile çağırma
    #başlangıç değerleri
    tur_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0
    
    
   
    while True:  # Oyun döngüsü
        baslangic = input("Oynamaya hazır mısın? (Evet/Hayır): ").lower()
        if baslangic != "evet":
           print("O zaman beni neden boş yere çağırıyorsun?")
           break
       
        if baslangic == "evet":
           
           while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            player = input("7 usta dövüşçüden birini seçin: {Po, Tigress, Mantis, Monkey, Viper, Crane, Shifu}: ").lower() 
            #kullanıcı büyük harf girdiğinde hata vermemesi için lower() function

            if player not in secenekler:
                print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")
                continue

            computer = random.choice(secenekler)
            print("Bilgisayarın seçimi: ", computer)

            result = determine_winner(player, computer)
            print(result)

            if result.startswith(player):
                oyuncu_galibiyetleri += 1
                print ("Siz:", oyuncu_galibiyetleri ,"Bilgisayar:" ,bilgisayar_galibiyetleri)
            elif result.startswith(computer):
                bilgisayar_galibiyetleri += 1
                print ("Siz:", oyuncu_galibiyetleri ,"Bilgisayar:", bilgisayar_galibiyetleri)

            tur_sayisi += 1
            print("Tur sayısı:", tur_sayisi)

        if oyuncu_galibiyetleri == 2:
            print("Tebrikler, oyunu kazandınız!")
        else:
            print("Bilgisayar oyunu kazandı. Başarılar dileriz!")

        # Devam etmek isteyip istemediklerini soruyoruz
        devam_bilgisayar = random.choice(["evet", "hayır"])
        if devam_bilgisayar == "hayır":
            print("Üzgünüm ,gerçekten yoruldum şu an için oynamak istemiyorum.Bilgisayar olmam yorulmayacağım anlamına gelmez değil mi:") 
            print("Benimle oynadığın için teşekkür ederim! Bir dahaki sefere görüşürüz.")
            break
        if devam_bilgisayar == "evet":
            devam_oyuncu = input("Sizinle tekrar oynamak isterim, başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
            
            if devam_oyuncu == "evet":
                print("Meydan okuma başlasın!")
                tas_kagit_makas_FEYZA_YİLDİZ()
            else:
                print("Pekala, benimle oynadığın için teşekkür ederim!")
                break
      
tas_kagit_makas_FEYZA_YİLDİZ()

     