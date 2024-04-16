###
# -----------------------------------------------------------------------
# 1. Centralization and Consistency (feature reuse): Centralize
# feature management to ensure that features are consistent and
# reusable across multiple machine learning models and
# applications. This reduces duplication and pr#events discrepancies
# between training and production environments.
# -----------------------------------------------------------------------
####

# Here's how you might create and populate a feature group in AWS SageMaker Feature Store to ensure centralization:

# get data from Snowflake:
import snowflake.connector

# Snowflake connection parameters
conn = snowflake.connector.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT.snowflakecomputing.com',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

# SQL query to fetch the data
query = "SELECT * FROM your_table_name"

# Execute the query
cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()

# Convert to DataFrame
import pandas as pd
df = pd.DataFrame(rows, columns=[x[0] for x in cur.description])

# Close the cursor and connection
cur.close()
conn.close()

# Let DataTransformer be a custom class,
# enabling centralization of transformations/reversions
# facilitating interpretability, forensics, and cloud/edge consistency
from transformers import DataTransformer 

transformer = DataTransformer()
df_transformed = transformer.fit_transform(df)

my_dataframe = 

# ----- AWS Feature Store
from sagemaker.feature_store.feature_group import FeatureGroup
import sagemaker

session = sagemaker.Session()
feature_group = FeatureGroup(name='my-feature-group', sagemaker_session=session)
feature_group.load_feature_definitions(data_frame=transformed_df)  # Define schema from a DataFrame
feature_group.create(s3_uri='s3://my-bucket/my-feature-store/', record_identifier_name='record_id', event_time_feature_name='event_time')

#----- Hopsworks
from hops import featurestore

# Create a new feature group in Hopsworks Feature Store
featurestore.create_featuregroup(
    data=transformed_df,
    featuregroup_name='my_feature_group',
    description='Centralized feature group for ML models',
    version=1
)

#----- SnowFlake
#-- this is problematic because while it works on the cloud, you can’t package this tranform logic easily into a package to import into a lambda function to serve a device doing inference at the edge.
#-- Additionally, querying this table will be slower and more expensive than an S3 GET
#-- SQL to create a feature view in Snowflake
#CREATE OR REPLACE VIEW my_feature_view AS
#SELECT
#    user_id,
#    AVG(transaction_amount) AS avg_transaction_amount,
#    COUNT(DISTINCT transaction_id) AS num_transactions
#FROM
#    transactions
#GROUP BY
#    user_id;
