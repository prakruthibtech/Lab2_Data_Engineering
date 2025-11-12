FDE LAB 2 — Building a Basic ETL Data Pipeline Using Python
Course: Foundations of Data Engineering (FDE)

Author: Prakruthi S

USN:1RVU23CSE341

🎯 Objective
This lab provides hands-on experience in building a Basic ETL (Extract, Transform, Load) data pipeline using Python.

The goal is to simulate real-world data engineering workflows — from extracting messy raw data, transforming it into a usable format, loading it into a target system, and deriving actionable business insights.

Additionally, this exercise demonstrates collaboration across data engineers, analysts, and machine learning engineers to build a data-driven solution.

🧠 Outcomes
By the end of this lab, you will be able to:

Identify and describe the stages of the data engineering lifecycle.

Explain the roles and responsibilities of different stakeholders (Data Engineer, Data Analyst, Business Analyst, ML Engineer).

Perform data ingestion, cleansing, transformation, and loading using Python.

Collaborate across simulated roles to design and implement a data-driven solution.

Apply a reverse ETL process after customer classification using machine learning.

🧰 Materials Used
sales_data_raw.csv → Raw sales data with missing values and inconsistent formats.
customer_feedback.json → Customer sentiment data from another source.
A mock data warehouse (folder structure for storing cleaned and processed data).
Python libraries:
  pandas

  numpy

  matplotlib

  scikit-learn

json
⚙️ Lab Procedure
Stage 1: Problem Definition and Requirements Gathering (Business Analyst)
Reviewed sales_data_raw.csv and customer_feedback.json.

Business Question:

“What are the top 5 products by revenue in the last quarter, and how does customer sentiment vary for these products?”

Identified required data points:

product_id, sale_price, sale_date, customer_id, sentiment_score

Created a simple requirements document summarizing the problem and desired outcome.

Stage 2: Data Ingestion and Cleansing (Data Engineer)
1.Ingestion:

  Read data from CSV and JSON files using pandas.

2.Cleansing:

Handled missing values by imputation or row removal.
Corrected data types (e.g., sale_price as float).
Standardized date formats.
3.Transformation:

Computed total_revenue = quantity * sale_price.
Joined sales and feedback data on a common key (product_id).
4.Loading:

Stored the cleaned and transformed dataset as
processed_sales_data.csv in the data_warehouse folder.
Stage 3: Data Analysis (Data Analyst)
Loaded the processed_sales_data.csv file.

Grouped data by product_id and summed total_revenue.

Calculated average sentiment_score for each top product.

Visualized results using a bar chart (matplotlib).

Identified potential data quality issues for feedback to the engineering team.

Output:

A table or bar chart showing Top 5 Products by Revenue and Average Sentiment Score.

Stage 4: Reporting and Insights (Business Analyst)
Interpretation Example:
“Product X generated the highest revenue but had below-average sentiment.

This may indicate customer dissatisfaction despite strong sales — suggesting a need for quality improvement or better customer support.”

Deliverable:
A concise final report summarizing:

The business question

Data insights

Actionable recommendations

Stage 5: Customer Classification (ML Engineer Task)
Objective:

To classify VIP customers based on purchasing behavior and update the dataset using a reverse ETL process.

Steps:

Feature Selection:
  Extracted features: customer_id, total_purchase_amount, purchase_frequency, avg_transaction_value.

2. Preprocessing:

Handled missing values
Normalized features using StandardScaler
3. Modeling:

Used K-Means Clustering to segment customers or Logistic Regression for binary VIP classification.
Labelled customers as “VIP” or “Non-VIP”.
4.Reverse ETL:

Added a new column vip_status to the dataset.
Exported the enriched dataset (enriched_sales_data.csv) to the mock CRM or data warehouse for business use.
