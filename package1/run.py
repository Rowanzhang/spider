from .mocklink import WebAccess
from .analysis import Analysis
from .refine import Refine
from .sort import Sort
class Run():
     def go_git(self, htmls):
         webaccess = WebAccess()
         html = webaccess.go(htmls)
         return html
     def go_analysis(self, html):
          analysis = Analysis()
          roughing = analysis.go_roughing(html)
          anchors = analysis.go_finishing(roughing)
          refine = Refine()
          anchors = refine.go_refine(anchors)
          return anchors
     def go_show(self, anchors):
          sort = Sort()
          anchors = sort.go_sort(anchors)
          for rank in range(0, len(anchors)):
              print('排名'+str(rank+1)+'   '+'主播：'+anchors[rank]['name']+"    "+'人气:'+anchors[rank]['number'])
     def go_all(self, htmls):
          html = self.go_git(htmls)
          anchors = self.go_analysis(html)
          self.go_show(anchors)
