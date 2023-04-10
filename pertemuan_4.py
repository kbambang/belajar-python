# for i in range (10)
#   print()

# Study Case 
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = "pintu"
        self.mobil = "mobil"

    def membukaPintu(self):
        if self.pintu == "tertutup":
            print("Pintu Berhasl Dibuka")
            self.pintu = "terbuka"
        else:
            print("Pintu Telah Terbuka")

    def menutupPintu(self):
        if self.pintu == "terbuka":
            print("Pintu Berhasil Ditutup")
            self.pintu = "tertutup"
        else:
            print("Pintu Telah Tertutup")

    def menyalakanMobil(self):
        if self.mobil == "mati":
            print("Mobil Berhasil Dinyalakan")
            self.mobil = "menyala"
        else:
            print("Mobil Sudah Menyala")

    def mematikanMobil(self):
        if self.mobil == "menyala":
            print("Mobil Berhasil Dimatikan")
            self.mobil = "mati"
        else:
            print("Mobil Sudah Mati")

mobilku = Car("toyota", 2021)

mobilku.membukaPintu()
mobilku.membukaPintu()
mobilku.menutupPintu()
mobilku.menutupPintu()
mobilku.menyalakanMobil()
mobilku.menyalakanMobil()
mobilku.mematikanMobil()
mobilku.mematikanMobil()