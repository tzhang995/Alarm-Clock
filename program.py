#Requires Tweepy and a linux machine with either ALSA or PulseAudio

import time
import os
import threading
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweetfu(name,filename):
  cfg = { 
    "consumer_key"        : "REDACTED",
    "consumer_secret"     : "REDACTED",
    "access_token"        : "REDACTED",
    "access_token_secret" : "REDACTED" 
    }

  api = get_api(cfg)
  tweet = "@" + name + " failed to stop the alarm!\nNow random file:" + filename + " will be DELETED!!!"
  try:
    status = api.update_status(status=tweet) 
  except:
    print("Error tweeting") 

from random import randint
b=randint(0,100)
home = os.path.expanduser('~')

def playmusic():
    selection = randint(0,1)
    songname = ""
    if selection:
        songname = "wakemeup"
    else:
        songname = "sheep"
    import subprocess
    try:
        bashcmd = "paplay " + os.getcwd() + "/" + songname + ".wav"
        process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
    except:
        bashcmd = "aplay " + os.getcwd() + "/" + songname + ".wav"
        process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)

def warning(name):
    playmusic()
    print("If you don't terminate the program, a random file will be GONE")
    print("And you will be shamed on twitter")
    threading.Timer(21.0, punish, args=[name]).start()

def punish(name):
    printfile(name)
    playmusic()
    threading.Timer(21.0, punish, args=[name]).start()

def printfile(myname):
    filename="butts"
    fullfilename=""
    ifdone=False
    home = os.path.expanduser('~')
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
    tweetfu(myname,filename)
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
                    warning(name)
                    return
            #time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False

name = raw_input("Enter your twitter handle: @")

print("Hello, " + name)

alarm_HH = input("Set the alarm hour in 24 hour format: ")
alarm_MM = input("How many minutes after the hour?: ")

print("You want to wake up at: {0:02}:{1:02}").format(alarm_HH, alarm_MM)

alarm = Alarm(alarm_HH, alarm_MM)
alarm.run()
while True:
    text = str(raw_input())
    if text == "stop":
        alarm.just_die()
        exit
