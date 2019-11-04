import boto3
import User_Defined_Variables as user_variable
from botocore.client import ClientError
import zipfile, os
import Cloudformation_Stack as stack


class Upload_Template_Python_Scripts:

    def upload_all_scripts(self):
        self.create_s3_bucket()
        self.upload_zip_object(user_variable.SOURCE_BUCKET, user_variable.LAMBDA_PYTHON_FILE,
                               user_variable.LAMBDA_ZIP_FILE, user_variable.LAMBDA_ZIP_FILE)
        self.upload_object(user_variable.SOURCE_BUCKET, user_variable.TEMPLATE_NAME1, user_variable.TEMPLATE_NAME1)
        self.upload_object(user_variable.SOURCE_BUCKET, user_variable.TEMPLATE_NAME2, user_variable.TEMPLATE_NAME2)
        self.upload_object(user_variable.SOURCE_BUCKET, user_variable.TEMPLATE_NAME, user_variable.TEMPLATE_NAME)


    def create_s3_bucket(self):
        try:
            user_variable.s3_client.create_bucket(Bucket='data-shwet',
                                           CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
        except ClientError:
            print("Data Bucket Already Created")

    def upload_object(self, bucket_name, real_filename, s3_filename):
        user_variable.s3_client.Object(bucket_name, s3_filename).upload_file(Filename=real_filename)

    def upload_zip_object(self, bucket_name, input_filename, output_filename, location):
        zip = zipfile.ZipFile(output_filename, "w")
        zip.write(input_filename, os.path.basename(input_filename))
        zip.close()
        self.upload_object(bucket_name, output_filename, location)
        os.remove(output_filename)

    def upload_sample_files(self):
        stacks = stack.Stack()
        status = stacks.stack_status(user_variable.STACK_NAME)
        if status == 'CREATE_COMPLETE' or status == 'UPDATE_COMPLETE':
            self.upload_object(user_variable.UPLOAD_OBJECT_BUCKET, 'Sample Data/sample1.csv', 'csv/sample1.csv')
            print("objects uploaded")
