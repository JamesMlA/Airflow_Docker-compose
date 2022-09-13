FROM apache/airflow:2.3.4 AS airflow

USER root

RUN apt-get update
# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

# install Git

RUN apt-get -y install git

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/"
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# configure liquibase
COPY /resources .
ENV PATH="${PATH}:/opt/airflow/liquibase"



COPY . . 
