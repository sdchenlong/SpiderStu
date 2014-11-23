__author__ = 'Lenovo'
import re
import urllib
import urllib2
import cookielib
class Spider:
 def getpage(self,name,x='.com'):
  values = {"d_name":"","dtype":"common","drand":".1416113688132"}
  values["d_name"] = name+x
  data = urllib.urlencode(values)
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar))
  headers = {"User-agent":"Mozilla/4.0(compatible;MSIE5.5;Windows NT"}
  req = urllib2.Request("http://www.zgsj.com/domain_reg/domaintrans.asp",data,headers)
  response = urllib2.urlopen(req)
  page=response.read()
  pattern = re.compile('color:green;')
  result = pattern.findall(page)
  if result:
   print name
 def addname(self):
  for n1 in range(97,123):
    self.getpage(chr(n1))
    for n2 in range(97,123):
     self.getpage(chr(n1)+chr(n2))
     for n3 in range(97,123):
      self.getpage(chr(n1)+chr(n2)+chr(n3))
      for n4 in range(97,123):
       self.getpage(chr(n1)+chr(n2)+chr(n3)+chr(n4))
       for n5 in range(97,123):
        self.getpage(chr(n1)+chr(n2)+chr(n3)+chr(n4)+chr(n5))
cl = Spider()
cl.addname()

