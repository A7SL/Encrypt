import hashlib
import os
import time
import urllib
import urllib2
import re

os.system("clear")

def info():
    """ banner display """
    at = """\033[91m
   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$      
 /$$__  $$|_____ $$//$$__  $$| $$      
| $$  \ $$     /$$/| $$  \__/| $$      
| $$$$$$$$    /$$/ |  $$$$$$ | $$      
| $$__  $$   /$$/   \____  $$| $$      
| $$  | $$  /$$/    /$$  \ $$| $$      
| $$  | $$ /$$/    |  $$$$$$/| $$$$$$$$
|__/  |__/|__/      \______/ |________/
                                       
                                       
                                       







   \033[92m# Code by A7SL@SuiteZploit\033[91m                                           
          """
    print(at)


def Menu():
	os.system("clear")
	print(index)
	print("""\033[1;36m
	 1  Md5 Encrypt
""")

def main():
		x = raw_input("[ Press 1 ]>")
		if x == "--Menu":
			time.sleep(2)
			Menu()
			main()
		
	
		elif x == "1":
			os.system("clear")
			print(index)
			b = raw_input("\033[1;31m[Your Text]>")
			md5 = hashlib.md5(b.encode())
			print "Your Hash =>",md5.hexdigest()
			print ""
			main()
			
if __name__ == "__main__":
	main()
