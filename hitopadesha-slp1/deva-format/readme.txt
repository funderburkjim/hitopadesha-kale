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
