import requests
import json
import time

localtime = time.localtime(time.time())
timeStr= str(localtime.tm_mon) + "/" + str(localtime.tm_mday) + "/" + str(localtime.tm_year) + "   " + str(localtime.tm_hour) + ":" + str(localtime.tm_min)

def drivetime(start,end):
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?&origin='+ start +'&destination='+ end +'&departure_time=now&traffic_model=best_guess&key=AIzaSyApmMEineEE6edY-mm3wYjgcZ3vqXvi_A0')
    output = r.json()
    return output["routes"][0]['legs'][0]["duration_in_traffic"]["text"]
    
f=open("/home/mitch/Documents/drivetime/drivetime.txt","a+")
f.write("\r\n"+ timeStr +"  The Woodlands TX   to  "+"Method Architecture PLLC, Lamar Street   "+drivetime("The+Woodlands+TX","Method+Architecture+PLLC,+Lamar+Street"))
f.write("\r\n"+ timeStr +"  The Woodlands TX   to  "+"Forum Energy Technologies, Sam Houston Park Drive   "+drivetime("The+Woodlands+TX","Forum+Energy+Technologies,+Sam+Houston+Park+Drive"))
f.write("\r\n"+ timeStr +"  Method Architecture PLLC, Lamar Street   to	"+"The Woodlands TX   "+drivetime("Method+Architecture+PLLC,+Lamar+Street","The+Woodlands+TX"))
f.write("\r\n"+ timeStr +"  Forum Energy Technologies, Sam Houston Park Drive   to	"+"The Woodlands TX   "+drivetime("Forum+Energy+Technologies,+Sam+Houston+Park+Drive","The+Woodlands+TX"))
