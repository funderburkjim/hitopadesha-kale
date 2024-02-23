reformat hitokale_deva_p.txt for https://samskrtam.info/.
   a copy from ../deva/hitokale_deva_p.txt as of 02-17-2024
   
sample.txt of the new format

--------------------------------------------------------
01.txt semicolon lines between F and A moved so after A

python checkF.py hitokale_deva_p.txt temp.txt
18511 lines read from hitokale_deva_p.txt
3416 F lines
98 next line not an A line
18511 lines written to 01.txt

cp temp.txt 01.txt
Manually edit 01.txt: move the comments between F and A after A.
A few are deleted.  The ' CHK' text is removed

python checkF.py 01.txt temp.txt
# 0 next line not an A line
--------------------------------------------------------
02.txt  Remove '2021' and '2022' lines
cp 01.txt 02.txt
python remove_dates.py 01.txt 02.txt temp_removed_02.txt
18503 lines read from 01.txt
18376 lines written to 02.txt
127 lines written to temp_removed_02.txt

--------------------------------------------------------
03.txt  change P+ to P, also P++, +++

python P_remove_plus.py 02.txt 03.txt

18376 lines read from 02.txt
339 lines changed
18376 lines written to 03.txt

--------------------------------------------------------
04.txt remove empty comment lines and empty lines
python remove_empty.py 03.txt 04.txt

18376 lines read from 03.txt
168 empty comment lines removed
4701 empty lines removed
13507 lines written to 04.txt
--------------------------------------------------------
; 05.txt  remove marked Jim, Sampada
; Also, add 105.31-33E: (last section)

cp 04.txt 05.txt
manual edit 05.txt

05.txt is a good 'cleaned' form.
--------------------------------------------------------
06.txt  remove comments at beginning of file,
   and save for future use.

Separate 05.txt into two parts:
 06a.txt and 06.txt 

python remove_initial.py 05.txt 06a.txt 06.txt 
13476 lines read from 05.txt
64 lines written to 06a.txt
13412 lines written to 06.txt


(+ 64 13412) = 13476
# check invertible
cat 06a.txt 06.txt > temp.txt
diff 05.txt temp.txt | wc -l
# 0 as expected
rm temp.txt

--------------------------------------------------------
07.txt comment line in 06.txt starts with ';'
The previous non-comment line should be an A: line
Check for this property, by moving comment-lines

python check_linetype.py 06.txt temp_07.txt
15 unknown line types marked

cp temp_07.txt 07.txt #and manually correct linetypes
 (which start with '***')
# check again after changes
python check_linetype.py 07.txt temp_07.txt
# 0 unknown line types marked

--------------------------------------------------------
08.txt checkEF
check that every E: is followed by F:

python checkEF.py 07.txt temp_08.txt
13412 lines read from 07.txt
100 errors noted
13412 lines written to temp_08.txt

cp temp_08.txt 08.txt
  Manually correct the 100 errors in 08.txt
  Problems are noted in temp_08.txt by
  starting with 'ERR '
# rerun with 08.txt
python checkEF.py 08.txt temp_08.txt
13408 lines read from 08.txt
0 errors noted
13408 lines written to temp_08.txt

Also, change '&c.' to 'etc.'
--------------------------------------------------------
hitokale_09.xml  

Add markup for sections, as defined by 'E:'
python e_group.py 08.txt hitokale_09.xml

hitokale_09.dtd
python /c/xampp/htdocs/cologne/xmlvalidate.py hitokale_09.xml hitokale_09.dtd
# ok

<hitokale>

<group ident="ppp,dd1,dd2" type="x">
  X = 'prose' or X="shloka n"
 
</group>

--------------------------------------------------------
Adding section element
<section n="0" title="प्रस्ताविका">
   <group ident="001,01,02">
   ...
   <group ident="005,11,11" type="prose">
</section>

<section n="1" title="मित्रलाभः">
<group ident="005,12,12" type="prose">
   ...
<group ident="032,18,21" type="shloka 213">
</section>

<section n="2" title="सुहृद्भेदः">
 <group ident="032,22,22" type="prose">
   ...
<group ident="061,21,22" type="shloka 182">
</section>

<section n="3" title="विग्रहः">
<group ident="061,23,23" type="prose">
   ...
<group ident="086,05,06" type="shloka 150">
</section>
 Note
  <group ident="086,05,06" type="shloka 150"> ->
  <group ident="086,05,07" type="shloka 150">
  086.07  not in <group ident="086,08,08" type="prose">
  
<section n="4" title="संधिः">
<group ident="086,08,08" type="prose">
   ...
<group ident="105,31,33" type="shloka 141">
</section>

</hitokale>

<body>

-----------------------------------------------
hitokale_10.xml
Add section.n
old:
<group ident="001,03,04" type="shloka 1">
new:
<group ident="001,03,04" type="shloka 0.1">

old:
001.04F: जाह्नवीफेनलेखेव यन्मूर्ध्नि शशिनः कला ॥ १॥
new:
001.04F: जाह्नवीफेनलेखेव यन्मूर्ध्नि शशिनः कला ॥ ०,१॥
And similarly for
001.04F

use comma since not transcoded by slp1_deva.xml
and similarly not by deva_slp1.xml

python shloka_section.py hitokale_09.xml hitokale_10.xml

1577 matches for "॥ *$"
1464 matches for "[०१२३४५६७८९]+॥"
732 matches for "^[0-9][0-9][0-9]\.[0-9][0-9]F: .*[०१२३४५६७८९]+॥"
732 matches for "^[0-9][0-9][0-9]\.[0-9][0-9]A: .*[०१२३४५६७८९]+॥"

^[0-9][0-9][0-9]\.[0-9][0-9]F: .*॥ [०१२३४५६७८९]+,[०१२३४५६७८९]+॥
^[0-9][0-9][0-9]\.[0-9][0-9]A: .*॥ [०१२३४५६७८९]+,[०१२३४५६७८९]+॥
There are 732 shlokas

732 matches for "type="shloka" in buffer: hitokale_10.xml
why not 
cp hitokale_09.dtd hitokale_10.dtd
python /c/xampp/htdocs/cologne/xmlvalidate.py hitokale_10.xml hitokale_10.dtd
# ok
