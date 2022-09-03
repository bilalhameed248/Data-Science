import os
import ssl
import email
import smtplib
import pymssql
import pandas as pd
from email import encoders
from jinja2 import Environment
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.utils import COMMASPACE, formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment
from email import encoders
from os.path import basename # last file name at this file
import smtplib
from datetime import date, timedelta

def Generate_Mail():
    FROM = "bilal.developer248@gmail.com"
    TO=['bilalhameed248@gmail.com']
    CC=['bilalaseer@gmail.com']
    SUBJECT="XYZ Service Down"
    #server='172.16.0.14'
    server='10.20.30.40'
    html_template=''

    html_template1= """
    <html>
    <head></head>
    <body>
    <p>Dear Team,
    <br>
    <b style="margin-left: 30px;">XYZ</b> service is down please reboot the service at your end.
    <br>
    </p>
    <p>
    THIS IS A SYSTEM GENERATED MAIL BY DATASCIENCE TEAM.
    </p>
    </body>
    </html>
    """
    try:
        html_template=html_template1
        msg=MIMEMultipart()
        part1 = MIMEText(Environment().from_string(html_template).render(), "html")
        msg.attach(part1)
        msg['From'] = FROM
        msg['To'] = COMMASPACE.join(TO)
        msg['Cc'] = COMMASPACE.join(CC)
        toAddress = TO+CC
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = SUBJECT
        msg.add_header('Content-Type','text/html')
        smtp = smtplib.SMTP(server)
        smtp.sendmail(FROM, toAddress, msg.as_string())
        smtp.close()
        print("Mail Generated Successfully")
    except Exception as e:
        print(e)
        return 0

if __name__=='__main__':
    Generate_Mail()
