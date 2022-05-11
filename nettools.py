#nettool.py
#Created 11.04.2022 by Harry Witriyono, Fajar Dwi Atmoko, Fajar Tirtayasa, Farid Adam Abdillah
#========================================================================
#Acknowledgment : Mr. Dodi Permana Hidayat as Our Python Lecturer
#========================================================================
import os
def clearscreen():
 if os.name != 'nt':
  os.system("clear") # Linux - OSX clear the screen
 else:
  os.system("cls") # Windows
def mainmenu():
 clearscreen()
 print("Simple Network Tools")
 print("V.1.0.2022")
 print("Made by Python Group F:")
 print("Harry Witriyono, Fajar Dwi Atmoko, Fajar Tirtayasa, Farid Adam Abdillah")
 print("##################################")
 print("Please enter your selection : ")
 print("[A] find out the corresponding IP address or domain name system (DNS) record")
 print("[B] test and verify a particular destination IP address")
 print("[C] cek your IP configuration")
 print("[D] Displays protocol statistics and current TCP/IP network connections")
 print("[E] cek web app vulnerabilties")
 print("[F] Use netsh for network configuration")
 print("[G] Backup database MySQL")
 print("[H] System Information for network configuration")
 print("[I] Address Resolution Protocol")
 print("[J] See IP routing table")
 print("[X] Exit")
 print("##################################")
pil=''
while pil.upper() != 'X':
 mainmenu()
 pil=input("Your selection : ")
 if pil.upper()=="A":
  namadomain=str(input("Enter the host name : "))
  command="nslookup "+namadomain
  print("Find out the corresponding IP address or DNS...:\n")
  if namadomain=="":
   print("Type exit to end the terminal")
  os.system(command)
## end of A option #################################
 if pil.upper()=="B":
  url=str(input("Enter the URL to test for : "))
  command="ping "+url
  print("Packet test to the ",url," .... \n")
  os.system(command)
## end of B option #################################
 if pil.upper()=="C":
  if os.name=='nt':
   command="ipconfig"
  else:
   command="ifconfig /all"
  os.system(command)
## end of C option #################################
 if pil.upper()=="D":
  command="netstat"
  os.system(command)
## end of D option #################################
 if pil.upper()=="E":
  namaapp=str(input("Please type the url that you want to check : "))
  sqlmapfolder=str(input("Please type your default sqlmap app (i.e:d:\sqlmap)\n:"))
  if sqlmapfolder== "": 
   command="python d:\sqlmap\sqlmap.py -u "+namaapp+" --forms -batch  --level=5 --random-agent --forms"
  else:
   command="python "+sqlmapfolder+"\sqlmap.py -u "+namaapp+" --forms -batch --level=5 --random-agent --forms"
  os.system(command)
## end of E option #################################
 if pil.upper() =="F":
  if os.name == "nt":
   os.system("netsh")
  else:
   print("Sorry, this command only in Windows Operating System.")
## end of F option #################################
 if pil.upper() =="G":
  pathmsyqldump=str(input("Ketik lokasi file mysqldump (default: c:\\xampp\\mysql\\bin\\): "))
  if pathmsyqldump=="":
   pathmsyqldump="c:\\xampp\\mysql\\bin\\"
  namahost=str(input("Enter the host name (default: localhost): "))
  if namahost=="":
   namahost=""
  else:
   namahost=" -h"+namahost
  namauser=str(input("Enter username for server MySQL (default: root): "))
  if namauser=="":
   namauser="root"
  namadatabase=str(input("Enter database name : "))
  if namadatabase=="":
   print("You must enter database name !")
   input("\nPress any keys to continue..")
   break
  namabackupdb=str(input("Enter backup database name : "))
  if namabackupdb =="":
   print("You must enter backup database name !")
   input("\nPress any keys to continue..")
   break
  import getpass
  passwordnya=getpass.getpass()
  if passwordnya=='':
   passwordnya=' '
  else:
   passwordnya=" -p"+passwordnya   
  perintah= pathmsyqldump+"mysqldump -u"+namauser+passwordnya+namahost+" "+namadatabase+" > "+namabackupdb
  os.system(perintah)
  if os.name == "nt":
   perintah="dir "+namabackupdb
  else:
   perintah="ls "+namabackupdb
  os.system(perintah)
## end of G option #################################
 if pil.upper() =="H":
  if os.name == "nt":
   os.system("systeminfo")
  else:
   print("Sorry, this command only in Windows Operating System.")
## end of H option #################################
 if pil.upper() == "I":
  os.system("arp -a")
 if pil.upper() == "J":
  if os.name=="nt":
    os.system("route print")
  else:
    os.system("route")
 if pil.upper() !='X':
  input("\nPress any keys to continue..")
## end while loop chek pil key
clearscreen()