import boto3
from botocore.client import ClientError

# client_glue.start_crawler(Name='CSVCrawler')

client_glue = boto3.client('glue')
def handler(event, context):
  client_glue.start_crawler(Name='CSVCrawler')




