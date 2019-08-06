import requests
import json
import time

localtime = time.localtime(time.time())
timeStr= str(localtime.tm_mon) + "/" + str(localtime.tm_mday) + "/" + str(localtime.tm_year) + "   " + str(localtime.tm_hour) + ":" + str(localtime.tm_min)

def drivetime(start,end):
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?&origin='+ start +'&destination='+ end +'&departure_time=now&traffic_model=best_guess&key=GOOGLEK_KEY')
    output = r.json()
    return output["routes"][0]['legs'][0]["duration_in_traffic"]["text"]
    
f=open("/home/mitch/Documents/drivetime/drivetime.txt","a+")


f.write("\r\n"+ timeStr +",Woodlands,"+"Method,"+drivetime("The+Woodlands+TX","Method+Architecture+PLLC,+Lamar+Street"))
f.write("\r\n"+ timeStr +",Woodlands,"+"Forum,"+drivetime("The+Woodlands+TX","Forum+Energy+Technologies,+Sam+Houston+Park+Drive"))

f.write("\r\n"+ timeStr +",Pearland,"+"Method,"+drivetime("Pearland+TX","Method+Architecture+PLLC,+Lamar+Street"))
f.write("\r\n"+ timeStr +",Pearland,"+"Forum,"+drivetime("Pearland+TX","Forum+Energy+Technologies,+Sam+Houston+Park+Drive"))

f.write("\r\n"+ timeStr +",Spring,"+"Method,"+drivetime("Spring+TX","Method+Architecture+PLLC,+Lamar+Street"))
f.write("\r\n"+ timeStr +",Spring,"+"Forum,"+drivetime("Spring+TX","Forum+Energy+Technologies,+Sam+Houston+Park+Drive"))

f.write("\r\n"+ timeStr +",Humble,"+"Method,"+drivetime("Humble+TX","Method+Architecture+PLLC,+Lamar+Street"))
f.write("\r\n"+ timeStr +",Humble,"+"Forum,"+drivetime("Humble+TX","Forum+Energy+Technologies,+Sam+Houston+Park+Drive"))
