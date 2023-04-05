class Sirket():
    def __init__(self, ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuSecim()
        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            ySecim = input("Yıllık bazda maaşları görmek ister misiniz?(E/H): ")
            if ySecim == "E" or ySecim == "e":
                self.verilecekMaasGoster(hesap="y")
            else:
                self.verilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()
        

    def menuSecim(self):
        secim = int(input("**** {} Otomasyonuna hoşgeldiniz****\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek maaş göster\n4-Maaşları ver\n5-Masraf Gir\n6-Gelir Gir\n\nSeçiminizi giriniz: ".format(self.ad)))
        while secim < 1 or secim > 6:
            int(input("Lütfen 1 - 6 arasında belirtilen seçeneklerden birini giriniz: "))
        return secim
    def calisanEkle(self):
        id = 1
        ad = input("Çalışanın adı: ")
        soyad = input("Çalışanın soyadı: ")
        yas = input("Çalışanın yaşı: ")
        cinsiyet = input("Çalışanın cinsiyeti: ")
        maas = input("Çalışanın maaşı: ")

        with open("calisanlar.md", "r") as dosya:
            calisanListesi = dosya.readlines()
            print(calisanListesi)

        if len(calisanListesi) == 0:
            id = 1
        else:
            with open("calisanlar.md", "r") as dosya:
               id = int(dosya.readlines()[-1].split(")")[0]) + 1
        
        with open("calisanlar.md", "a+", encoding='utf-8') as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id, ad, soyad, yas, cinsiyet, maas))


    def calisanCikar(self):
        with open("calisanlar.md","r") as dosya:
            calisanlar = dosya.readlines()
        gCalisanlar = []

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))
        for calisan in gCalisanlar:
            print(calisan)
        
        secim = int(input("Lütfen çıkartmak istediğiniz çalışanın ID numarasını giriniz(1-{})").format(len(gCalisanlar)))
        while secim < 1 or secim > len(gCalisanlar):
            input("Lütfen 1 - {} arasında bir sayı giriniz: ".format(len(gCalisanlar)))

    def verilecekMaasGoster(self, hesap="a"):
        """Hesap parametresi a ise aylık y ise yıllık hesap"""
        with open("calisanlar.md","r", encoding='utf-8') as dosya:
            calisanlar = dosya.readlines()
        
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        
        if hesap == "a":
            print("Bu ay toplam verilecek maaş: {}".format(sum(maaslar)))
        else:
            print("Bu yıl toplam verilecek maaş: {}".format(sum(maaslar) * 12))

    def maaslariVer(self):
         with open("calisanlar.md","r", encoding='utf-8') as dosya:
            calisanlar = dosya.readlines()
        
            maaslar = []

            for calisan in calisanlar:
                maaslar.append(int(calisan.split("-")[-1]))
            
            toplamMaas = sum(maaslar)

            ### Bütçeden maaşı alma ###
            with open("butce.md","r", encoding='utf-8') as dosya:
                tbutce = int(dosya.readlines()[0])
            
            tbutce = tbutce - toplamMaas
            
            with open("butce.md","w", encoding="utf-8") as dosya:
                dosya.write(str(tbutce))

    def masrafGir(self):
        tMasraf = int(input("Toplam masrafınızı giriniz: "))
        with open("butce.md","r", encoding='utf-8') as dosya:
                tbutce = int(dosya.readlines()[0])
        tbutce = tbutce - tMasraf
        
        with open("butce.md","w", encoding="utf-8") as dosya:
                dosya.write(str(tbutce))
                print("Kalan bütçeniz: {}".format(tbutce))

    def gelirGir(self):
        tGelir = int(input("Toplam gelirinizi giriniz: "))
        with open("butce.md","r", encoding='utf-8') as dosya:
                tbutce = int(dosya.readlines()[0])
        tbutce = tbutce + tGelir
        
        with open("butce.md","w", encoding="utf-8") as dosya:
                dosya.write(str(tbutce))
                print("Yeni bütçeniz: {}".format(tbutce))



sirket = Sirket("MB Yazılım")

while sirket.calisma:
    sirket.program()
