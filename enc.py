import hashlib
import os
import time
import urllib
import urllib2
import re

os.system("clear")

index = """\033[1;31m
 █████╗ ███████╗███████╗██╗     
██╔══██╗╚════██║██╔════╝██║     
███████║    ██╔╝███████╗██║     
██╔══██║   ██╔╝ ╚════██║██║     
██║  ██║   ██║  ███████║███████╗
╚═╝  ╚═╝   ╚═╝  ╚══════╝╚══════╝                           
{#} MD5 Encrypter {#}"""

print(index)


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
