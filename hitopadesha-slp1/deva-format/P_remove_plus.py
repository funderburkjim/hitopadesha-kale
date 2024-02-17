# coding=utf-8
""" P_remove_plus.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   out = ''  # blank line separates recs
   f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

regex_page_line = '^([0-9][0-9][0-9]\.[0-9][0-9])'
regexF = r'%sF: ' % regex_page_line
regexA = r'%sA: ' % regex_page_line
def P_remove_plus(lines):
 newlines = []
 n = 0 # number of lines changed
 regex = r'%s(P[+]+)' % regex_page_line
 for iline,line in enumerate(lines):
  newline = re.sub(regex,r'\1P',line)
  if newline != line:
   n = n + 1
  newlines.append(newline)

 print(n,'lines changed')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  #  
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines = P_remove_plus(lines)
 write_lines(fileout,newlines)

 
