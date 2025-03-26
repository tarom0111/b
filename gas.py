# -*- coding:utf-8 -*-
# <------------! LUXINE !------------> #
import os
import re
import sys
import time
import json
import string
import requests
import random


R = "\x1b[38;5;196m"
G = "\x1b[38;5;46m"
W = "\x1b[97m"
P = "\x1b[38;5;203m"

banner = ("""\x1b[97m
{
    "DEVELOPER":"LUXINE,
    "GITHUB":"luxine-dev",
    "VERSION":"Dump File",
}
------------------------------------""")

class Main:
    def __init__(self):
        self.uid = []
        self.token = []
        self.user = []

    def clear(self):
        rj = "ahay"
        #os.system('clear')
  #  $    print(banner)

    def linex(self):
        print(f"{W}------------------------------------")

    def login(self):
        self.clear()
        try:
            print(f"")
            cookie = input(f"COOKIE :{G} ")
            self.linex()
            open("/sdcard/.cokx.txt","w").write(cookie)
            with requests.Session() as aiman:
                aiman.headers.update({'Accept-Language': 'id,en;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Origin': 'https://www.instagram.com',
                'Accept-Encoding': 'gzip, deflate'})
                response = aiman.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open("/sdcard/.tokx.txt","w").write(token)
                    print(f"TOKEN  :{G} {token}")
                    self.linex()
                    print("LOGGED IN SUCCESSFULLY")
                else:
                    print("COOKIE ERROR BRO..!")
            self.login_check()
        except Exception as e:
            print(e)
    
    def login_check(self):
        try:
            coki = open("/sdcard/.cokx.txt","r").read()
            token = open("/sdcard/.tokx.txt","r").read()
            self.token.append(token)
            try:
                response = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+self.token[0], cookies={'cookie':coki})
                datas = json.loads(response.text)
                name = datas['name']
                ids = datas['id']
                self.Menu(name,ids)
            except requests.exceptions.ConnectionError:
                sys.exit("NETWORK CONNECTION PROBLEM...")
        except IOError:
            os.system("rm -f /sdcard/.cokx.txt")
            os.system("rm -f /sdcard/.tokx.txt")
            self.login()
    
    def Menu(self,name,ids):
        self.clear()
        print(f"{W}USERNAME  : {G}{name}")
        print(f"{W}USER UID  : {G}{ids}")
        self.linex()
        print("[1] DUMP ID SIMPLE")
        print("[2] DUMP ID BRUTAL (SARANKAN)")
        print("[3] EXIT PROGRAM </>")
        self.linex()
        xxxx = input(f"{W}CHOOSE AN OPTION : ")
        if xxxx == "1":self.simple_file()
        elif xxxx == "2":self.unlimited_file()
        elif xxxx == "3":sys.exit()
        else:sys.exit("Wrong...")
    
    def simple_file(self):
        self.clear()
        try:
            coki = open("/sdcard/.cokx.txt","r").read()
            token = open("/sdcard/.tokx.txt","r").read()
        except IOError:
            print("COOKIE TOKEN NOT FOUND.LOGIN AGAIN...")
            self.login()
        print("ENTER FILE NAME : /sdcard/awm.txt")
        file_name = input("PUT FILE NAME : ")
        self.linex()
        print("PASTE ALL IDS HERE..")
        self.linex()
        while True:
            ids_all = input("")
            if ids_all == "":
                break
            try:
                uid = ids_all.split("|")[0]
            except:
                uid = ids_all
            self.user.append(uid)
            for user in self.user:
                try:
                    head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
                    if len(self.uid) == 0:
                        params = ({'access_token': token,'fields': "friends"})
                    else:
                        params = ({'access_token': token,'fields': "friends"})
                    response = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
                    try:main_rexx = response['friends']['data']
                    except:main_rexx = response['subscribers']['data']
                    for awm in main_rexx:
                        try:
                            self.uid.append(awm['id'])
                            open(file_name,"a").write(awm['id']+"|"+awm['name']+"\n")
                            tani = str(awm['id'])
                            total = len(self.uid)
                            print(f"SUCCESSFULLY DUMP FROM : {tani}|{total}")
                        except:continue
                except requests.exceptions.ConnectionError:
                    pass
            sys.exit(self.linex())
    def unlimited_file(self):
        self.clear()
        try:
            coki = open("/sdcard/.cokx.txt","r").read()
            token = open("/sdcard/.tokx.txt","r").read()
        except IOError:
            print("COOKIE TOKEN NOT FOUND.LOGIN AGAIN...")
            self.login()
        print("ENTER FILE NAME : /sdcard/awm.txt")
        ahay = random.randint(100,292)
        file_name = f"ALVINO-DUMP/DumpId{ahay}"
        file_name = input("PUT FILE NAME : ")
        self.linex()
        tls = int(input("HOW MANY IDS DO YOU WANT TO ADD? : "))
        for a in range(tls):
            self.user.append(input(f"No.{a+1} Put Ids - "))
        self.linex()
        for user in self.user:
            try:
                head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
                if len(self.uid) == 0:
                    params = ({'access_token': token,'fields': "friends"})
                else:
                    params = ({'access_token': token,'fields': "friends"})
                response = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
                try:main_rexx = response['friends']['data']
                except:main_rexx = response['subscribers']['data']
                for awm in main_rexx:
                    try:
                        self.uid.append(awm['id'])
                        open(".temp.txt","a").write(awm['id']+"\n")
                        total = len(self.uid)
                    except:continue
                print(f"XTRACT SUCCESSFUL : {user}|{total}")
            except requests.exceptions.ConnectionError:
                pass
        self.clear()
        try:filexx = open(".temp.txt","r").read().splitlines()
        except:filexx = []
        print(f"TOTAL IDS FROM DUMP : {total}")
        print(f"THE PROCESS HAS BEEN STARTED...")
        self.linex()
        for user in filexx:
            try:
                head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
                if len(self.uid) == 0:
                    params = ({'access_token': token,'fields': "friends"})
                else:
                    params = ({'access_token': token,'fields': "friends"})
                response = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':coki}).json()
                try:main_rexx = response['friends']['data']
                except:main_rexx = response['subscribers']['data']
                for awm in main_rexx:
                    try:
                        self.uid.append(awm['id'])
                        open(file_name,"a").write(awm['id']+"|"+awm['name']+"\n")
                        total = len(self.uid)
                        sys.stdout.write(f"\r\r{W}SUCCESSFUL DUMP FROM -> {user}|{G}{total}")
                        sys.stdout.flush()
                    except:continue
            except KeyError:pass
            except requests.exceptions.ConnectionError:
                pass
        sys.exit(self.linex())

if __name__ == "__main__":
    os.system("rm .temp.txt")
    Main().login_check()