class Bateau:

    def __init__(self, name, marque, speedMax, km):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km

"""
class Voiture(name, marque, speedMax, km):
    def __init__(self):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km


class Moto(name, marque, speedMax, km):
    def __init__(self):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km


class Avion(objetJeu, arme):
    def __init__(self):
        objetJeu.__init__(self)
        arme.__init__(self)

"""

if __name__ == "__main__":

    Bateau = Bateau("toto", "nike", 56)

    print(Bateau)

