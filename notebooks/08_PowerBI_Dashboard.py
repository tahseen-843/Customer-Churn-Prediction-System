# Databricks notebook source
# MAGIC %md
# MAGIC ## Objective
# MAGIC
# MAGIC The purpose of this dashboard is to visualize customer churn trends,
# MAGIC
# MAGIC high-risk customers, churn drivers, and retention recommendations.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## KPIs
# MAGIC
# MAGIC - Total Customers
# MAGIC
# MAGIC - Churned Customers
# MAGIC
# MAGIC - Churn Rate %
# MAGIC
# MAGIC - High-Risk Customers
# MAGIC
# MAGIC - Model AUC Score
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dashboard Pages
# MAGIC
# MAGIC ### Page 1: Executive Overview
# MAGIC
# MAGIC - Total Customers
# MAGIC
# MAGIC - Churn Rate
# MAGIC
# MAGIC - High-Risk Customers
# MAGIC
# MAGIC - Model Performance
# MAGIC
# MAGIC ### Page 2: Churn Analysis
# MAGIC
# MAGIC - Churn by Contract Type
# MAGIC
# MAGIC - Churn by Payment Method
# MAGIC
# MAGIC - Risk Category Distribution
# MAGIC
# MAGIC ### Page 3: Customer Behavior
# MAGIC
# MAGIC - Monthly Charges vs Churn
# MAGIC
# MAGIC - Tenure vs Churn
# MAGIC
# MAGIC - Tech Support Analysis
# MAGIC
# MAGIC ### Page 4: High-Risk Customers
# MAGIC
# MAGIC - Top 100 High-Risk Customers
# MAGIC
# MAGIC ### Page 5: AI Recommendations
# MAGIC
# MAGIC - Churn Reasons
# MAGIC
# MAGIC - Retention Recommendations

# COMMAND ----------

# MAGIC %md
# MAGIC ## Key Findings
# MAGIC
# MAGIC 1. Month-to-Month customers have the highest churn rate.
# MAGIC
# MAGIC 2. Customers with lower tenure are more likely to churn.
# MAGIC
# MAGIC 3. Higher monthly charges are associated with higher churn.
# MAGIC
# MAGIC 4. Customers without Tech Support show increased churn risk.
# MAGIC
# MAGIC 5. Electronic Check payment method shows higher churn behavior.
# MAGIC
# MAGIC 6. The model achieved an AUC score of 0.838.
# MAGIC Show more lines

# COMMAND ----------

# MAGIC %md
# MAGIC ## Business Value
# MAGIC
# MAGIC - Identify customers likely to churn.
# MAGIC
# MAGIC - Support retention campaigns.
# MAGIC
# MAGIC - Reduce customer loss.
# MAGIC
# MAGIC - Improve revenue retention.
# MAGIC
# MAGIC - Enable data-driven decision making.