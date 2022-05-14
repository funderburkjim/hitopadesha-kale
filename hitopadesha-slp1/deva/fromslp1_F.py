#-*- coding:utf-8 -*-
"""fromslp1.py   convert files from sanskrit in slp1 to other transcodings
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')
def convert(line,tranout):
 tranin = 'slp1'
 newline = transcoder.transcoder_processString(line,tranin,tranout)
 return newline

def filter_F_pageadjust(lines,tranout):
 ans = []
 prevpage = None
 for line in lines:
  m = re.search(r'^([0-9]+) +(.*)$',line)
  page = m.group(1)
  text = m.group(2)
  if page != prevpage:
   x = page
   ans.append(x)
   prevpage = page
  ans.append(text)
 return ans
def filter_F(lines,tranout):
 """ Keep only the 'F' lines.  
   show only the page, not the line-within-page
   And only show the page when there is a break
 """
 ans = []
 for line in lines:
  if line.startswith(';'): # comment
   continue  
  if line.strip() == '':  # blank
   continue
  m = re.search(r'^([0-9][0-9][0-9])[.][0-9][0-9]F: *(.*)$',line)
  if m == None:
   continue
  page = m.group(1)
  text = m.group(2)
  newline = '%s  %s' %(page,text)
  ans.append(newline)
 ans1 = filter_F_pageadjust(ans,tranout)
 return ans1

if __name__=="__main__": 
 tranout = sys.argv[1] # deva or slp1
 filein = sys.argv[2] #  xxx.txt file to be converted
 fileout = sys.argv[3] # result of conversion
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 newlines = filter_F(lines,tranout)
 with codecs.open(fileout,'w','utf-8') as f:
  for line in newlines:
   out = convert(line,tranout)
   f.write(out+'\n')
