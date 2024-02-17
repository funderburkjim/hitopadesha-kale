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
