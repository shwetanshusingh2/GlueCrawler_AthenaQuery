import boto3
import csv
import os
import pandas as pd
import io
import time
import User_Defined_Variables as user_variable


class Athena:

    # this function runs the query in athena in same account
    def run_query(self, query, database, s3_output):
        response2 = user_variable.ATHENA_CLIENT.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': database
            },
            ResultConfiguration={
                'OutputLocation': s3_output,
            }
        )
        print('Execution ID: ' + response2['QueryExecutionId'])
        s3_key = response2['QueryExecutionId']
        query_status = None
        while query_status == 'QUEUED' or query_status == 'RUNNING' or query_status is None:
            query_status = \
                user_variable.ATHENA_CLIENT.get_query_execution(QueryExecutionId=response2["QueryExecutionId"])[
                    'QueryExecution']['Status']['State']
            print(query_status)
            if query_status == 'FAILED' or query_status == 'CANCELLED':
                raise Exception('Athena query with the string "{}" failed or was cancelled'.format(query))
            time.sleep(4)
        print('Query "{}" finished.'.format(query))
        return self.read_file(s3_key)

    # this function converts the csv stored in s3 bucket to pandads dataframe and prints it
    def read_file(self, s3_key):
        try:
            print('output/' + s3_key + '.csv')
            response1 = user_variable.s3_client \
                .Bucket('shwet2') \
                .Object(key='output/' + s3_key + '.csv') \
                .get()
            return pd.read_csv(io.BytesIO(response1['Body'].read()), encoding='utf8')
        except Exception as e:
            print(e)

    def athena_main(self):
        res = self.run_query(user_variable.QUERY, user_variable.DATABASE, user_variable.S3_OUTPUT)
        # res=read_file()
        print(res)