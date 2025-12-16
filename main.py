from fastapi import FastAPI
from pydantic import BaseModel
from kerykeion import AstrologicalSubject

app = FastAPI()

class BirthData(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    city: str
    lat: float
    lng: float

@app.post("/calculate")
async def calculate_map(data: BirthData):
    try:
        # Cria a instância do mapa
        user = KrInstance(
            "User", 
            data.year, data.month, data.day, 
            data.hour, data.minute, 
            data.city, lat=data.lat, lng=data.lng
        )

        # Extrai os dados
        sun = user.sun['sign']
        moon = user.moon['sign']
        rising = user.first_house['sign'] # Ascendente é a Casa 1

        return {
            "status": "success",
            "sun": sun,
            "moon": moon,
            "rising": rising,
            "full_data": {
                "sun_house": user.sun['house'],
                "moon_house": user.moon['house']
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def read_root():
    return {"status": "Online", "service": "Netzach Astrology API"}
