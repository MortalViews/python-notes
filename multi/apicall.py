import http
urls = [
    'http://xyx.com',
    'http://xyx.com/1'
    'http://xyx.com/2'
    'http://xyx.com/3'
    ]
def get_info(url): #5~15 secs
    # make http request 
    return ['dummy_data']


def write_to_disk(data,f): #5~6
    #write to file 
    pass 



for url in urls:
    data = get_info(url)
    write_to_disk(data,'xyxy')
    
    
print("DONE")