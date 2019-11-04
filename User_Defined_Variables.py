import boto3
import User_Defined_Variables as user_variable
import Cloudformation_Stack as stack
import Upload_Data as data_upload
import Athena as athena
import Crawler_Status as crawlerstatus

s3_client = boto3.resource('s3')
SOURCE_BUCKET = "data-shwet"
TEMPLATE_NAME = "template.yaml"
TEMPLATE_NAME1 = "security.yaml"
TEMPLATE_NAME2 = "resources.yaml"
LAMBDA_PYTHON_FILE = "lambda_trigger.py"
LAMBDA_ZIP_FILE = "lambda_trigger.zip"
STACK_NAME = "stack2"
lambda_version = ""
CLIENT = boto3.client('cloudformation')
UPLOAD_OBJECT_BUCKET = "shwet23"
TEMPLATE_URL = 'https://data-shwet.s3.ap-south-1.amazonaws.com/template.yaml'
GLUE_CLIENT = boto3.client('glue')
ATHENA_CLIENT = boto3.client('athena')
S3_OUTPUT = 's3://shwet2/output'
DATABASE = 'dbcrawler'
QUERY = 'SELECT * FROM "dbcrawler"."csv" limit 10'
