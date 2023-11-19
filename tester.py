import snowflake.connector

# Replace with your Snowflake account details
conn = snowflake.connector.connect(
    user='mishka',
    password='TurboTurd1002',
    account='oadbdrg-eqa12001.snowflakecomputing.com',
    warehouse='your_warehouse',
    database='azure',
    schema='public'
)
