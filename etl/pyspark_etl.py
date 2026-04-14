# etl/pyspark_etl.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL_Pipeline").getOrCreate()

# Extract
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Transform
df_clean = df.dropna().withColumnRenamed("value", "metric_value")

# Load
df_clean.write.mode("overwrite").parquet("data/output_data.parquet")

print("ETL pipeline completed successfully.")
