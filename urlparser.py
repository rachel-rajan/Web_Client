# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:42:09 2019

@author: Rachel Rajan
"""
import time
#from parsel import Selector
#import urllib.request
#from bs4 import BeautifulSoup


class URLparser:
    
    def parse(self, string): # string is a url
#        start = time.time()
#        response = urllib.request.urlopen(string)
#        response_soup= BeautifulSoup(response, 'html.parser')
#        href_links= response_soup.findAll('a')
        
       
        self.query = '' # default query is an empty string
        self.path = '/' # default path
        self.port = '80' # default port
        self.host = '' # host is always defined for valid URLs
        string = string[:-1] # remove line break that is in the end of one line!!!
        # remove 'http://' or 'https://' if it is present in the URL given
        if string[:7] == 'http://':
            string = string[7:]
        elif string[:8] == 'https://':
            string = string[8:]
        # remove fragment from url
        index = string.find('#')
        if index != -1: # if it found a fragment
            string = string[:index] # strip fragment
        # remove user:pass@ if exists
        
        # get query first, remove query from url
        index = string.find('?')
        if index != -1: # if found a query
            self.query = string[index:] # get the query
            string = string[:index] # remove the query from the string
        # get path next, remove path from url
        index = string.find('/')
        if index != -1: # if found a path
            self.path = string[index:]
            string = string[:index] # remove the path
        # get port
        index = string.find(':') 
        if index != -1: # if found a query
            self.port = string[index:] # get the port
            string = string[:index] # remove the port from the string
        # get host
        self.host = string.split("//")[-1].split("/")[0].split('?')[0] # get the host
            
        
#        end = time.time()
#        time_taken = (end-start)*1000
#        print("Parsing page... done in ") 
#        print( time_taken, "ms")
#        print(len(href_links), " links ") 
        
        return self.host, int(self.port), self.path, self.query
    
#   # def load(self, string):
#        response = urllib.request.Request(string) #getting forbidden error
#        data = urllib.request.urlopen(response)
#        start = time.time()
#        len_data = len(data.read())
#        end = time.time()
#        print("Loading... done in ", (end-start)*1000, "ms with ", len_data, " bytes")