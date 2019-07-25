# -*- coding: utf-8 -*-
""" adjust1.py
   Changes to hitoengXXX.txt in place.
   This will speed up the proofreading.
   
  python adjust1.py 11 20
  

"""
import sys,re,codecs

def adjust_line(x):
 x = x.replace(' )',')')
 x = x.replace('( ','(')
 x = x.replace(u'—',' -- ')
 x = x.replace(' & ',' a ')
 x = re.sub(r'([a-z])-([A-Z])',r'\1 -- \2',x)
 return x

def adjust(n):
 filein = "hitoeng%03d.txt" %n
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip() for x in f]
 fileout = filein
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   line1 = adjust_line(line)
   f.write(line1 + '\n')
 print('Adjusted',filein)

if __name__ == "__main__":
 n1 = int(sys.argv[1])
 n2 = int(sys.argv[2])
 for n in range(n1,n2+1):
  adjust(n)

