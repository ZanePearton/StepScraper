#import text
from cgitb import text
#import requests
import requests;
#import sleep
from time import sleep
#min Count 
count = 0; 
#max count 
max_count = 50; 
#while true do the following 
while True:
    #inscrements of 50
    count += 50
    #count concat with str
    URL = "https://www.steptember.org.au/funraisin/viewlump/4688?offset=";
    #sleep 1 second 
    sleep (1);
    #concat url with path
    con_url = (URL + str (count)); 
    #print path
    print (con_url)
    #send request
    r = requests.get(con_url);
    # print (r.text)
    output = str (r.text);
    # str output = (r.text);
    with open('Steptember.html', 'w') as f:
        #write 
        f.write(output)

    #break
    if count >= max_count:
        #exceeds max count break
        break
    print ("complete")