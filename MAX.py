import os, platform
 
try:
        import requests
        os.system("git pull")
        print('\x1b[38;5;46m Join new Facebook Group')
        os.system("xdg-open https://www.facebook.com/groups/king.official.bd/?ref=share")
        os.system('clear');print('\x1b[38;5;46m checking new update')
except:
        os.system('pip2 install requests')
import requests
bit = platform.architecture()[0]
if bit == "64bit":
        from king64 import main
        main()
elif bit == "32bit":
        from king32 import main
        main()
        
