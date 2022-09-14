from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Ancordss',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='example_dag_01',
    default_args=default_args,
    start_date=datetime(2022,9,1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id='print_to_shell_with_bash',
        bash_command='echo this is a simple bash command!'
    )

    task2 = BashOperator(
        task_id='is_liquibase_installed?',
        bash_command='liquibase --version'
    )

    task3 = BashOperator(
        task_id='is_git_installed?',
        bash_command='git --version'

    )

    [task2,task3] >> task1