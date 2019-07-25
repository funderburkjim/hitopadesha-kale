""" drive_copy.py
   Copy hitoengXXX_ocr.txt from Google drive to here,
   changing name to hitoengXXX.txt, and inserting ';hitoengxxx.txt' as
   first line of file
  python drive_copy.py "/c/Users/Jim/Google Drive/hitoenglish" 11 20
  

"""
import sys,re,codecs

def copy(dirin,n):
 filein = "%s/hitoeng%03d_ocr.txt" %(dirin,n)
 fileout = "hitoeng%03d.txt" %n
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip() for x in f]
 extra = [';'+fileout,'']
 linesout = extra + lines
 with codecs.open(fileout,"w","utf-8") as f:
  for line in linesout:
   f.write(line + '\n')
 print('Copied',filein,'to',fileout)

if __name__ == "__main__":
 dirin = sys.argv[1]
 n1 = int(sys.argv[2])
 n2 = int(sys.argv[3])
 for n in range(n1,n2+1):
  copy(dirin,n)

