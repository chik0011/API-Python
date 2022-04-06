from fastapi import Request, FastAPI
from vehicules import Bateau, Moto, Voiture, Avion
from fastapi.responses import JSONResponse
from json import JSONDecodeError
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "L'api est lancé !"}


@app.post("/addBateau")
async def create_item(request: Request):
    data = await request.json()

    print(data)
    bateau = Bateau(data["name"], data["marque"], data["speedMax"], data["km"])
    return bateau

@app.post("/addVoiture")
async def create_item(request: Request):
    data = await request.json()

    print(data)
    voiture = Voiture(data["name"], data["marque"], data["speedMax"], data["km"])
    return voiture

@app.post("/addAvion")
async def create_item(request: Request):
    data = await request.json()

    print(data)
    avion = Avion(data["name"], data["marque"], data["speedMax"], data["km"])
    return avion

@app.post("/addMoto")
async def create_item(request: Request):
    data = await request.json()

    print(data)
    moto = Moto(data["name"], data["marque"], data["speedMax"], data["km"])
    return moto

@app.get("/totalVehicule")
async def total():
    with open('bateau.json') as json_data:
        data_bateau = json.load(json_data)

    lenBateau = len(data_bateau)

    with open('avion.json') as json_data:
        data_avion = json.load(json_data)

    lenAvion = len(data_avion)

    with open('moto.json') as json_data:
        data_moto = json.load(json_data)

    lenMoto = len(data_moto)

    with open('voiture.json') as json_data:
        data_voiture = json.load(json_data)

    lenVoiture = len(data_voiture)

    total = lenBateau + lenAvion + lenMoto + lenVoiture

    return {"TotalVehicule": total} 


'''
    type == 0 => bateau
    type == 1 => avion
    type == 2 => moto
    type == 3 => voiture
'''

@app.post("/totalPerVehicule")
async def numberVehicule(request: Request):
    data = await request.json()

    if data["type"] == "0":
        with open('bateau.json') as json_data:
            data_bateau = json.load(json_data)

        total = len(data_bateau)

    elif data["type"] == "1":
        with open('avion.json') as json_data:
            data_avion = json.load(json_data)

        total = len(data_avion)

    elif data["type"] == "2":
        with open('moto.json') as json_data:
            data_moto = json.load(json_data)

        total = len(data_moto)

    elif data["type"] == "3":
        with open('voiture.json') as json_data:
            data_voiture = json.load(json_data)

        total = len(data_voiture)

    return { "TotalVehicule": total } 