#coding:utf-8
'''
Created on 2016年7月9日
该模块应用到py的bs4第三方包/插件，字符串处理（包括正则）
@author: super idiot
'''

import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    
    #parse函数的作用是，从html_cont中解析出:基本url列表；数据

    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
    
        return res_data
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)#page_url只在这里被使用
            new_urls.add(new_full_url)
        return new_urls
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None :
            return
        #通过调用bs模块，传参，得到soup对象，以便进一步数据的获取
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        
        return new_urls,new_data
    
    



