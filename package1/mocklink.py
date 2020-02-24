from urllib import request
import urllib
class WebAccess():
    
    def __fetch_content(self, url):
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls


    def go(self, url):
        htmls = self.__fetch_content(url)
        return htmls
