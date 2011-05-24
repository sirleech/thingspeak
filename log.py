import httplib, urllib
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time

cpu_pc = psutil.cpu_percent()
mem_avail_mb = psutil.avail_phymem()/1000000	
params = urllib.urlencode({'field1': cpu_pc, 'field2': mem_avail_mb,'key':'YOURKEYHERE'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
	
try:
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print cpu_pc
	print mem_avail_mb
	print strftime("%a, %d %b %Y %H:%M:%S", localtime())
	print response.status, response.reason
	data = response.read()
	conn.close()
except:
	print "connection failed"
