from pydantic import BaseModel


class Heart(BaseModel):
    """
    Represents a mobile phone with various attributes.

    Attributes:

    age (float): Placeholder for  age attribute
    sex (float): Placeholder for  sex attribute
    cp (float): Placeholder for  cp attribute
    trtbps (float): Placeholder for  trtbps attribute
    chol (float): Placeholder for  chol attribute
    fbs (float): Placeholder for  fbs attribute
    restecg (float): Placeholder for  restecg attribute
    thalachh (float): Placeholder for thalachh attribute
    exng (float): Placeholder for  exng attribute
    oldpeak (float): Placeholder for  oldpeak attribute
    slp (float): Placeholder for  slp attribute
    caa (float): Placeholder for  caa attribute
    thall (float): Placeholder for  thall attribute
    """

    age: float 
    sex: float 
    cp: float 
    trtbps: float 
    chol: float 
    fbs: float 
    restecg: float 
    thalachh: float
    exng: float 
    oldpeak: float 
    slp: float 
    caa: float 
    thall: float
