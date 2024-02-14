#-*- coding:utf-8 -*-
"""syllables.py 
"""
from __future__ import print_function
import sys, re,codecs
sys.path.insert(0,'../')
import transcoder
transcoder.transcoder_set_dir('../transcoder')

vowels_short_slp = {'a','i','u','f','x'}
vowels_long_slp = {'A','I','U','F','X','e','E','o','O'}
vowels_slp = vowels_short_slp.union(vowels_long_slp)
consonants_slp = 'kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh'
visarga = 'H'
space = ' '
avagraha = "'"
anusvara = 'M'
laghu_code = '1'
guru_code = '2'

def get_syllables(text):
 chars = [c for c in text if c not in (space,avagraha)]
 nchars = len(chars)
 iclast = nchars - 1 # index of last character
 syllable = []
 # PY: for i,c in enumerate(alist)
 # JS: for (let [i,c] of alist.entries()) 
 for ic,c in enumerate(chars):
  # cnext is the next character, or None if c is last character
  if ic == iclast:
   cnext = None
  else:
   cnext = chars[ic + 1]
  if c in vowels_slp:
   syllable.append(c)
   if cnext in (visarga,anusvara):
    syllable.append(cnext)
   yield(syllable)
   syllable = []
   continue
  if c in (visarga,anusvara):
   # handled by vowel
   continue
  if c not in consonants_slp:
   print('get_syllables Error. Unexpected "%s"' % c)
   print('text=' + text)
   exit(1)
  syllable.append(c)
  if ic == iclast:
   yield syllable

def get_syllables_list(text):
 chars = [c for c in text if c not in (space,avagraha)]
 nchars = len(chars)
 iclast = nchars - 1 # index of last character
 syllable = []
 syllables = []  # returned
 # PY: for i,c in enumerate(alist)
 # JS: for (let [i,c] of alist.entries()) 
 for ic,c in enumerate(chars):
  # cnext is the next character, or None if c is last character
  if ic == iclast:
   cnext = None
  else:
   cnext = chars[ic + 1]
  if c in vowels_slp:
   syllable.append(c)
   if cnext in (visarga,anusvara):
    syllable.append(cnext)
   syllables.append(syllable)
   syllable = []
   continue
  if c in (visarga,anusvara):
   # handled by vowel
   continue
  if c not in consonants_slp:
   print('get_syllables Error. Unexpected "%s"' % c)
   print('text=' + text)
   exit(1)
  syllable.append(c)
  if ic == iclast:
   syllables.append(syllable)
 # final adjustment when last character of text is a consonant   
 c = chars[iclast]
 if (c in consonants_slp) and (len(syllables) > 1):
  last_syl = syllables.pop()
  penul_syl = syllables.pop()
  newlast = penul_syl + last_syl # concatenate character arrays
  syllables.append(newlast)
 return syllables

def get_syllable_weights(syllable_texts):
 nsyllables = len(syllable_texts)
 weights = []
 for idx,syllable_text in enumerate(syllable_texts):
  # get weight of syllable
  lastchar = syllable_text[-1]
  if lastchar in (visarga,anusvara):
   weight = guru_code  # guru
  elif lastchar in vowels_long_slp:
   weight = guru_code
  elif (idx + 1) == nsyllables:
   # last syllable
   if lastchar in vowels_short_slp:
    weight = laghu_code
   else:
    weight = guru_code 
  elif lastchar in vowels_short_slp:
   # we know this is not last syllable
   # does next syllable start with a conjunct consonant?
   s1 = syllable_texts[idx+1] # next syllable
   n1 = len(s1)
   if n1 < 2:
    # next syllable not long enough to containt conjunct cons
    weight = laghu_code  
   elif (s1[0] in consonants_slp) and (s1[1] in consonants_slp):
    # next syllable starts with conjunct consonant
    weight = guru_code
   else:
    # next syllable does not start with conjunct consonant
    weight = laghu_code
  else:
   # error condition - more info needed for message
   print('error getting weight')
   exit(1)
  weights.append(weight)
 return weights

def process_slp1(text):
 syllables = get_syllables_list(text)
 nsyllables = len(syllables) # number of syllables
 syllable_texts = [''.join(schars) for schars in syllables]
 weights = get_syllable_weights(syllable_texts)
 return (syllable_texts,weights)

if __name__=="__main__": 
 texttran = sys.argv[1] # deva, roman, etc.
 textin = sys.argv[2]
 textslp = transcoder.transcoder_processString(textin,texttran,'slp1')
 # print(textslp)
 syllables_slp,syllable_weights = process_slp1(textslp)
 ans = [transcoder.transcoder_processString(s,'slp1',texttran) for s in syllables_slp]
 out = ' '.join(ans)
 print(out)
 print(' '.join(syllable_weights))
 if True:
  # for php debugging
  fileout = "temp_php.txt"
  with codecs.open(fileout,"w","utf-8") as f:
   out = "texttran=%s, textin=%s\n" %(texttran,textin)
   f.write(out)
 
