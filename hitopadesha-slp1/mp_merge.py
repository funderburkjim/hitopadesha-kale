# -*- coding: utf-8 -*-
""" mp_merge.py
"""
import re,codecs,sys
#import os
import shutil

def init_slp1_p(filein):
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for i,x in enumerate(f):
   #print(i)  # to find non-utf8 codings
   x = x.rstrip('\r\n')
   x = x.strip()
   recs.append(x)
 return recs

def init_dictA(recs):
 dictA = {}
 for i,x in enumerate(recs):
  # detect Analyzed Sandhi lines
  m =  re.search(r'^([0-9][0-9][0-9][.][0-9][0-9]A:)',x)
  if m:
   key = m.group(1)
   if key in dictA:
    print('init_prev. Duplicate A record',key,'at index',i)
    exit(1)
   dictA[key] = i
 return dictA

def init_mp(filein):
 with codecs.open(filein,"r","utf-8") as f:
  dictP = {}
  for i,x in enumerate(f):
   #print(i)  # to find non-utf8 codings
   x = x.rstrip('\r\n')
   x = x.strip()
   #recs.append(x)
   # identify a marma-prakASika line
   m =  re.search(r'^([0-9][0-9][0-9][.][0-9][0-9])(P.*?:)',x)
   if m:
    lnum  = m.group(1)  #xxx.yy
    if lnum not in dictP:
     dictP[lnum]=[]
    dictP[lnum].append(x)
 print(len(dictP.keys()),"lines with marma-prakASika from",filein)
 print(sum(len(dictP[k]) for k in dictP.keys()),"total mp-lines")
 return dictP

def merge(linesin,dictA,dictP):
 # process in reverse, so line insertions will work properly
 keys = sorted(dictP.keys(),reverse=True)
 for k in keys:
  plines = dictP[k]
  ak = k + 'A:'
  if ak not in dictA:
   print('Cannot find %s' %ak)
   exit(1)
  indx = dictA[ak]
  # insert all lines of plines AFTER indx
  for i in range(len(plines)):
   j = indx + i + 1
   linesin.insert(j,plines[i])

if __name__ == "__main__":
 filein = sys.argv[1]   #hitokale_slp1_p.txt
 filemp = sys.argv[2]   #sam-hito-p/sampada_mp_nnn.txt
 filesave = sys.argv[3]  #old (pre-merge) version of hitokale_slp1_p.txt
 linesin = init_slp1_p(filein)
 print(filein,'has',len(linesin),'lines before merger')
 dictA = init_dictA(linesin)
 dictP = init_mp(filemp)
 try:
  #os.rename(filein,filesave)
  shutil.copyfile(filein,filesave)
  print('copied %s to %s' %(filein,filesave))
 except:
  print('Cannot copy %s to %s'%(filein,filesave))
  exit(1)  # don't proceed
 # insert mp lines into linesin.
 merge(linesin,dictA,dictP)
 #exit(1)
 # write over filein
 with codecs.open(filein,"w","utf-8") as f:
  for x in linesin:
   f.write(x+'\n')
 print(filein,'has',len(linesin),'lines after merger')
