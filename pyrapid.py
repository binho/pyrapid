# -*- coding: utf-8 -*-
'''
	Download multiple files from rapidshare.com using premium account
	Created by Cleber Santos
	binho.net - cleberwillian@gmail.com
	
	Usage:
		Configure urls.txt with urls to download and run "python pyrapid.py" without quotes.
'''
import os
import time

# username and password for rapid share premium account
username = 'cleber.santos'
password = 'n70nokia'

# current directory
dir = os.getcwd()

# load or create
log = open('history', 'w+')

# remove old cookies
if os.path.isfile( dir + '/rs_cookie' ):
	os.remove( dir + '/rs_cookie' )

# save local rapid share cookie
print >>log, time.strftime('%d/%m/%y %H:%M:%S') + ' --- downloading cookie from rapid share...'
os.system('wget --no-check-certificate --save-cookies ' + dir + '/rs_cookie --post-data "login=' + username + '&password=' + password + '" -O - https://ssl.rapidshare.com/cgi-bin/premiumzone.cgi > /dev/null')

# get urls (one per line) from urls.txt
urls = open('urls.txt', 'r')

for url in urls.readlines():
	print >>log, time.strftime('%d/%m/%y %H:%M:%S') + ' --- downloading file '+url+' please wait...'
	os.system( 'wget -c --load-cookies ' + dir + '/rs_cookie ' + url )
	print >>log, time.strftime('%d/%m/%y %H:%M:%S') + ' --- waiting 3 seconds to download next file...'
	time.sleep(3)

urls.close()

print >>log, time.strftime('%d/%m/%y %H:%M:%S') + ' --- all files downloaded! done!'
