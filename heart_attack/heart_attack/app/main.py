import logging
import subprocess

import pandas as pd
from fastapi import FastAPI, HTTPException, status
from models.models import Heart
from predictor.predict import ModelPredictor
from starlette.responses import JSONResponse


PIPELINE_SAVE_FILE = f'models_ml/rf_heart_attack.pkl'

logger = logging.getLogger(__name__)  # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG)  # Configuramos el nivel de logging
formatter = logging.Formatter(
    '%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')  # Creamos el formato
# Indicamos el nombre del archivo
file_handler = logging.FileHandler('main_api.log')
file_handler.setFormatter(formatter)  # Configuramos el formato
logger.addHandler(file_handler)  # Agregamos el archivo


app = FastAPI()


@app.get('/', status_code=200)
async def healthcheck():
    logger.info("Heart Attack predictor is all ready to go!")
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
        logger.info(f"Are you having a heart attack? Response: {prediction}")
        return JSONResponse(f"Are you having a heart attack? Response: {prediction}")
    except Exception as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error: {str(e)}")
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

