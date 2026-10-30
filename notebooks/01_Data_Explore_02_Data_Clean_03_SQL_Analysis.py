# Databricks notebook source
display(dbutils.fs.ls("/"))


# COMMAND ----------

spark.sql("SHOW CATALOGS").show()

# COMMAND ----------

spark.sql("SHOW SCHEMAS").show()


# COMMAND ----------

spark.sql("SHOW TABLES").show(truncate=False)

# COMMAND ----------

df = spark.read.csv(
    "/Volumes/my_volume/default/my_volume/customer_churn.csv",
    header=True,
    inferSchema=True
)

display(df)

# COMMAND ----------

print("Total Rows:", df.count())

# COMMAND ----------

print(df.columns)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.describe().show()

# COMMAND ----------

02_Data_Cleaning

# COMMAND ----------

from pyspark.sql.functions import when, col

df = df.withColumn(
    "ChurnFlag",
    when(col("Churn") == "Yes", 1).otherwise(0)
)

display(df)

# COMMAND ----------

display(
    df.groupBy("Churn").count()
)

# COMMAND ----------

df.show(5)


# COMMAND ----------

from pyspark.sql.functions import when, col

df = df.withColumn(
    "ChurnFlag",
    when(col("Churn") == "Yes", 1).otherwise(0)
)

display(df)

# COMMAND ----------

df.groupBy("Churn").count().show()

# COMMAND ----------

from pyspark.sql.functions import avg

df.select(
    avg("MonthlyCharges")
).show()

# COMMAND ----------

df.write.mode("overwrite").saveAsTable(
    "customer_churn_cleaned"
)

# COMMAND ----------

spark.sql(
    "SELECT * FROM customer_churn_cleaned LIMIT 5"
).show()

# COMMAND ----------





# COMMAND ----------

df = spark.read.csv(
    "/Volumes/my_volume/default/my_volume/customer_churn.csv",
    header=True,
    inferSchema=True
)

display(df)

# COMMAND ----------

print("Total Records:", df.count())

# COMMAND ----------

print(df.columns)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

type(df)

# COMMAND ----------

print("Total Records:", df.count())

# COMMAND ----------

df.groupBy("Churn").count().show()

# COMMAND ----------

from pyspark.sql.functions import when, col

df = df.withColumn(
    "ChurnFlag",
    when(col("Churn") == "Yes", 1).otherwise(0)
)

df.select("customerID","Churn","ChurnFlag").show(5)

# COMMAND ----------

from pyspark.sql.functions import col, trim

df.filter(
    trim(col("TotalCharges")) == ""
).count()

# COMMAND ----------

from pyspark.sql.functions import trim

df = df.filter(
    trim(col("TotalCharges")) != ""
)

# COMMAND ----------

from pyspark.sql.functions import col

df = df.withColumn(
    "TotalCharges",
    col("TotalCharges").cast("double")
)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.describe().show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.write.mode("overwrite").saveAsTable(
    "customer_churn_cleaned_v1"
)

# COMMAND ----------

spark.sql("SHOW TABLES").show(truncate=False)

# COMMAND ----------

03_SQL_Analysis

# COMMAND ----------

df_saved = spark.table("customer_churn_cleaned_v1")

df_saved.show(5)

# COMMAND ----------

df.groupBy("Churn").count().show()

# COMMAND ----------

df.groupBy("Contract").count().show()

# COMMAND ----------

df.groupBy("Contract","Churn").count().show()

# COMMAND ----------

from pyspark.sql.functions import avg

df.groupBy("Churn") \
  .agg(avg("MonthlyCharges").alias("Avg_Monthly_Charges")) \
  .show()

# COMMAND ----------

from pyspark.sql.functions import avg

df.groupBy("Churn") \
  .agg(avg("tenure").alias("Avg_Tenure")) \
  .show()

# COMMAND ----------

display(
    df.groupBy("Contract","Churn").count()
)

# COMMAND ----------

