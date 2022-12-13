import random
class Harcos:
    def __init__ (self, nev = "Ismeretlen", eletero = 0, harciEro = 0, pluszElet = True ):
        self.nev = nev
        self.eletero = eletero
        self.harciEro = harciEro
        self.pluszElet = pluszElet


    def info (self):
        print("Név: {}".format(self.nev))
        print("Életerő: {}".format(round(self.eletero, 2)))
        print("Harci erő: {}".format(self.harciEro))
        print("Plusz élet: {}".format(self.pluszElet))


    def harcol (self):
        self.eletero = self.eletero + (random.uniform(-4.5, 1.5) * self.harciEro / 10)
        if (self.eletero > 10.0):
            self.eletero = 10.0

        if (self.eletero < 0.0 and self.pluszElet == True):
            self.pluszElet = False
            self.eletero = 10.0

        if (self.eletero < 0.0 and self.pluszElet == False):
            print("A vesztes: {}".format(self.nev))
            exit()
        return self.eletero


  
            

megatron = Harcos("Megatron", 8.20, 4.70)
optimus = Harcos("Optimus", 9.90, 4.80)

for i in range (1, 21):
    print("----------------------------------------")
    print("{}. Forduló".format(i))
    i += 1
    optimus.harcol()
    print()
    optimus.info()
    print()
    megatron.harcol()
    print()
    megatron.info()



