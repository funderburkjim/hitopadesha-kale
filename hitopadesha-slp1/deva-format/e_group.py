# coding=utf-8
""" e_group.py
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
 sections.append(Section("3","विग्रहः","061,23,23","086,07,07"))
 sections.append(Section("4","संधिः","086,08,08","105,31,33"))
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


if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  #  
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 #lines = xml_adjust(lines)
 
 groups = make_groups(lines)
 write_groups(fileout,groups)
 
