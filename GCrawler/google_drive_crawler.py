# -*- coding: utf-8 -*-
import os
import sys
import time
import string
import random
import requests
from urllib.parse import urlparse

def check(url, wait, proxy_ip, proxy_port):
    ok = False
    
    proxies = {
        'http': f'socks4://{proxy_ip}:{proxy_port}',
        'https': f'socks4://{proxy_ip}:{proxy_port}',
    }
    
    try:
        response = requests.get(url, proxies=proxies, timeout=wait)
        
        if response.status_code == 200:
            return True
        else:
            return False
        
    except: #RequestException as e:
        return False

def main():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
        
    print('''
\033[22m\033[32m             .\033[1m\033[32mZOOOOOOOOOI\033[22m\033[33m.              
\033[22m\033[32m             $$\033[1m\033[32mZOOOOOOO7\033[22m\033[33m??.             
\033[22m\033[32m           .$$$$\033[1m\033[32mZOOOOOZ\033[22m\033[33m????.            
\033[22m\033[32m           $$$$$$\033[1m\033[32mOOOO8\033[22m\033[33m??????            
\033[22m\033[32m         .O$$$$$$$\033[1m\033[32mOO8\033[22m\033[33m???????I          
\033[22m\033[32m         $$$$$$$$$$\033[1m\033[32mO\033[22m\033[33m??????????         
\033[22m\033[32m        ?$$$$$$$$$$ \033[22m\033[33m??????????+
\033[22m\033[32m       :$$$$$$$$$$   \033[22m\033[33m??????????=        
\033[22m\033[32m      .$$$$$$$$$$     \033[22m\033[33m??????????,       
\033[22m\033[32m     .$$$$$$$$$$       \033[22m\033[33m??????????.      
\033[22m\033[32m    .$$$$$$$$$$         \033[22m\033[33m??????????.     
\033[22m\033[32m    $$$$$$$$$$,.       \033[22m\033[33m..??????????.    
\033[0m\033[34m   .7777777777\033[1m\033[34m???????????\033[1m\033[31mI777777777.    
\033[0m\033[34m    777777777\033[1m\033[34m?????????????\033[1m\033[31mI77777777    
\033[0m\033[34m     Z777777\033[1m\033[34m???????????????\033[1m\033[31m777777$     
\033[0m\033[34m      $7777\033[1m\033[34m?????????????????\033[1m\033[31m77777      
\033[0m\033[34m       777\033[1m\033[34m???????????????????\033[1m\033[31m777       
\033[0m\033[34m        $\033[1m\033[34m?????????????????????\033[1m\033[31m$
         
         \033[1m\033[37mGoogle Drive Crawler
''')

    _sock4 = []
    
    #capture user input
    try:
        _list = input('Proxy list (C:\socks4.txt): ')
        
        #import proxy list
        try:
            with open(_list, "r") as f:
                for line in f:
                    if "\n" in line:
                        # remove any carriage return/s
                        line = line.replace("\n", "")
                        _sock4.append(line)
                    else:
                        _sock4.append(line)
        except:
            sys.exit('Error importing proxies! Exiting...')
        
        #integrity check
        if not _sock4:
            sys.exit('List appears empty! Exiting...')
        
        _time = int(input('Timeout sec. (1=default): '))
        
        input('\r\nReady? Strike <ENTER> to crawl and <CTRL+C> to abort...\r\n')
        
    except KeyboardInterrupt:
        sys.exit()
    except:
        main()
        
    #begin scan
    try:
        while True:

            print('Now checking...')
            
            #generate url
            query = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(33))
            url = 'https://drive.google.com/drive/folders/' + query
        
            #select proxy
            proxy = random.choice(_sock4)
            ip, port = proxy.split(":")
        
            valid = check(url, _time, ip, port)
            
            if valid:
                print('----> FOUND @ ' + url)
                
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        pass
    except:
        pass
        
    sys.exit('\r\nDone!\r\n')
  
if __name__ == '__main__':
    main()
