class Haz:
    def __init__(self, helyrajziSzam = "", villanyoraAllas = 0.00, vizoraAllas = 0.00, esovizgyujtoTartaly = 0.00, mozgaserzekeloKiBe = False):
        self.helyrajziSzam = helyrajziSzam
        self.villanyoraAllas = villanyoraAllas
        self.vizoraAllas = vizoraAllas
        self.mozgaserzekeloKiBe = mozgaserzekeloKiBe
        self.esovizgyujtoTartaéy = esovizgyujtoTartaly


    def info(self):
        print("Helyrajzi szám: {}".format(self.helyrajziSzam))
        print("Villanyóra állása: {}".format(self.villanyoraAllas))
        print("Vízóra állása: {}".format(self.vizoraAllas))
        print("Esővízgyűjtő tartály: {}".format(self.esovizgyujtoTartaéy))
        print("Mozgásérzékelő: {}".format(self.mozgaserzekeloKiBe))
        print()


    def kapcsol(self):
        if (self.mozgaserzekeloKiBe == True):
            self.mozgaserzekeloKiBe = False
        else:
            self.mozgaserzekeloKiBe = True

        if (self.mozgaserzekeloKiBe == True):
            self.villanyoraAllas = self.villanyoraAllas - 0.05


hasznalt = Haz("KH23456-14", 124.25, 23.50, 3.25, True)
ujepitesu = Haz("KH25681-58")


print("Használt kertesház: ")
hasznalt.info()

print("Újépítésű kertesház: ")
ujepitesu.info()

hasznalt.kapcsol()
hasznalt.kapcsol()
ujepitesu.kapcsol()
ujepitesu.kapcsol()
ujepitesu.kapcsol()
ujepitesu.kapcsol()
ujepitesu.kapcsol()

print("Használt kertesház: ")
hasznalt.info()

print("Újépítésű kertesház: ")
ujepitesu.info()


