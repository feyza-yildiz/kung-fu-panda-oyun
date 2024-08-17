Kung Fu Panda Taş Kağıt Makas Oyunu:

Bu proje, Kung Fu Panda filmindeki 6 usta dövüşçü ve Usta Shifu'nun yer aldığı bir taş kağıt makas oyunudur. 
Oyuncular, filmdeki karakterlerden birini seçerek bilgisayara karşı mücadele ederler.
Oyun, klasik taş kağıt makas oyunu mantığıyla çalışır ve her turda karakterlerin birbirlerine karşı kazandığı, kaybettiği ya da berabere kaldığı bir durum oluşur.

İçindekiler:
-Kurulum
-Kullanım
-Oyun Mantığı


Kurulum:
Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

Bu repository'yi kopyalayın: git clone https://github.com/feyza-yildiz/kung-fu-panda-oyun
Projeyi çalıştırın: python main.py

Kullanım:
Oyunu başlattığınızda, oyuncu bir karakter seçecek ve bilgisayar da rastgele bir karakter seçecek. Kazanan, kaybeden veya beraberlik durumu ekrana yazdırılacak. Oyun toplamda 3 tur oynanacak, 2 tur kazanan oyunu kazanır.

Oyun Mantığı:
Her karakterin farklı karakterlere karşı kazanma veya kaybetme olasılıkları vardır. Bu ilişkiler şu şekildedir:

Po kazandığı karakterler: Tigress, Monkey, Crane
Tigress kazandığı karakterler: Mantis, Viper, Shifu
Mantis kazandığı karakterler: Po, Monkey, Shifu
Monkey kazandığı karakterler: Viper, Crane, Shifu
Viper kazandığı karakterler: Po, Mantis, Crane
Crane kazandığı karakterler: Tigress, Monkey, Viper
Shifu kazandığı karakterler: Po, Mantis, Monkey
Bu ilişkiler oyun sırasında kullanılarak kazanan belirlenir.
