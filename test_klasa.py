class Osoba:
    def __init__(
        self, ime, prezime, spol, starost, grad, drzava, omiljena_boja
    ):
        self.ime = ime
        self.prezime = prezime
        self.spol = spol
        self.starost = starost
        self.grad = grad
        self.drzava = drzava
        self.omiljena_boja = omiljena_boja

# osoba = Osoba("Pero", "Perić", "M", 20, "Zagreb", "Hrvatska", "Bijela")

class Osoba2:
    def __init__(self, *args):
        print(args)
        self.ime = args[0]
        self.prezime = args[1]
        self.spol = args[2]

# osoba2 = Osoba2("Pero", "Perić", "M")   - OK
# osoba2 = Osoba2("Pero", "Perić", "M", 20)   - OK, ali se 20 ne koristi nigdje
# osoba2 = Osoba2("Pero", "Perić")   - nije OK, fali nam jedan argument

class Osoba3:
    def __init__(self, **kwargs):
        print(kwargs)
        self.ime = kwargs["ime"]
        self.prezime = kwargs["prezime"]
        self.spol = kwargs["spol"]
        self.grad = kwargs["grad"]

# osoba3 = Osoba3(ime="Pero", prezime="Perić", spol="M", grad="Zagreb") - OK
# osoba3 = Osoba3(ime="Pero", prezime="Perić", spol="M", grad="Zagreb", starost=20) - OK, ali se starost ne koristi
# osoba3 = Osoba3(ime="Pero", prezime="Perić", grad="Zagreb") - nije OK jer fali key "spol"

class Osoba4:
    def __init__(self, *args, **kwargs):
        self.ime = args[0]
        self.prezime = args[1]
        self.spol = kwargs["spol"]
        self.grad = kwargs["grad"]


