import time
import os
import threading
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweetfu(name,filename):
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "agvZ0kTe9Se820jwrk3J2EfMu",
    "consumer_secret"     : "5aYEdm1QUoiGh4K6QaJUdqjsHbbqXsI0F4LlqbL0IH55E3qXBi",
    "access_token"        : "3862358111-bKBdQtb80BUAqFJz0Le3MZbgYq1zVTTaaBvkBXx",
    "access_token_secret" : "kG3yWxBBT7Tx6DytUD0Shlz5mXI1nBjdEgh2UwuW88Xnh" 
    }

  api = get_api(cfg)
  tweet = "@" + name + " failed to stop the alarm!\n Now " + filename + "will be DELETED!!!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing


from random import randint
b=randint(0,100)
home = os.path.expanduser('~')

def threat(name):
    print("If you don't wake-up, a random file will be GONE")
    print("And you will be shamed")
    #bashcmd = "len=`find ~ | wc -l`"
    #bashcmd2 = "$(( ( RANDOM % $len )  + 1 ))"
    import subprocess
    process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    process2 = subprocess.Popen(bashcmd2.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

def printfile(name):
    #threading.Timer(10.0, printfile).start()
    filename="butts"
    fullfilename=""
    ifdone=False
    for path, subdirs, files in os.walk(home):
        for name in files:
            from random import randint
            a=randint(0,100)
            if a==b:
                fullfilename=os.path.join(path, name)
                filename=name
                ifdone=True
                break
        if ifdone:
            break
    print(filename)
    tweetfu(name,filename)
    #os.remove(fullfilename)
 

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("WAKEY-WAKEY!")
                    threat(name)
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False

name = raw_input("Enter your twitter handle: @")

print("Hello, " + name)

alarm_HH = input("Enter the hour you want to wake up at: ")
alarm_MM = input("Enter the minute you want to wake up at: ")

print("You want to wake up at: {0:02}:{1:02}").format(alarm_HH, alarm_MM)


alarm = Alarm(alarm_HH, alarm_MM)
alarm.run()
printfile(name)
while True:
    text = str(raw_input())
    if text == "stop":
        alarm.just_die()
        exit

