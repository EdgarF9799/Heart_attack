
# Heart_attack
The dataset "heart.csv" deals with the study of heart attacks, through a study carried out on 303 individuals and using various variables, such as age, gender, triglycerides, cholesterol and height, among others. This study carried out not only shows the complexity of cardiovascular health by uniting certain variables that allow recognizing heart attacks, but also offers a perspective of preventing heart disease and promoting a better quality of life. Among the most important variables, we found that age and gender are crucial factors influencing heart health. As we age, the structures and functions of the heart can change, increasing the risk of heart disease. On the other hand, there are studies that have shown that there are differences in the way men and women experience and develop cardiovascular diseases. Understanding these variations is essential to offer an effective and personalized approach to care.

The dataset makes it possible to correlate different variables, which, although they have already been identified in isolated or independent ways as prone variables for a person to suffer heart attacks, the complete set would help to understand or predict whether a person is prone to a heart attack, for example. Give some examples of relationship:

Triglyceride and cholesterol levels are critical indicators of heart health, high levels of these lipids in the blood can increase the risk of plaque buildup in the arteries, which can lead to heart disease.

In summary, the detailed study of the heart, integrating factors such as age, gender, triglycerides, cholesterol, height and others, plays an essential role in the prevention and treatment of heart disease. By considering these key variables, healthcare professionals can personalize care, make informed decisions, and promote a holistic approach to ensuring cardiovascular health throughout life.


# Analysis and model of ML

An analysis of the DataSet was carried out completely in another repository, I leave the link below:

https://github.com/EdgarF9799/ProyectoFinalEFNB/blob/main/01ConceptosClave/heart_attack_EdgarFNavaBarron.ipynb


# Configuration to be able to execute the project (Windows)

We go to the folder where we will have our project hosted and execute the following command in CMD to create a virtual environment to install Python version "3.10"
  ```bash
python310 -m venv venv
  ```
and we activate 
  ```bash
source venv/bin/activate
  ```
We are going to have to install some libraries, for this we define a list in a file called "Requirements"

  ```bash
(venv) PS C:\Users\Edgar F\Desktop\EdgarProyecto02\HEART_ATTACK> pip install -r ./requirements_dev.txt
  ```

# Test Loggin

The following link contains the validation tests, which are necessary to execute our project (remembering that the code was simplified to execute the project in a simpler way).

https://github.com/EdgarF9799/Heart_attack/blob/main/heart_attack/tests/test_heart_attack.py


and the code to test would be the following, in the terminal

  ```bash
pytest "C:\Users\Edgar F\Desktop\EdgarProject02\Heart_attack\heart_attack\tests\test_heart_attack.py" -v
  ```

# Docker 

Run the next command to start the Mobile Price API locally:
  ```bash
uvicorn api.main:app --reload
  ```

In the browser you must enter with the following path

  ```bash
Access http://127.0.0.1:8000/docs/
  ```

![Evidencia01](https://github.com/EdgarF9799/Heart_attack/blob/b89b024d34cf5d3cc0774604c7312d8de6c5539c/Images/01_EvidenciaApi.png)


To run the application, the following format will be used (an example is given below):
  ```bash
{"age": 57.0,
  "sex": 1.0,
  "cp": 2.0,
  "trtbps": 150.0,
  "chol": 168.0,
  "fbs": 0.0,
  "restect": 1.0,
  "thalachh": 174.0,
  "exng": 0.0,
  "oldpeak": 1.6,
  "slp": 2.0,
  "cae": 0.0,
  "thall": 2.0}
  ```

![Evidencia02](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/02_EvidenciaApi.png)

The API trains according to the model, to start just enter the patient's data and press the execute button

![Evidencia04](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/04_EvidenciaApi.png)

The application predicts based on the assigned variables if a person is prone to cardiac arrest (result "1") con el siguiente mensaje

  ```bash
"Are you having a heart attack? Response: [1]"
  ```

Logs are integrated and an image is shared.


![Evidencia03](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/03_EvidenciaApi.png)


# API deployment with Docker

Being in the root directory, we will use the following command:

  ```bash
docker build -t heart_attack-image ./heart_attack/heart_attack/app/
  ```


![Evidencia05](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/05_EvidenciaApi.png)



we will make an image with Docker

  ```bash
docker build -t mobilepc-image ./mobilepc/mobilepc/app/
  ```

Let's see if I really believe

  ```bash
docker images
  ```

![Evidencia06](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/06_EvidenciaApi.png)


To start running the Docker image we use the following command
```bash
docker run -d --rm --name heart_attack-image -c -p 8000:8000 mobilepc-image
```

To access, we enter the following path:
```bash
http://127.0.0.1:8000/docs
```


![Evidencia07](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/07_EvidenciaApi.png)

put the following parameters
```bash
{"age": 57.0,
"sex": 1.0,
"cp": 2.0,
"trtbps": 150.0,
"chol": 168.0,
"fbs": 0.0,
restect: 1.0,
"thalachh": 174.0,
"exng": 0.0,
"oldpeak": 1.6,
"slp": 2.0,
"falls": 0.0,
"thall": 2.0}
```
![Evidencia08](https://github.com/EdgarF9799/Heart_attack/blob/main/Images/08_EvidenciaApi.png)

To stop Docker the following code is used:
```bash
docker-compose -f heart_attack/heart_attack/docker-compose.yml stop
```
and to delete it
```bash
docker-compose -f heart_attack/heart_attack/docker-compose.yml rm
```



