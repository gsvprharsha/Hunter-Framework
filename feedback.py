import smtplib
import subprocess
import os
import filetype
import imghdr
from email.message import EmailMessage
from termcolor import colored

def send_email():
    host_email = str(input("Your Email ID: "))
    host_password = str(input("Your Email Password: "))
    target_email = "lgion7611@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = str(input("Subject: "))
    msg['From'] = host_email
    msg['To'] = target_email
    msg.set_content(input("Body: "))
    