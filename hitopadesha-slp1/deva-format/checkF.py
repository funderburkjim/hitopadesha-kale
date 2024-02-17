# coding=utf-8
""" hremove.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

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
def checkF(lines):
 newlines = []
 n = 0 # number of lines changes
 nf = 0
 for iline,line in enumerate(lines):
  if not re.search(regexF,line):
   newlines.append(line)
   continue
  nf = nf + 1
  # line is F-line
  # is next line an A-line?
  nextline = lines[iline+1]
  if re.search(regexA,nextline):
   newlines.append(line)
   continue
  # temporary mark this F-line 
  newline = line + ' CHK'
  newlines.append(newline)
  n = n + 1
 print(nf,'F lines')
 print(n, 'next line not an A line')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version pw.txt
 fileout = sys.argv[2]  # version of pw.txt with <e>N removed
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines = checkF(lines)
 write_lines(fileout,newlines)
 
