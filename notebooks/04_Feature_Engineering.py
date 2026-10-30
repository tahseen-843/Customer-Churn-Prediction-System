# Databricks notebook source
df = spark.table("customer_churn_cleaned_v1")

display(df)

# COMMAND ----------

selected_df = df.select(
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Contract",
    "PaymentMethod",
    "ChurnFlag"
)

display(selected_df)

# COMMAND ----------

from pyspark.ml.feature import StringIndexer

# COMMAND ----------

categorical_cols = [
    "gender",
    "Partner",
    "Dependents",
    "Contract",
    "PaymentMethod"
]

# COMMAND ----------

indexers = [
    StringIndexer(
        inputCol=col,
        outputCol=col+"_Index"
    )
    for col in categorical_cols
]

# COMMAND ----------

indexed_df = selected_df

for indexer in indexers:
    indexed_df = indexer.fit(indexed_df).transform(indexed_df)

display(indexed_df)

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler

# COMMAND ----------

feature_cols = [
    "gender_Index",
    "SeniorCitizen",
    "Partner_Index",
    "Dependents_Index",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Contract_Index",
    "PaymentMethod_Index"
]

# COMMAND ----------

assembler = VectorAssembler(
    inputCols=feature_cols,
    outputCol="features"
)

# COMMAND ----------

final_df = assembler.transform(indexed_df)

display(final_df.select(
    "features",
    "ChurnFlag"
))

# COMMAND ----------

ml_df = final_df.select(
    "features",
    "ChurnFlag"
)

display(ml_df)

# COMMAND ----------

train_df, test_df = ml_df.randomSplit(
    [0.8, 0.2],
    seed=42
)

# COMMAND ----------

print("Train Rows:", train_df.count())

print("Test Rows:", test_df.count())

# COMMAND ----------

ml_df.write.mode("overwrite").saveAsTable(
    "customer_ml_dataset"
)