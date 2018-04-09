from bs4 import BeautifulSoup
import re
import json
import urllib
import requests
import os

def ipvuln():
	soup = BeautifulSoup(open('security.htm').read(),'html.parser')
	print("You have active sessions at the following locations:",file=f)
	for item in soup.find(class_='contents').find('ul').find_all(class_='meta'):
		ip = item.find('br').findNext('br').next_sibling[12:]
		query = requests.get('http://ipinfo.io/'+ip).json()
	
		ip=query['ip']
		org=query['org']
		city = query['city']
		country=query['country']
		region=query['region']
		loc=query['loc']

		time = item.find('br').previous_sibling[9:]

		print('ip: {}\ncity: {}\nregion: {}\ncountry: {}\nloc: {}\norg: {}\ncreated time: {}\n'\
			.format(ip,city,region,country,loc,org,time),file=f)
	print("If any of these locations seem unusual, log out of those sessions and change your login info immediately.",file=f)

def advuln():
	soup = BeautifulSoup(open('ads.htm').read(),'html.parser')
	count = 0
	print("The following advertisers possess your contact information:",file=f)
	for item in soup.find(class_='contents').find('ul').findNext('ul').findNext('ul').find_all('li'):
		print(item.text,file=f)
		count += 1
	print("\nA total of "+str(count)+" advertisers have your contact info. Remove any advertisers"+\
		" you do not trust with such information.",file=f)

def appvuln():
	soup = BeautifulSoup(open('apps.htm').read(),'html.parser')
	count = 0
	print("You have installed the following apps:",file=f)
	for item in soup.find(class_='contents').find('ul').find_all('li'):
		print(item.text,file=f)
		count += 1
	print("\nYou have installed "+str(count)+" apps, permissions of which can vary from possessing profile info"+\
		" to posting on your timeline. It is recommended to uninstall any apps whose services you do not find necessary.\n",file=f)


if __name__ == "__main__":
	pright = False
	f = open('out.txt','w')
	path = input("Enter filepath of your downloaded Facebook data, for example ~/Documents/facebook-michaeltang:\n").strip()
	while not pright:
		try:
			os.chdir(path+'/html')
			pright = True
		except:
			path = input("Invalid path, please try again:\n")
	print("-------------------------------\nLooking for active session vulnerabilities:\n",file=f)
	ipvuln()
	print("\n-------------------------------\nLooking for ad contact vulnerabilities:\n",file=f)
	advuln()
	print("\n-------------------------------\nLooking for app login vulnerabilities:\n",file=f)
	appvuln()
	f.close()