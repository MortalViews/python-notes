Database 
==========
urls 
----------------------
id url depth state 
----------------------

=======================
sqlalchemy 

2.) make http request
urllib.request.urlopen

3.)
    a.) regex 
    b.) html parser [Beautiful Soup ]

4.) 

algo:
----- 
initial:
--------
1.0)add the url from command to database and set state and PENDING and DEPTH=0
    1.) get a url with state PENDING from database 
    1a.) mark state as STARTED
    2.) make a http get request and get html 
    2a.) if error then set state to err
    3.) parse the links from the html 
    4.) convert relative links to absolute
    5.) filter our internal links 
    6.) check if link already parsed
    7.) add new links to database with proper depth
    8.) mark state as DONE
9.) continue from step 1 
