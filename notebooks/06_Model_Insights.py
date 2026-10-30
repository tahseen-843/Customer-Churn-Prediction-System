# Databricks notebook source
predictions = spark.table(
    "customer_churn_predictions"
)

display(predictions)

# COMMAND ----------

predictions.groupBy(
    "RiskCategory"
).count().show()

# COMMAND ----------

display(
    predictions.groupBy(
        "RiskCategory"
    ).count()
)

# COMMAND ----------

from pyspark.sql.functions import col

top_100 = predictions.orderBy(
    col("ChurnProbability").desc()
).limit(100)

display(top_100)

# COMMAND ----------

top_100.write.mode("overwrite").saveAsTable(
    "top_100_high_risk_customers"
)

# COMMAND ----------

customer_df = spark.table(
    "customer_churn_cleaned_v1"
)

# COMMAND ----------

customer_predictions = customer_df.join(
    predictions,
    on="ChurnFlag",
    how="inner"
)

# COMMAND ----------

customer_df.groupBy(
    "Contract",
    "Churn"
).count().show()

# COMMAND ----------

from pyspark.sql.functions import avg

customer_df.groupBy(
    "Contract"
).agg(
    avg("ChurnFlag").alias("ChurnRate")
).show()

# COMMAND ----------

customer_df.groupBy(
    "PaymentMethod"
).agg(
    avg("ChurnFlag").alias("ChurnRate")
).show(truncate=False)


# COMMAND ----------

customer_df.groupBy(
    "Churn"
).avg("tenure").show()

# COMMAND ----------

customer_df.groupBy(
    "Churn"
).avg("MonthlyCharges").show()

# COMMAND ----------

customer_df.groupBy(
    "InternetService"
).agg(
    avg("ChurnFlag").alias("ChurnRate")
).show()

# COMMAND ----------

customer_df.groupBy(
    "TechSupport"
).agg(
    avg("ChurnFlag").alias("ChurnRate")
).show()

# COMMAND ----------

customer_df.groupBy(
    "OnlineSecurity"
).agg(
    avg("ChurnFlag").alias("ChurnRate")
).show()

# COMMAND ----------

customer_df.groupBy(
    "SeniorCitizen"
).agg(
    avg("ChurnFlag").alias("ChurnRate")
).show()

# COMMAND ----------

from pyspark.sql.functions import avg

customer_df.groupBy("Contract") \
.agg(avg("ChurnFlag").alias("ChurnRate")) \
.orderBy("ChurnRate", ascending=False) \
.show()

# COMMAND ----------

summary = predictions.groupBy(
    "RiskCategory"
).count()

summary.show()

# COMMAND ----------

summary.write.mode("overwrite").saveAsTable(
    "executive_dashboard_summary"
)

# COMMAND ----------

