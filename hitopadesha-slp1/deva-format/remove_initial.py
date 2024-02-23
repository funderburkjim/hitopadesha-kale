# coding=utf-8
""" remove_initial.py
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


def make_parts(lines):
 lines1 = []
 lines2 = []
 flag = True  # line is in first part
 n = 0 # number of lines removed 
 for iline,line in enumerate(lines):

  if flag:
   if re.search(regexF,line):
    flag = False
  if flag:
   lines1.append(line)
  else:
   lines2.append(line)

 return lines1,lines2

if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout1 = sys.argv[2] # initial comments
 fileout2 = sys.argv[3]  # everything but initial comments
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 lines1,lines2 = make_parts(lines)
 write_lines(fileout1,lines1)
 write_lines(fileout2,lines2)
 
 
