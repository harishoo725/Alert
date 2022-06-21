import sendgrid
from elasticsearch import Elasticsearch
import time
mail = sendgrid.SendGridAPIClient('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')

esconnector = Elasticsearch(
    "http://10.101.60.86:32315/")
    

message = sendgrid.Mail(
                from_email='harinath.kavuri@gmail.com',
                to_emails='anandsadhu@perigorddata.com',
                subject='PM Elastic DB Down',
                html_content='<strong>Elastic DB Down</strong>')

#response = client1.send(message)

while True:
    time.sleep(10)
    try:
        esconnector.info()
        print("Connected")
        continue    
    except:
        print("Error an expectional")
        response = mail.send(message)
        break