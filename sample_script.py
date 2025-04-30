# Databricks notebook source
from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("SamplePythonScript").getOrCreate()

    # Sample data
    data = [("Alice", 29), ("Bob", 35), ("Charlie", 40)]
    columns = ["Name", "Age"]

    # Create DataFrame
    df = spark.createDataFrame(data, columns)

    # Show DataFrame
    df.show()

    # Save DataFrame as a table in Databricks
    df.write.mode("overwrite").saveAsTable("sample_table")

    print("Table 'sample_table' created successfully!")

if __name__ == "__main__":
    main()
