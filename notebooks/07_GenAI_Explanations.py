# Databricks notebook source
customer_df = spark.table(
    "customer_churn_cleaned_v1"
)

display(customer_df)

# COMMAND ----------

high_risk_customers = customer_df.filter(
    (customer_df.tenure < 12) &
    (customer_df.MonthlyCharges > 70) &
    (customer_df.Contract == "Month-to-month")
)

display(high_risk_customers)

# COMMAND ----------

def generate_explanation(
    tenure,
    monthly_charges,
    contract,
    tech_support
):
    
    reasons = []

    if tenure < 12:
        reasons.append(
            "short customer tenure"
        )

    if monthly_charges > 70:
        reasons.append(
            "high monthly charges"
        )

    if contract == "Month-to-month":
        reasons.append(
            "month-to-month contract"
        )

    if tech_support == "No":
        reasons.append(
            "lack of technical support"
        )

    return (
        "Customer is likely to churn due to: "
        + ", ".join(reasons)
    )

# COMMAND ----------

def generate_recommendation(
    contract,
    tech_support
):

    recommendations = []

    if contract == "Month-to-month":
        recommendations.append(
            "offer annual contract discount"
        )

    if tech_support == "No":
        recommendations.append(
            "provide free technical support"
        )

    recommendations.append(
        "offer loyalty rewards"
    )

    return (
        ", ".join(recommendations)
    )

# COMMAND ----------

print(
    generate_explanation(
        3,
        100,
        "Month-to-month",
        "No"
    )
)

# COMMAND ----------

print(
    generate_recommendation(
        "Month-to-month",
        "No"
    )
)

# COMMAND ----------

sample_customers = customer_df.select(
    "customerID",
    "tenure",
    "MonthlyCharges",
    "Contract",
    "TechSupport"
).limit(10)

display(sample_customers)