import _pickle as cPickle
import traceback
import json
from os import path

class Bateau:
    def __init__(self, name, marque, speedMax, km):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km

        filename = 'bateau.json'
        listObj = []

        if path.isfile(filename) is False:
            raise Exception("Fichier pas trouvé")
        
        with open(filename) as fp:
            listObj = json.load(fp)
        
        listObj.append({
            "name": self.name,
            "marque": self.marque,
            "speedMax": self.speedMax,
            "km": self.km
        })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file,indent=4,separators=(',',': '))
        
        print('Fichier modifié')
        

class Voiture:
    def __init__(self, name, marque, speedMax, km):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km

        filename = 'voiture.json'
        listObj = []

        if path.isfile(filename) is False:
            raise Exception("Fichier pas trouvé")
        
        with open(filename) as fp:
            listObj = json.load(fp)
        
        listObj.append({
            "name": self.name,
            "marque": self.marque,
            "speedMax": self.speedMax,
            "km": self.km
        })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file,indent=4,separators=(',',': '))
        
        print('Fichier modifié')


class Moto:
    def __init__(self, name, marque, speedMax, km):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km

        filename = 'moto.json'
        listObj = []

        if path.isfile(filename) is False:
            raise Exception("Fichier pas trouvé")
        
        with open(filename) as fp:
            listObj = json.load(fp)
        
        listObj.append({
            "name": self.name,
            "marque": self.marque,
            "speedMax": self.speedMax,
            "km": self.km
        })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file,indent=4,separators=(',',': '))
        
        print('Fichier modifié')


class Avion:
    def __init__(self, name, marque, speedMax, km):
        self.name = name
        self.marque = marque
        self.speedMax = speedMax
        self.km = km

        filename = 'avion.json'
        listObj = []

        if path.isfile(filename) is False:
            raise Exception("Fichier pas trouvé")
        
        with open(filename) as fp:
            listObj = json.load(fp)
        
        listObj.append({
            "name": self.name,
            "marque": self.marque,
            "speedMax": self.speedMax,
            "km": self.km
        })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file,indent=4,separators=(',',': '))
        
        print('Fichier modifié')



if __name__ == "__main__":
    Bateau = Bateau("toto", "nike", 56, 25)
    print(Bateau)

