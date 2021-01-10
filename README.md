## hitopadesha-kale


Digitization of Kale's *Hitopadesha of Narayana*, 1912.

One source of scanned images pdf is https://archive.org/details/HitopadesaOfNarayanaM.R.Kale.

The scans were done by Jim Funderburk.

Major contributions by Dr. Sampada Savardekar.


## file synopsis
 
1. hitopadesha-slp1 : Sanskrit Text. As written and with sandhi analysis
   * hitokale_slp1_v2.txt is the latest form
   * hitokale_slp1_p.txt  add Kale Sanskrit notes to Sanskrit text.
                          also add Kale's English translation: xxx.yy-zzE:
                               (from hitoeng.txt)
   * folder sam-hito-p : Sampada's addition of marma-prakASika notes.
     xxx.yyP:  and P+, P++, etc.
     These are merged into hitokale_slp1_p.txt. For pages 1-2, manual
     For rest:  
      python mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_nnn.txt tempsave.txt

2. hitoenglish : Kale's translation, with markup related to hitokale_slp1 line numbering
   * hitoeng.txt is latest
3. hitonotes : digitization of Kale's 54 pages of notes

## Scanned image files

* hitopadesha.pdf : Front matter and Sanskrit text (pages 1-104)
* hitoenglish/pdfpages :  pdf of each page (1-104) of English translation.
* hitonotes/pdfpages : pdf of each page (1-54) of English notes
