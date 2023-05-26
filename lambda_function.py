import json
import boto3

rds_client = boto3.client('rds-data')

database_name = ''
db_cluster_arn = ''
db_credentials_secrets_store_arn = ''

def lambda_handler(event, context):
    response = execute_statement('SELECT * FROM serverless.Customers');
    return response['records'];

def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_store_arn,
        database=database_name,
        resourceArn=db_cluster_arn,
        sql=sql
    )
    return response;