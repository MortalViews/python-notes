from  urllib import request
from threading import Thread
timeout = 20
import time 
start_time= time.time()
print('start_time',start_time)
URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/'
        ]



def download(url):
    print('donwloading:',url)
    with request.urlopen(url,timeout=timeout) as response:
        html = response.read()
        print(url,'donwloaded-len: ',len(html))
        
for url in URLS:
    download(url)

end_time = time.time()

print('end_time',end_time)
print('total_time',end_time-start_time)
print("in the end")
    
    
    
        
        