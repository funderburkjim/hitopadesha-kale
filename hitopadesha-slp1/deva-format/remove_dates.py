# coding=utf-8
""" remove_dates.py
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
def remove_dates(lines):
 regex = r'^;.*202[12]' 
 newlines = []
 removed = []
 n = 0 # number of lines removed 
 nf = 0
 for iline,line in enumerate(lines):
  if re.search(regex,line):
   removed.append(line)
  elif line == '; 07/17/2020 END':
   removed.append(line)
  else:
   newlines.append(line)
 
 return newlines,removed

if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  #  
 fileout1 = sys.argv[3]  # 
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines,removed = remove_dates(lines)
 write_lines(fileout,newlines)
 write_lines(fileout1,removed)
 
