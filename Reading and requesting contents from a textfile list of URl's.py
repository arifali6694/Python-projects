"""
Here is my code to pull contents of several webpages/urls in stored a local text file  named "urilist2.txt"
The output shows all the websites visited from "urilist2.txt" , if the websites respond then it says 'website works' and takes a text snippet of the page else it moves to the next URI. If the website request leads to an error then inforamtion on the type of error will be returned , i.e detailing if its a network connection or http server error.
"""

#https://docs.python.org/3/howto/urllib2.html#fetching-urls
import urllib.request
f = open("urilist2.txt") #open the uri text file
for line in f.readlines(): 
    j = line.strip()
    req = urllib.request.Request(j) # request object for url I want to fetch, req object represents my http request. 
    
    try: 
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:  # URLError deals with network connection eerors 
        print( j )  # e.reason  gives type of error code if required but we just need the link.
    else:
        print ( 'website works',response.read(30), j ) # a snippet of the page that works.
        
'''   
an extra http error excepetion which can be used.
    except urllib.error.HTTPError as e: # HTTPError deals with server http response erorrs 
        print(e.code, e.read(30), j) # gives type of  http error code and a snippet of the page.
  
    
    '''     
    
        
               
''' with urllib.request.urlopen(req) as response: # # This response is a file-like object, which means you can for example call .read() on the response:
    print( response.read())
    '''
    
    """ 
Sample input :
    
http://allindiTapoint.com/links/arts-theatre.html
http://simlockservis.fCr.pl/simlock-nokia_8146.html
http://cheaphotelflVight.hu/europe/italy/posada/hotel_donatella.html
http://test.fromanywhYere.hu/common/pseudoscript/common.html
http://selladena.ucKoz.ru/forum/7-88-1
http://www.carefreeazhomesyastems.hu/MYlzBA__.dat
....

Sample output:

http://allindiTapoint.com/links/arts-theatre.html
website works b'<!DOCTYPE html>\r\n<html lang="p' http://simlockservis.fCr.pl/simlock-nokia_8146.html
http://cheaphotelflVight.hu/europe/italy/posada/hotel_donatella.html
http://test.fromanywhYere.hu/common/pseudoscript/common.html
website works b'<!DOCTYPE html><html data-adbl' http://selladena.ucKoz.ru/forum/7-88-1
http://www.carefreeazhomesyastems.hu/MYlzBA__.dat
....
we can see the websites working from this sample list 
"""
