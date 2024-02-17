# coding=utf-8
""" remove_empty.py
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
def remove_empty(lines):
 regex1 = r'^; *$'
 regex2 = r'^^ *$'
 n1 = 0
 n2 = 0
 newlines = []
 n = 0 # number of lines removed 
 for iline,line in enumerate(lines):
  if re.search(regex1,line):
   n1 = n1 + 1
   continue
  elif re.search(regex2,line):
   n2 = n2 + 1
   continue
  else:
   newlines.append(line)
 print(n1,"empty comment lines removed")
 print(n2,"empty lines removed")
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  #  
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines = remove_empty(lines)
 write_lines(fileout,newlines)
 
