import boto3
import User_Defined_Variables as user_variable
import Cloudformation_Stack as stack
import Upload_Data as data_upload
import Athena as athena
import Crawler_Status as crawlerstatus

class helper:

    def __init__(self):
            self.stacks = stack.Stack()
            self.upload_object = data_upload.Upload_Template_Python_Scripts()
            self.athena = athena.Athena()
            self.crawler_object = crawlerstatus.Check_Crawler()

    def run_all_scripts(self):
        self.upload_object.upload_all_scripts()
        self.stacks.create_upload_stack()
        self.upload_object.upload_sample_files()
        self.crawler_object.run_crawler()
        self.athena.athena_main()



run_script = helper()
run_script.run_all_scripts()