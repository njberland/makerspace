# code to connect to wifi and sync time 

import time
import network
import ntptime

wlan = network.WLAN(network.STA_IF) # create station interface                                                                               
wlan.active(True)       # activate the interface                                                                                             
aps = wlan.scan()             # scan for access points                                                                                       
print(aps)
wlan.connect('LinksysMakers', 'hemmelig') # connect to an AP                                                                                 
wlan.config('mac')      # get the interface's MAC address                                                                                    
wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses                                                                    

time.sleep(5)

if (wlan.isconnected()):      # check if the station is connected to an AP                                                                   
    print("Online")
else:
    print("offline")

try:
  print("Local time before synchronization：%s" %str(time.localtime()))
  #make sure to have internet connection                                                                                                     
  ntptime.settime()
  print("Local time after synchronization：%s" %str(time.localtime()))
except:
  print("Error syncing time")
