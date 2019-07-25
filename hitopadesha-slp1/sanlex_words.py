# -*- coding: utf-8 -*-
"""sanlex_words.py
python sanlex_words.py 0001,0010 hitopadesha-slp1.txt tempout.txt
Utility program.
Consider the lines whose 'id' is between (inclusive) 0001A: and 0010A:
Break the line into words (via spaces) and
print the resulting words 
e.g. If one of the filtered lines is
0072A: ekEkam api anarTAya kim yatra catuzwayam .. 11..
output 
; 0072
ekEkam
api
anarTAya
kim
yatra
catuzwayam
 'ekEkam','api','anarTAya','kim','yatra','catuzwayam'
This is to make more efficient the manual generation of dictionary headwords
based on the text.
A few word endings will be dropped:  m,M,H
A few common words will be skipped.

python sanlex_words.py 0100,0149 hitopadesha-slp1.txt tempout.txt
(50, 'records kept')
(210, 'words from', 50, 'padas written to', 'tempout.txt')

"""
import re,codecs,sys

class Rec(object):
 def __init__(self,recid,words,line):
  self.line = line
  self.recid = recid
  # skip ending danda and/or verse number
  words = [w for w in words if not '.' in w]
  self.words = words
  self.wordsadj = []  # filled in later

def init_recs(filein,first,last):
 recs = []
 #print(first,last)
 with codecs.open(filein,"r","utf-8") as f:
  for i,x in enumerate(f):
   x = x.rstrip('\r\n')
   x = x.strip()
   if x == '':
    continue
   words = re.split(r' +',x)
   if x.startswith(';'):
    continue
   if not words[0].endswith('A:'):  # keep only analyzed sandhi lines
    continue
   recid = words[0]
   recid = recid[0:-2]  # remove A:
   #print(recid)
   if recid < first:
    continue
   if recid > last:
    break
   recs.append(Rec(recid,words[1:],x))
 print(len(recs),"records kept")
 return recs

skip_words_txt="""
saH sa kaH yaH sA kA yA kim
tasya kasya yasya
na ca tu iti api atra yatra eva vA
tena yena kena taTA yaTA
iva
"""
def init_skip_words():
 lines = skip_words_txt.splitlines()
 words = []
 for line in lines:
  line = line.rstrip('\r\n')
  wordsline = re.split(r' +',line)
  words = words + wordsline
 return set(words)

predetermined_words = {
 "Bavanti":"BU","uvAca":"vac","UcuH":"vac",
 "abravIt":"brU", "avadat":"vad",
 "anyat":"anya",
 "yataH":"yatas",
 "tataH":"tatas",
 "dfzwvA":"dfS", "paSyati":"dfS", 
 "ataH":"atas",
 "etat":"etad",
 "SrutvA":"Sru",
 "paScAd":"paScAt",
 "paScAt":"paScAt",
 "asya":"idam","anena":"idam",
 "Aha":"ah", "AhuH":"ah","brUte":"brU", "tizWati":"sTA",
 # words, such as those ending in 'am', that need no change
 "aham":"aham", "kaTam":"kaTam", "evam":"evam",
 "idam":"idam","AH":"AH","ayam":"ayam",
 "anantaram":"anantaram"
}
def adjust_word(word):
 if word in predetermined_words:
  return predetermined_words[word]
 # remove common inflections for nouns ending in 'a'
 word1 = word
 word1 = re.sub(r'EH$','a',word1)
 word1 = re.sub(r'AH$','a',word1)
 word1 = re.sub(r'A[td]$','a',word1)
 word1 = re.sub(r'e[nR]a$','a',word1)
 word1 = re.sub(r'asya$','a',word1)
 word1 = re.sub(r'Aya$','a',word1)
 word1 = re.sub(r'A[nR]Am$','a',word1)
 word1 = re.sub(r'ezu$','a',word1)
 word1 = re.sub(r'An$','a',word1)
 word1 = re.sub(r'[mMH]$','',word1)
 word1 = re.sub(r'e$','a',word1)
 
 return word1

def adjust(recs):
 skip_words = init_skip_words() 
 for rec in recs:
  wordsadj = []
  for word in rec.words:
   if word in skip_words:
    continue
   word1 = adjust_word(word)
   wordsadj.append(word1)
  rec.wordsadj = wordsadj

def output(recs,fileout):
 with codecs.open(fileout,"w","utf-8") as f:
  nwtot = 0  # total number of words
  for rec in recs:
   outarr = []
   outarr.append('; ' + rec.recid)
   outarr = outarr + rec.wordsadj
   nwtot = nwtot + len(rec.wordsadj)
   for out in outarr:
    f.write(out + '\n')
 print(nwtot,"words from",len(recs),"padas written to",fileout)

if __name__ == "__main__":
 option = sys.argv[1]   #XXXX,YYYY
 filein = sys.argv[2]
 fileout = sys.argv[3]
 first,last = option.split(',')
 recs = init_recs(filein,first,last)
 adjust(recs)
 output(recs,fileout)
