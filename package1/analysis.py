import re
from .mocklink import WebAccess

class Analysis():
    roughing = '<span class="txt">([\s\S]*?)</li>'
    name_machining = '<i class="nick" title="([\w\W]*?)">' 
    number_machining = '<i class="js-num">([\s\S]*?)</i>'

    def __roughing(self, html):
        anchors = re.findall(Analysis.roughing, html)
        return anchors
    
    def __finishing(self, roughing):
        anchors = []
        for html in roughing:
            name = re.findall(Analysis.name_machining, html)
            number = re.findall(Analysis.number_machining, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def go_roughing(self, html):
        anchors = self.__roughing(html)
        return anchors
    
    def go_finishing(self, roughing):
        anchors = self.__finishing(roughing)
        return anchors




        
    