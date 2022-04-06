from fastapi import Request, FastAPI
from vehicules import Bateau, Moto, Voiture, Avion
from fastapi.responses import JSONResponse
from json import JSONDecodeError
import json

from starlette.exceptions import HTTPException as StarletteHTTPException

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

@app.post("/findVehicule")
async def find_item(request: Request):

    data = await request.json()

    findVehicule = "Aucun vehicule n'a était trouvé"

    with open('bateau.json') as json_data:
            data_bateau = json.load(json_data)

    for bateau in data_bateau:
        for j in range(len(bateau)):
            if bateau["name"] == data["name"] :
                findVehicule = bateau
            elif bateau["marque"] == data["marque"] :
                findVehicule = bateau
            elif bateau["speedMax"] == data["marque"] :
                findVehicule = bateau
            elif bateau["km"] == data["marque"] :
                findVehicule = bateau

    with open('avion.json') as json_data:
            data_avion = json.load(json_data)

    for avion in data_avion:
        for j in range(len(avion)):
            if avion["name"] == data["name"] :
                findVehicule = avion
            elif avion["marque"] == data["marque"] :
                findVehicule = avion
            elif avion["speedMax"] == data["marque"] :
                findVehicule = avion
            elif avion["km"] == data["marque"] :
                findVehicule = avion

    with open('moto.json') as json_data:
            data_moto = json.load(json_data)

    for moto in data_moto:
        for j in range(len(moto)):
            if moto["name"] == data["name"] :
                findVehicule = moto
            elif moto["marque"] == data["marque"] :
                findVehicule = moto
            elif moto["speedMax"] == data["marque"] :
                findVehicule = moto
            elif moto["km"] == data["marque"] :
                findVehicule = moto
       
    with open('voiture.json') as json_data:
            data_voiture = json.load(json_data)

    for voiture in data_voiture:
        for j in range(len(voiture)):
            if voiture["name"] == data["name"] :
                findVehicule = voiture
            elif voiture["marque"] == data["marque"] :
                findVehicule = voiture
            elif voiture["speedMax"] == data["marque"] :
                findVehicule = voiture
            elif voiture["km"] == data["marque"] :
                findVehicule = voiture
       
    return findVehicule

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })

