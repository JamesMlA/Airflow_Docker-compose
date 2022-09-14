from datetime import datetime, timedelta


from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import (
    S3CopyObjectOperator,
    S3CreateBucketOperator,
    S3CreateObjectOperator,
    S3DeleteBucketOperator,
    S3DeleteBucketTaggingOperator,
    S3DeleteObjectsOperator,
    S3FileTransformOperator,
    S3GetBucketTaggingOperator,
    S3ListOperator,
    S3ListPrefixesOperator,
    S3PutBucketTaggingOperator,
)
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor, S3KeysUnchangedSensor


default_args = {
    'owner': 'ancordss',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

with DAG(
    dag_id='dag_with_minios_s3_v01',
    start_date=datetime(2023,3,12),
    schedule_interval='@daily',
    default_args=default_args


) as dag:
    task1= S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minio_conn',
        mode='poke',
        poke_interval=5,
        timeout=30
    )

    