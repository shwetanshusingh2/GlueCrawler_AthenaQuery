# GlueCrawler_AthenaQuery

The aim of this project was to trigger glue crawler when there is any object upload in s3 and create catalogue in glue and query the table using athena in the same account and cross account

i have created a lambda trigger on s3 bucket and the lambda function invokes the glue crawler on any object upload event and updates the database if already created or it creates the database.athena query is run through python using boto3

the jdbc is also also configured to connect cross account database access and query the data using athena.(cross account used is sudarshan)
