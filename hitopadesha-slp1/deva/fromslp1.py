#-*- coding:utf-8 -*-
"""fromslp1.py   convert files from sanskrit in slp1 to other transcodings
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')
def convert(line,tranout,iline):
 tranin = 'slp1'
 if line.startswith(';'):
  return line # comment
 if re.search(r'^ *$',line): # empty line
  return line
 #m = re.search(r'^([0-9][0-9][0-9][.][0-9][0-9][A-Z]+): (.*)$',line)
 m = re.search(r'^([0-9.-]+)([A-Z+]+): (.*)$',line)
 if not m:
  print('convert Format ERROR line %s\n%s'% (iline+1,line))
  exit(1)
 a = m.group(1)
 cat = m.group(2)
 t = m.group(3)
 if cat in ('E'):
  return line
 t1 = transcoder.transcoder_processString(t,tranin,tranout)
 b = '%s%s: %s' %(a,cat,t1)
 return b
if __name__=="__main__": 
 tranout = sys.argv[1] # deva or slp1
 filein = sys.argv[2] #  xxx.txt file to be converted
 fileout = sys.argv[3] # result of conversion
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 with codecs.open(fileout,'w','utf-8') as f:
  for iline,line in enumerate(lines):
   out = convert(line,tranout,iline)
   f.write(out+'\n')
