import requests
import json
import time

localtime = time.localtime(time.time())
timeStr= str(localtime.tm_mon) + "/" + str(localtime.tm_mday) + "/" + str(localtime.tm_year) + "   " + str(localtime.tm_hour) + ":" + str(localtime.tm_min)

def drivetime(start,end):
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?&origin='+ start +'&destination='+ end +'&departure_time=now&traffic_model=best_guess&key=AIzaSyApmMEineEE6edY-mm3wYjgcZ3vqXvi_A0')
    output = r.json()
    return output["routes"][0]['legs'][0]["duration_in_traffic"]["text"]
    
f=open("/home/mitchaheim/drivetime/drivetime.txt","a+")

f.write("\r\n"+ timeStr +",Method,"+"Woodlands,"+drivetime("Method+Architecture+PLLC,+Lamar+Street","The+Woodlands+TX"))
f.write("\r\n"+ timeStr +",Forum,"+"Woodlands,"+drivetime("Forum+Energy+Technologies,+Sam+Houston+Park+Drive","The+Woodlands+TX"))

f.write("\r\n"+ timeStr +",Method,"+"Pearland,"+drivetime("Method+Architecture+PLLC,+Lamar+Street","Pearland+TX"))
f.write("\r\n"+ timeStr +",Forum,"+"Pearland,"+drivetime("Forum+Energy+Technologies,+Sam+Houston+Park+Drive","Pearland+TX"))


f.write("\r\n"+ timeStr +",Method,"+"Spring,"+drivetime("Method+Architecture+PLLC,+Lamar+Street","Spring+TX"))
f.write("\r\n"+ timeStr +",Forum,"+"Spring,"+drivetime("Forum+Energy+Technologies,+Sam+Houston+Park+Drive","Spring+TX"))

f.write("\r\n"+ timeStr +",Method,"+"Humble,"+drivetime("Method+Architecture+PLLC,+Lamar+Street","Humble+TX"))
f.write("\r\n"+ timeStr +",Forum,"+"Humble,"+drivetime("Forum+Energy+Technologies,+Sam+Houston+Park+Drive","Humble+TX"))
