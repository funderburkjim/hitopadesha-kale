# coding=utf-8
""" check_linetype.py
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
regexP = r'%sP: ' % regex_page_line
regexE = r'^([0-9][0-9][0-9])\.([0-9][0-9])-([0-9][0-9])E: '

def get_linetype(line):
 if line.startswith(';'):
  kind = 'C'
 elif re.search(regexF,line):
  kind = 'F'
 elif re.search(regexP,line):
  kind = 'P'
 elif re.search(regexA,line):
  kind = 'A'
 elif re.search(regexE,line):
  kind = 'E'
 else:
  kind = None
 return kind

def check_linetype(lines):
 newlines = []  
 n = 0 # number of lines changes
 prevtag = None
 nerr = 0
 for iline,line in enumerate(lines):
  kind = get_linetype(line)
  if kind == None:
   #print('checkC ERROR:',iline+1,line)
   nerr = nerr + 1
   newline = '? ' + line
  else:
   newline = line
  newlines.append(newline)
 print(nerr,'unknown line types marked ')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  # error notes
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines = check_linetype(lines)
 write_lines(fileout,newlines)
 
