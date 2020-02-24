import re
class Sort():
    def __sort_key(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_key,  reverse=True)
        return anchors
    
    def go_sort(self, anchors):
        anchors = self.__sort(anchors)
        return anchors
    