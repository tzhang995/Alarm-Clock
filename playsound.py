import os
path = os.getcwd() + "/wakemeup.wav"
bashcmd = "paplay " + path
import subprocess
process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
