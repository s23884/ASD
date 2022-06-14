import math

class E:
    def __init__(self, znak, priorytet):
        self.znak = znak
        self.priorytet = priorytet

class Kolejka:
    def __init__(self):
        self.dane = list()

    def umiesc(self, e):
        if self.rozmiar() == 0: self.dane.append(e)
        elif e in self.dane: return False
        else:
            for x in range(0, self.rozmiar()):
                if e.priorytet <= self.dane[x].priorytet:
                    if x == (self.rozmiar() - 1): self.dane.insert(x + 1, e)
                    else: continue
                else:
                    self.dane.insert(x, e)
                    return True

    def usun(self): return self.dane.pop(0)

    def rozmiar(self): return len(self.dane)

with open('wejscie.txt', 'r') as plik: wejscie = plik.read()

kolejka = Kolejka()
slownik = dict()

for znak in "".join(set(wejscie)): kolejka.umiesc(E(znak, wejscie.count(znak)))

while (kolejka.rozmiar() > 0):
    e = kolejka.usun()
    slownik[e.znak] = e.priorytet

dlugosc_slowa = math.ceil(math.log(len(slownik), 2))

with open('wyjscie.txt', 'w') as plik:
    print(slownik, file=plik)

bity = []
for znak in wejscie:
    for bit in "{:0{ds}b}".format(list(slownik.keys()).index(znak), ds=dlugosc_slowa):
        bity.append(bit)

with open('wyjscie.txt', 'ab') as plik:
    for bajt in zip(*[iter(bity)]*8):
        plik.write(bytes([int("".join(bajt), 2)]))