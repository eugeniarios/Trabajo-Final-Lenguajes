from fastapi import FastAPI
from services.roi_service import load_roi_by_genre, load_roi_by_country
from services.runtime_service import load_runtime_evolution
from services.correlation_service import load_budget_rating_corr

app = FastAPI(title="Data Analyst Films API")

@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}

@app.get("/roi/genre")
def roi_genre():
    return load_roi_by_genre().to_dict()

@app.get("/roi/country")
def roi_country():
    return load_roi_by_country().to_dict()

@app.get("/runtime/evolution")
def runtime():
    return load_runtime_evolution().to_dict()

@app.get("/correlation/budget-rating")
def correlation():
    return load_budget_rating_corr().to_dict()