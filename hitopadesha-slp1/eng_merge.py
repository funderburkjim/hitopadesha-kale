# -*- coding: utf-8 -*-
""" eng_merge.py
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
  # detect last line of form xxx.yy
  m =  re.search(r'^([0-9][0-9][0-9][.][0-9][0-9])(.*?):',x)
  if m:
   key = m.group(1)
   sfx = m.group(2)
   if sfx in ['F','A','P']:
    pass
   elif re.search('^P[+]*$',sfx):
    pass
   elif re.search(r'^-[0-9][0-9]E$',sfx):
    pass
   else:
    print('init_dictA ERROR at line',i+1)
    print(x)
    exit(1)
   if key not in dictA:
    dictA[key]=[]
   dictA[key].append((i,sfx))  # index of last line with given 
 return dictA

def init_eng(filein):
 # filein is hitoeng.txt
 with codecs.open(filein,"r","utf-8") as f:
  dictE = {}
  lines = [] # list of lines
  for i,x in enumerate(f):
   #print(i)  # to find non-utf8 codings
   #x = x.rstrip('\r\n')
   x = x.strip()
   lines.append(x)
   #recs.append(x)
   # identify an English translattion following the given line.
   m =  re.search(r'^; +([0-9][0-9][0-9][.][0-9][0-9])$',x)
   if m:
    lnum  = m.group(1)  #xxx.yy
    if lnum in dictE:
     print('init_eng ERROR. line number duplicate:',x)
     exit(1)
    dictE[lnum]= i # index of line with this lnum

 print(len(dictE.keys()),"identified lines",filein)
 return dictE,lines

def check_no_translation(vnum,dictA):
 """ function exits if a problem
     Otherwise just returns
 """
 if vnum not in dictA:
  print('merge Error 1: Cannot find verse %s in text' %vnum)
  exit(1)
 # list of pairs, (i,sfx) of lines in dictA where the line id
 # is vnum + sfx
 i_sfx_pairs = dictA[vnum]
 # check that '-zzE' is not among the suffixes
 E_pairs = [(i,sfx) for i,sfx in i_sfx_pairs if sfx.endswith('E')]
 if len(E_pairs) != 0:
  print('merge Error 2: English translation already found',vnum)
  exit(1)

def merge(linesin,dictA,dictE,linesE,pagein):
 # process in reverse, so line insertions will work properly
 keys_E = [vnum for vnum in dictE.keys() if vnum.startswith(pagein+'.')]
 keys = sorted(keys_E) #sorted(keys_E,reverse=True)
 linesafter = {}
 ivnum_last = len(keys)-1 # last index into keys
 for ivnum,vnum in enumerate(keys):
  # vnum is a verse id: xxx.yy
  # indx_E is index into linesE, the lines of hitoeng
  indx_E = dictE[vnum] 
  etran = linesE[indx_E + 1]  # the translation on next line of hitoeng
  # check that we do not already have a translation for vnun
  check_no_translation(vnum,dictA)
  # The translation pertains to a range of verse numbers, starting with vnum.
  # We don't know the last verse number,but must infer it.
  if ivnum < ivnum_last:
   ivnum_next = ivnum + 1  # next translation
   vnum_next = keys[ivnum_next]  ## xxx.zz
   zz = vnum_next[-2:]  # this is where NEXT translation STARTS
   izz_next = int(zz)
   izz_last = izz_next - 1 # where current translation ENDS
   vnum1 = '%s.%02d' %(pagein,izz_last)
   # check that vnum1 in dictA
   if vnum1 not in dictA:
    print('merge Error 3: verse number not in dictA',ivnum,vnum,vnum1)
    exit(1)
  else:
   # there is no 'next translation'. Find last verse in dictA for pagein
   vnums = [k for k in dictA.keys() if k.startswith(pagein+'.')]
   vnums = sorted(vnums)
   vnum1 = vnums[-1]  # we know vnum1 in dictA
  #print(vnum,vnum1)
  i_sfx_pairs1 = dictA[vnum1]
  idx_A,sfxlast = i_sfx_pairs1[-1]  # last line with verseid vnum1
  zz = vnum1[-2:]  # vnum1 = xxx.zz
  newid = vnum + '-'+zz + 'E: '  # prefix for new translation line
  newline = newid + etran
  # insert a blank line and newline
  newlines = ['',newline]
  # these newlines to go after linesin at idx_A
  linesafter[idx_A] = newlines
  # insert newlines into linesin AFTER line ilast
 # construct the new list of lines
 linesout = []
 for idx_A,line in enumerate(linesin):
  linesout.append(line)
  if idx_A in linesafter:
   newlines = linesafter[idx_A]
   for newline in newlines:
    linesout.append(newline)
 return linesout

def unused_merge(linesin,dictA,dictE,linesE,pagein):
 # process in reverse, so line insertions will work properly
 keys_E = [lnum for lnum in dictE.keys() if lnum.startswith(pagein+'.')]
 keys = sorted(keys_E,reverse=True)
 for ivnum,vnum in enumerate(keys):
  # vnum is a verse id
  # indx_E is index into linesE, the lines of hitoeng
  indx_E = dictE[vnum] 
  if vnum not in dictA:
   print('merge Error 1: Cannot find verse %s in text' %vnum)
   exit(1)
  # list of pairs, (i,sfx) of lines in dictA where the line id
  # is vnum + sfx
  i_sfx_pairs = dictA[vnum]
  # check that '-zzE' is not among the suffixes
  E_pairs = [(i,sfx) for i,sfx in i_sfx_pairs if sfx.endswith('E')]
  if len(E_pairs) != 0:
   print('merge Error 2: English translation already found',vnum)
   exit(1)
  # insert blank line, then english translation after line ilast of linesin
  newlines = []
  newlines.append('') # blank line
  # the english translation are all lines after indx_E in linesE,
  # up to the next ';' 
  # We ASSUME that there is just ONE such line 
  # (this assumption is believed to be almost always true;
  #  exceptions will be handled by later manual process.
  etran = linesE[indx_E + 1]  # the translation on next line
  # find identifier of the new line. In other words: suppose vnum is
  # Example: vnum is 004.30.  And etran is the translation of 
  # two lines: 004.30 and 004.31.
  # We want to put etran AFTER the other lines of 004.31.
  # and to label the etran line with '004.30-31E'
  # if ivnum is 0, then we are in the last English translation on page 004.
  if ivnum == 0:
   pagenum,versenum = vnum.split('.')
   iversenum = int(versenum)
   iversenum1 = iversenum + 1
   versenum1 = '%02d'%iversenum1
   vnum1 = '%s.%s' %(pagenum,versenum1)
  else:
   vnum1 = keys[ivnum - 1]
   pagenum,versenum1 = vnum1.split('.')
  if vnum1 not in dictA:
   print('merge Error 3: next verse number not in dictA',ivnum,vnum,vnum1)
   exit(1)
  print(vnum,vnum1)
  i_sfx_pairs1 = dictA[vnum1]
  ilast,sfxlast = i_sfx_pairs1[-1]
  newid = vnum + ('-%s'%versenum1) + 'E: '
  newline = newid + etran
  newlines.append(newline)
  # insert newlines into linesin AFTER line ilast
  for i,newline in enumerate(newlines):
   j = ilast + i + 1
   linesin.insert(j,newline)


if __name__ == "__main__":
 filein = sys.argv[1]   #hitokale_slp1_p.txt
 fileeng = sys.argv[2]   #../hitoenglish/hitoeng.txt
 pageeng = sys.argv[3]  # 005, etc.
 filesave = sys.argv[4]  #old (pre-merge) version of hitokale_slp1_p.txt
 linesin = init_slp1_p(filein)
 print(filein,'has',len(linesin),'lines before merger')
 dictA = init_dictA(linesin)
 dictE,linesE = init_eng(fileeng)
 try:
  #os.rename(filein,filesave)
  shutil.copyfile(filein,filesave)
  print('copied %s to %s' %(filein,filesave))
 except:
  print('Cannot copy %s to %s'%(filein,filesave))
  exit(1)  # don't proceed
 # insert english lines into linesin.
 linesout = merge(linesin,dictA,dictE,linesE,pageeng)
 #print('debug: exit early')
 #exit(1)
 # write over filein
 with codecs.open(filein,"w","utf-8") as f:
  for x in linesout:
   f.write(x+'\n')
 print(filein,'has',len(linesout),'lines after merger')
