from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

class Alien(BaseModel):
    name: str
    type: str
    hp: int
    atk: int
    spd: int

# In-memory storage for aliens
aliens_db: List[Alien] = []

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/api/aliens")
def add_aliens(aliens: List[Alien]):
    aliens_db.extend(aliens)
    return {"message": f"Added {len(aliens)} aliens"}

@app.get("/api/aliens")
def get_aliens(
    spd_lte: int = Query(None),
    spd_gte: int = Query(None),
    atk_lte: int = Query(None),
    atk_gte: int = Query(None),
    hp_lte: int = Query(None),
    hp_gte: int = Query(None),
    type: str = Query(None)
):
    results = aliens_db
    if spd_lte is not None:
        results = [a for a in results if a.spd <= spd_lte]
    if spd_gte is not None:
        results = [a for a in results if a.spd >= spd_gte]
    if atk_lte is not None:
        results = [a for a in results if a.atk <= atk_lte]
    if atk_gte is not None:
        results = [a for a in results if a.atk >= atk_gte]
    if hp_lte is not None:
        results = [a for a in results if a.hp <= hp_lte]
    if hp_gte is not None:
        results = [a for a in results if a.hp >= hp_gte]
    if type is not None:
        results = [a for a in results if a.type == type]

    return results

@app.delete("/api/aliens")
def clear_aliens():
    aliens_db.clear()
    return {"message": "All aliens cleared"}
