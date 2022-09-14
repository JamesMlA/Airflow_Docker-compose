from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'Ancordss',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='this is out first dag that we write',
    start_date=datetime(2022,7,29,2),
    schedule_interval='@daily'
) as dag:
    task1=BashOperator(
        task_id='firs_task',
        bash_command='echo hello world, this is the first task'

    )

    task2=BashOperator(
        task_id='second_task',
        bash_command='echo this is the second task and i will be running after the fisrt task'
         )

    task3=BashOperator(
        task_id='third_task',
        bash_command='echo hey im task 3 and will be running after task1 at the same time as task 2'
        )
    #task dependecy method 1
   # task1.set_downstream(task2)
   # task1.set_downstream(task3)

   # task dependency method2
    # task1 >> task2
    # task1 >> task3

    #task dependecy method 3

    task1 >> [task2,task3]
