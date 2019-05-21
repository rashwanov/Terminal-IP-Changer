import os
import sys
import time
import socks
import socket
import subprocess
import urllib2

def ipExist(ipAdd):
    if ipAdd in open('urllist.txt', 'a+').read():
        print('IP Already Exist')
    else:
        f = open('urllist.txt', 'a+')
        f.write(ipAdd)
        print ('Added NEW!!!')
    stopTor()

def checkIP():
    try:
        response = urllib2.urlopen('https://wtfismyip.com/text')
        html = response.read()
    except socks.ProxyConnectionError:
        time.sleep(5)
        checkIP
    ipExist(html)
    return html

def restartTor():
    print ("Starting TOR Service....")
    cmd = ['service','tor','restart']
    subprocess.Popen(cmd).wait()
    time.sleep(.5)

def stopTor():
    cmd = ['service', 'tor', 'stop']
    subprocess.Popen(cmd).wait()
    print ("TOR Service Stopped")

def updateIP():
    restartTor()
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9050,True)
    socket.socket=socks.socksocket
    checkIP()


updateIP()

