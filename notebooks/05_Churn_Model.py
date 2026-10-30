# Databricks notebook source
ml_df = spark.table("customer_ml_dataset")


# COMMAND ----------

ml_df

# COMMAND ----------

ml_df.printSchema()

# COMMAND ----------

df = spark.table("customer_churn_cleaned_v1")

display(df)

# COMMAND ----------

from pyspark.ml.classification import LogisticRegression
2
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# COMMAND ----------

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler

# COMMAND ----------

ml_df = spark.table("customer_ml_dataset")



# COMMAND ----------

train_df, test_df = ml_df.randomSplit(
    [0.8, 0.2],
    seed=42
)

# COMMAND ----------

print("Train Rows:", train_df.count())
print("Test Rows:", test_df.count())

# COMMAND ----------

from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(
    featuresCol="features",
    labelCol="ChurnFlag"
)

# COMMAND ----------

model = lr.fit(train_df)

# COMMAND ----------

predictions = model.transform(test_df)

# COMMAND ----------

display(
    predictions.select(
        "ChurnFlag",
        "prediction",
        "probability"
    )
)

# COMMAND ----------

from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator(
    labelCol="ChurnFlag"
)

auc = evaluator.evaluate(predictions)

print("AUC Score:", auc)

# COMMAND ----------

from pyspark.sql.functions import udf, col
from pyspark.sql.types import DoubleType

def get_probability(v):
    return float(v[1])

prob_udf = udf(get_probability, DoubleType())

predictions = predictions.withColumn(
    "ChurnProbability",
    prob_udf(col("probability"))
)

# COMMAND ----------

display(
    predictions.select(
        "ChurnFlag",
        "prediction",
        "ChurnProbability"
    )
)

# COMMAND ----------

from pyspark.sql.functions import when

predictions = predictions.withColumn(
    "RiskCategory",
    when(col("ChurnProbability") >= 0.8, "High")
    .when(col("ChurnProbability") >= 0.5, "Medium")
    .otherwise("Low")
)

# COMMAND ----------

display(
    predictions.select(
        "ChurnProbability",
        "RiskCategory"
    )
)

# COMMAND ----------

predictions.groupBy(
    "RiskCategory"
).count().show()

# COMMAND ----------

predictions.write.mode("overwrite").saveAsTable(
    "customer_churn_predictions"
)

# COMMAND ----------

spark.sql("SHOW TABLES").show(truncate=False)