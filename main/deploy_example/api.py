from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from run_model import make_prediction

class WineFeatures(BaseModel):
    fixed_acidity: Optional[float]
    volatile_acidity: Optional[float]
    citric_acid: Optional[float]
    residual_sugar: Optional[float]
    chlorides: Optional[float]
    free_sulfur_dioxide: Optional[float]
    total_sulfur_dioxide: Optional[float]
    density: Optional[float]
    pH: Optional[float]
    sulphates: Optional[float]
    alcohol: Optional[float]

app = FastAPI()

@app.post("/make_prediction")
def operate(input: WineFeatures):

    if input.alcohol is None:
        raise ValueError("The alcohol content must be entered")

    result = make_prediction([input.fixed_acidity,
                              input.volatile_acidity,
                              input.citric_acid,
                              input.residual_sugar,
                              input.chlorides,
                              input.free_sulfur_dioxide,
                              input.total_sulfur_dioxide,
                              input.density,
                              input.pH,
                              input.sulphates,
                              input.alcohol])
    return result

