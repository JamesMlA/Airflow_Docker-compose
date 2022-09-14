from datetime import datetime, timedelta
from sched import scheduler

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'ancordss',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_git_v03",
    start_date=datetime(2022,9,1),
    schedule_interval='1 * * * *'
) as dag:
    task1 = BashOperator(
        task_id='pulling_repository',
        bash_command='git pull'
    )
    task1
