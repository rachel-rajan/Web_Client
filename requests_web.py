# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

class Request:
    """Build HTTP requests """
    
    def __init__(self):
        self.request = '' # instance variable, unique to each instance
    def getRequest(self, host, path, query):
        """Build an HTTP GET request """
        self.request = 'GET /'+ path +query+ ' HTTP/1.1\r\nHost: ' + host + '\r\nConnection: close\r\n\r\n';
        return self.request
    
    def headRequest(self, host):
        
        """Build a HEAD request, to check if host has "robots.txt" file """
        self.request = 'HEAD /robots.txt HTTP/1.0\n' + 'Host: ' + host + '\n\n'
        
        return self.request
    
       