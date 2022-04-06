from fastapi import Request, FastAPI
from vehicules import Bateau, Moto, Voiture, Avion
from fastapi.responses import JSONResponse
from json import JSONDecodeError

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