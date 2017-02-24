#coding:utf-8
'''
Created on 2016��7��9��
该模块应用到py的网络模块——http
@author: super idiot
'''
import urllib2


class HtmlDownloader(object):
    
    
    def load(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
        
    
    



