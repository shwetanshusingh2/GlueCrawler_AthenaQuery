import time
import User_Defined_Variables as user_variable

class Check_Crawler():
    def crawler_status(self):
        response = user_variable.GLUE_CLIENT.get_crawler(Name='CSVCrawler')
        return response['Crawler']['State']


    def run_crawler(self):
        print("crawler started")
        time.sleep(6)
        while self.crawler_status() != 'READY':
            print("running crawler")
            time.sleep(3)
        print("crawler completed")
