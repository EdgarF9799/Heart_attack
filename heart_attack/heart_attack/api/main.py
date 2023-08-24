import os
import subprocess

import pandas as pd
from fastapi import FastAPI, HTTPException, status
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse

from .models.models import Heart

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
GRANDPARENT_DIR = os.path.abspath(os.path.join(PARENT_DIR, ".."))
ROOT_DIR = os.path.abspath(os.path.join(GRANDPARENT_DIR, ".."))
DATASETS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "data"))


PIPELINE_SAVE_FILE = PARENT_DIR + f'\\models\\rf_heart_attack.pkl'

PYTHON_DIR = ROOT_DIR + '\\venv\\Scripts\\python'

app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    return 'Heart Attack predictor is all ready to go!'


@app.post('/predict')
def extract_name(heart_features: Heart):
    try:
        predictor = ModelPredictor(PIPELINE_SAVE_FILE)
        X = {'age': [heart_features.age], 
            'sex': [heart_features.sex], 
            'cp': [heart_features.cp], 
            'trtbps': [heart_features.trtbps], 
            'chol': [heart_features.chol], 
            'fbs': [heart_features.fbs], 
            'restecg': [heart_features.restecg], 
            'thalachh': [heart_features.thalachh],
            'exng': [heart_features.exng], 
            'oldpeak': [heart_features.oldpeak], 
            'slp': [heart_features.slp], 
            'caa': [heart_features.caa], 
            'thall': [heart_features.thall]            
             }
        prediction = predictor.predict(pd.DataFrame(X))
        return JSONResponse(f"Are you having a heart attack? Response: {prediction}")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "result: invalid format",
                "hints": [
                    "Check the numbers",
                    "Must be float",
                    "It is recommended avoid all zeros in petition"
                ],
            },
        ) from e

