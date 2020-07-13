#import libraries
import time
from datetime import datetime as dt
redirect="127.0.0.1" #host
#list of websites to be blocked
websites=["www.youtube.com","youtube.com", "www.facebook.com", "facebook.com"]

while True:
    #set time
    if dt(dt.now().year,dt.now().month,dt.now().day,9,50) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9,51):

        print ("Working Hours, Permission Denied!!")
        #open text file that contains website names
        with open("website.txt",'r+') as file:
            #read website file
            content = file.read()
            #iterate through file
            for site in websites:
                if site in content: #check for website
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
        time.sleep(10)
    else:
        #open text file that contains website names
        with open("website.txt",'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
                file.truncate()
            print ("Well! You Can Use This Website.")
        time.sleep(10)
