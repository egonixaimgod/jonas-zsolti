class Torta:
    def __init__ (self, emeletekSzama = 1, megVanKenve = False):
        self.emeletekSzama = emeletekSzama
        self.megVanKenve = megVanKenve

    def ujEmelet (self):
        self.emeletekSzama = self.emeletekSzama + 1

    def kremmelMegken (self):
        if (self.megVanKenve == False):
            self.megVanKenve = True
            print("Sikeres kenés") 
        elif (self.megVanKenve == True):
            print("Sikertelen kenés")

    
    def mennyiKaloria (self):
        emeletKaloria = 1000
        haVanKrem = 2
        ennyikaloria = self.emeletekSzama * emeletKaloria 
        if (self.megVanKenve == True):
            ennyikaloria = haVanKrem * ennyikaloria
        print ("Kalória: {}".format(ennyikaloria))


    def info(self):
        
        print("Emeletek Száma: {}".format(self.emeletekSzama))
        print("Meg van kenve: {}".format(self.megVanKenve))
        


torta1 = Torta(2, True)
torta2 = Torta()

print("Torta1")
torta1.info()
print()
print("Torta2")
torta2.info()
print()
print("Torta2 krémmel kenése 2x")
torta2.kremmelMegken()
torta2.kremmelMegken()
print()
print("Torta1 újabb emelet")
torta1.ujEmelet()
print()
print("Torta1")
torta1.info()
print()
torta1.mennyiKaloria()
print()
print("Torta2")
torta2.info()
print()
torta2.mennyiKaloria()
