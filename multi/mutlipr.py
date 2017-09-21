from  urllib import request
from multiprocessing import Process
timeout = 60
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
    s = time.time()
    with request.urlopen(url,timeout=timeout) as response:
        html = response.read()
        print(url,len(html))
        print("IN",time.time()-s)
threads = []      
for url in URLS:
    t = Process(target=download,kwargs={'url':url})
    t.start()
    threads.append(t)

for t in threads:    
    t.join()

end_time = time.time()

print('end_time',end_time)
print('total_time',end_time-start_time)
print("in the end")
    
    
    
        
        