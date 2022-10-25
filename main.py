from fastapi import FastAPI
from pydantic import BaseModel


class Personne(BaseModel):
    nom: str
    prenom: str
    age: int
    taille: float | None = None
    poids: float | None = None
    sport: str | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(personne: Personne):
    personne.nom = "Marembert"
    personne.prenom = "Quentin"
    personne.age =  22
    return personne