import subprocess

cmd = "wget "
URL = ".cce.oregonstate.edu"

printer1 = 'owen335-prn'
printer2 = 'owen-color'
p =  subprocess.Popen(cmd + printer1 + URL, shell=True )
p = subprocess.Popen(cmd + printer2 + URL, shell=True)
