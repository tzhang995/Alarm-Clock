import time
import os
import threading

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
                    #os.popen("shell=True")
                    #os.popen("${dirname}\wakemeup.mp3")
                    from pygame import mixer # Load the required library
                    mixer.init()
                    mixer.music.load('wakemeup.mp3')
                    mixer.music.play()
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
alarm.start()

try:
    while True:
         text = str(raw_input())
         if text == "stop":
            alarm.just_die()
            break
except:
    print("Yikes lets get out of here")
    alarm.just_die()
