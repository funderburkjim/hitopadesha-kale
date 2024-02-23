# coding=utf-8
""" shloka_section.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.append('../deva')
import transcoder
transcoder.transcoder_set_dir('../deva/transcoder')

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,blanklineflag=False):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blanklineflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

regex_page_line = '^([0-9][0-9][0-9]\.[0-9][0-9])'
regexF = r'%sF: ' % regex_page_line
regexE = r'^([0-9][0-9][0-9])\.([0-9][0-9])-([0-9][0-9])E:'
# regexE = r'^([0-9][0-9][0-9]\.[0-9][0-9]-([0-9][0-9])E:'
regexA = r'%sA: ' % regex_page_line

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

class Group:
 def __init__(self,m,lines):
  # m is regexE match object
  self.page = m.group(1)
  self.idx1 = m.group(2)
  self.idx2 = m.group(3)
  self.lines = lines
  #
  subgroups = {}
  # keys of subgroups
  linetypes = 'FAPCE'
  for linetype in linetypes:
   subgroups[linetype] = []
  for line in lines:
   linetype = get_linetype(line)
   if linetype in linetypes:
    subgroups[linetype].append(line)
   else:
    print('Group ERROR: bad linetype for',line)
    exit(1)
  self.subgroups = subgroups
  
def make_groups(lines):
 n = 0 # number of lines removed
 groups = []
 grouplines = []
 for iline,line in enumerate(lines):
  m = re.search(regexE,line)
  if m == None:
   grouplines.append(line)
  else:
   grouplines.append(line)
   group = Group(m,grouplines)
   groups.append(group)
   grouplines = []
 print(len(groups),'groups found')
 return groups

def get_group_attribs(group):
 identval =  '%s,%s,%s' % (group.page,group.idx1,group.idx2)
 fgrouplast = group.subgroups['F'][-1]
 m = re.search(r'॥ *(.*?) *॥',fgrouplast)
 if m == None:
  shloka_num_latin = None
 else:
  shloka_num_deva = m.group(1)
  shloka_num_latin = transcoder.transcoder_processString(shloka_num_deva,"deva","slp1")
  if not re.search(r'^[0-9]+$',shloka_num_latin):
   #"shloka mitralABaH", 
   shloka_num_latin = None
 if shloka_num_latin == None:
  typeval = "prose"
 else:
  typeval = "shloka %s" % shloka_num_latin
 return identval,typeval

class Section:
 def __init__(self,n,title,identval1,identval2):
  self.n = n
  self.title = title
  self.identval1 = identval1
  self.identval2 = identval2
  
def init_sections():
 sections = []
 sections.append(Section("0","प्रस्ताविका","001,01,02","005,11,11"))
 sections.append(Section("1","मित्रलाभः","005,12,12","032,18,21"))
 sections.append(Section("2","सुहृद्भेदः","032,22,22","061,21,22"))
 sections.append(Section("3", "विग्रहः","061,23,23","086,07,07"))
 sections.append(Section("4", "संधिः","086,08,08","105,31,33"))
 # map of section via identval1
 d1 = {}
 for section in sections:
  d1[section.identval1] = section
 # map of section via identval2
 d2 = {}
 for section in sections:
  d2[section.identval2] = section  
 return sections,d1,d2
              
def write_groups(fileout,groups):
 sections,sectionsd1,sectionsd2 = init_sections()

 outrecs = [] # list of lines
 # xml root
 outarr = ['<hitokale>']
 outrecs.append(outarr)
 linetypes = 'FAPCE'
 for group in groups:
  outarr = []
  identval,typeval = get_group_attribs(group)
  if identval in sectionsd1:
   section = sectionsd1[identval]
   outarr.append('<section n="%s" title="%s">' %(section.n,section.title))
  outarr.append('<group ident="%s" type="%s">' % (identval,typeval))
  for linetype in linetypes:
   outarr.append('<%s>' % linetype)
   for line in group.subgroups[linetype]:
    outarr.append(line)
   outarr.append('</%s>' % linetype)
  outarr.append('</group>')
  if identval in sectionsd2:
   section = sectionsd2[identval]
   outarr.append('</section>')
  outarr.append('')
  outrecs.append(outarr)
 # close xml root
 outarr = ['</hitokale>']
 outrecs.append(outarr)
 write_recs(fileout,outrecs)

def new_groupline(line,section_id):
 m = re.search(r'<group.*?type="shloka (.*?)">',line)
 if m == None:
  newline = line
 else:
  shloka = "shloka "
  oldshloka = m.group(1)
  newshloka = '%s,%s' %(section_id,oldshloka)
  newline = line.replace(shloka+oldshloka,shloka+newshloka)
 return newline

def new_FAline(line,section_id):
 dbg = False #(line == '036.13F: स भूमौ निहतः शेते कीलोत्पाटीव वानरः ॥ ३० ॥')
 m = re.search(r'^[0-9][0-9][0-9]\.[0-9][0-9]([FA]): .*॥( *[०१२३४५६७८९]+ *)॥',line)
 if m == None:
  if dbg:print('m=',m)
  return line
 fa = m.group(1) # used?
 shloka_num_deva_raw = m.group(2)
 shloka_num_deva = shloka_num_deva_raw.strip() # remove blanks at ends
 shloka_num_latin = transcoder.transcoder_processString(shloka_num_deva,"deva","slp1")
 if dbg:print(shloka_num_deva,shloka_num_latin)
 if not re.search(r'^[0-9]+$',shloka_num_latin):
  if dbg:print('skipping')
  return line
 section_id_deva = transcoder.transcoder_processString(section_id,"slp1","deva")
 old = "॥%s॥" % shloka_num_deva_raw
 new = "॥ %s,%s॥" % (section_id_deva,shloka_num_deva)
 newline = line.replace(old,new)
 if dbg:
  print('old=',old)
  print('new=',new)
  print('newline=',newline)
 return newline

def adjust_lines(lines):
 newlines = []
 section_id = None
 for iline,line in enumerate(lines):
  m = re.search(r'<section n="(.*?)"',line)
  if m != None:
   section_id = m.group(1)
   newlines.append(line)
   continue
  newline = new_groupline(line,section_id)
  if newline != line:
   newlines.append(newline)
   continue
  #
  newline = new_FAline(line,section_id)
  if newline != line:
   newlines.append(newline)
   continue
  # other lines are unchanged
  newlines.append(line)
 return newlines

from difflib import context_diff

def check1(lines):
 regex_page_line = '^([0-9][0-9][0-9]\.[0-9][0-9])'
 regexA = r'%sA: .*॥ [०१२३४५६७८९,]+॥' % regex_page_line
 regexF = r'%sF: .*॥ [०१२३४५६७८९,]+॥' % regex_page_line
 def f(regex):
  a = []
  for line in lines:
   m = re.search(regex,line)
   if m != None:
    a.append((m.group(1),line))
  return a

 A = f(regexA)
 F = f(regexF)
 found = False
 for i,x in enumerate(A):
  a,aline = x
  y = F[i]
  f,fline = y
  if a != f:
   #print(i+1)
   #print('%sA != %sF' %(a,f))
   print('check1 First Diff')
   print('A=',a,aline)
   print('F=',f,fline)
   exit(1)
 print('check1: no diffs')
 print('#A = %s, #F = %s' % (len(A),len(F)))
 return
 # unused
 diff = context_diff(A,F,fromfile="A",tofile="F")
 diff1 = list(diff)
 print(len(diff1),"diffs from check1")
 for x in diff1:
  print(x)
 return
 diff2 = ''.join(diff1)
 print(diff2)

def check2(lines):
 regex_page_line = '^([0-9][0-9][0-9]\.[0-9][0-9])'
 regexF = r'%sF: .*॥ ([०१२३४५६७८९,]+)॥' % regex_page_line
 F = []
 for line in lines:
  m = re.search(regexF,line)
  if m != None:
   x_deva = m.group(2)
   x_latin = transcoder.transcoder_processString(x_deva,"deva","slp1")
   F.append((x_latin,line))
 #
 regex_shloka = r'^<group ident="(.*?)" type="shloka (.*?)">$'
 S = []
 for line in lines:
  m = re.search(regex_shloka,line)
  if m != None:
   x_latin  = m.group(2)
   S.append((x_latin,line))
 # first diff
 print('# shlokas=',len(S))
 print('check2 First diff')
 for i,x in enumerate(S):
  S_latin,S_line = x
  y = F[i]
  F_latin,F_line = y
  if S_latin != F_latin:
   print('S=',S_latin, S_line)
   try:
    print('F=', F_latin,F_line)
   except:
    print('print error in check2')
   return
 print('check2 no diffs')
if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  #  
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 newlines = adjust_lines(lines)
 write_lines(fileout,newlines)

 check1(newlines)
 check2(newlines)
 
