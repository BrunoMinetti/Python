def main():
    pri = Carro('brasilia', 1968, 'amarela', 80)
    seg = Carro('fuscao', 1981, 'preto', 95)

    Carro.acelere(pri, 40)
    pri.acelere(40)
    Carro.acelere(seg, 50)
    Carro.acelere(pri, 80)
    Carro.pare(pri)
    seg.pare()
    Carro.acelere(seg, 100)

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano    = a
        self.cor    = c
        self.vel    = 0
        self.maxV   = vm  # velocidade maxima

    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print( "%s %s %d"%(self.modelo, self.cor, self.ano)     )
        elif self.vel < self.maxV:
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel) )
        else:
            print( "%s %s indo muito raaaaaapiiiiiiiidoooooo!"%(self.modelo, self.cor))

    def acelere(self, v):
        self.vel = v
        if self.vel > self.maxV:
            self.vel = self.maxV
        Carro.imprima(self)

    def pare(self):
        self.vel = 0
        Carro.imprima(self)

main()

