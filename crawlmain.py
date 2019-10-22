# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:54:54 2019

@author: Rachel Rajan
"""

from tcpsocket import TCPsocket # from tcpsocket.py file import class TCPsocket
from urlparser import URLparser # from urlparser.py
from requests_web import Request # from requestweb.py
from queue import Queue # import Queue
import time

# define a main() function so that variables will be local to main(), instead of global
def main():
    Q = Queue()
    #print("number of urls:", Q.qsize())
    ps = URLparser() # create an url parser object
    r = Request() # create an request builder object
    ws = TCPsocket() # create a tcp socket object
    try:
        with open("URL-input-100.txt") as file:            
            for line in file:
                Q.put(line)
    except IOError:
        print('No such file')
        exit(1)
    count = 0
    while not Q.empty():
        url = Q.get()
        count += 1
        print(count) # !!! print it for debugging !!!
        print("URL: ", url) # !!! print it for debugging !!!
        host, port, path, query = ps.parse(url) # port in int, other returned values are str
        #print host, port, path, query for debugging
        print("Parsing URL... host: ", host, ", port: ", port)
        #get IP 
        ip = ws.getIP(host)
        ws.createSocket()
        ws.connect(ip, port)
        #build head request check robots.txt
        request_head = r.headRequest(host)
        #build get request
        request_get = r.getRequest(host, path, query) # host, path, query: str, request: str
        print("request: ", request_get)
        #ws.crawl(host) # host: str, port: int, request: str
        #ps.load(url)
       
        
# call main() method:
if __name__ == "__main__":
    main()