import os, sys, time

os.system('clear')

username = 'kenzo'      
password = '1945'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("\033[1;92musername : ")
	if uname == username:
		pwd = raw_input("\033[1;92mpassword : ")

		if pwd == password:
		 	os.system('clear')
			

		else:
			restart()

	else:
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()