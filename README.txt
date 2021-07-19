iyi günler hocam.

Ben Q learning yaptım.Ödevi yaparken python3.6 ve grafik işlemleri için pygame1.9.6 kütüphanesi kullandım .
https://www.pygame.org/wiki/GettingStarted 
bu adresten kütüphaneyi indirebilirsiniz

Oyun Açıklama
1-Oyun 10x10 grid yapsı üzerinde 0,0 (sol üst köşe yeşil kutucuk) de bulunan egent imiz var bu agent 9,9 (sağ alt köşe kırmızı kutucuk) da ki kutuya sizin belirttiğiniz engellere takılmadan ulaşmaya çalışıyor. 
2.Oyun ilk açıldığında boş bir grid uzayı olarak açılıyor eğer isterseniz mause kullanarak gridlere tıklayarak engeller ekleyebilir, eklediğiniz engeli kaldırmak için tekrar üstüne tıklayabilirsiniz.
3.Engelleri ekledikten sonra Q-learningi çalıştırmak için yeşil kutucuğa (sol üst) tıklamanız gerek.

Q-Learning Environment Açıklama
1-Hocam burada enviroment sabit olmadığı için yani kullanıcı tarafından değiştirilebildiğinden hedef noktası yani kırmızı kutucuğu baz alarak tüm kutulara oklid uzaklığına göre değer atadım bu kısmen daha mantıklı bir environment oluşturduğu için böyle yaptım.
2-Eklenen engelleri enviromentte çok düşük bir değerle temsil ettim 

Q-learning Q-Table Açıklama
Q tablomda her bir grid yani state için 4 farklı action var hocam bunlar sol,sağ,yukarı,aşağı program kısmında kodlarkende aynı şekilde liste içinde böyle kodladım [sol,sağ,yukarı,aşağı] (program satır 30)

*Living Penalty tanımlamam gerektiğini düşündüm bunuda -10 olarak aldım (program satir 56)

-program içindede elimden geldiğince yorum satırları eklemeye çalıştım.

sevgiler saygılar iyi çalışmalar hocam.
