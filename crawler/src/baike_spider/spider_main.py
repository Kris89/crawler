#coding:utf-8
'''
Created on 2016��7��9��

@author: super idiot
'''
from baike_spider import html_downlodader, url_manager, html_parser,\
    html_outputer


class SpiderMain(object):
    #�ڹ��캯���г�ʼ������Ҫ�Ķ���
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downlodader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    #������ȳ���    
    def craw(self, root_url):
        cout = 1
        self.urls.add_new_url(root_url)#��ʱurl���������Ѿ���ȡ�˴���ȡ��url����һ�����������ѭ��
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()#��ȡ������ҳ��
                print 'craw %d : %s'%(cout,new_url)
                html_cont = self.downloader.load(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)#��ҳ����н�������ȡ�µ�url�洢��new_urls��
                self.urls.add_new_urls(new_urls)#��new_urls��ʱ�����д洢��һ��urls��һ�����ݽṹ��
                self.outputer.collect_data(new_data)
                
                if cout == 100:
                    break
                cout = cout + 1
                
            except Exception as e:
                print('craw failed',e)
                
        self.outputer.output_html()
            

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    