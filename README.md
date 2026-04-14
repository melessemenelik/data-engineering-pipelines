# ⚙️ Data Engineering Pipelines

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PySpark](https://img.shields.io/badge/PySpark-BigData-orange)
![Airflow](https://img.shields.io/badge/Apache-Airflow-lightblue)
![Kafka](https://img.shields.io/badge/Apache-Kafka-black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

## 🧾 Description
ETL/ELT workflows using **PySpark**, **Airflow**, and **Kafka**. Includes sample datasets and pipeline orchestration examples to demonstrate scalable data engineering practices.

## ⭐ Features
- ETL workflows with PySpark for batch processing
- ELT pipelines orchestrated with Apache Airflow
- Real‑time streaming ingestion with Kafka
- Sample datasets for reproducible demos
- Modular design for extending pipelines

## 📂 Repository Structure
## 🚀 Quickstart
Clone the repo and install dependencies:

```bash
git clone https://github.com/melessemenelik/data-engineering-pipelines.git
cd data-engineering-pipelines
pip install -r requirements.txt
python etl/pyspark_etl.py
airflow dags trigger elt_pipeline
python streaming/kafka_consumer.py
pip install -r requirements.txt
