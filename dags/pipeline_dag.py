from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
from ml.train import train_model

def extract():
    response = requests.get("https://api.com/data")
    data = response.json()
    # Guarda en Postgres o disco temporal
    return data

def clean():
    # Limpieza básica, puede usar Pandas
    pass

def preprocess():
    # Preprocesamiento
    pass

def train():
    train_model()

with DAG(
    dag_id='mlops_data_pipeline',
    schedule_interval='*/5 * * * *',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='clean', python_callable=clean)
    t3 = PythonOperator(task_id='preprocess', python_callable=preprocess)
    t4 = PythonOperator(task_id='train', python_callable=train)

    t1 >> t2 >> t3 >> t4
