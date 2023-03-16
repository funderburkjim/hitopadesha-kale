
python fromslp1.py deva ../hitopadesha-slp1.txt hitopadesha-deva.txt

python fromslp1_F.py deva ../hitokale_slp1_p.txt hitokale_deva_F.txt

#----- devanagari
python fromslp1.py deva ../hitokale_slp1_p.txt hitokale_deva_p.txt
python toslp1.py deva hitokale_deva_p.txt temp_hitokale_slp1_p.txt
diff ../hitokale_slp1_p.txt temp_hitokale_slp1_p.txt
# should be no difference
rm temp_hitokale_slp1_p.txt

#----- iast
python fromslp1.py roman ../hitokale_slp1_p.txt hitokale_iast_p.txt
python toslp1.py roman hitokale_iast_p.txt temp_hitokale_slp1_p.txt
diff ../hitokale_slp1_p.txt temp_hitokale_slp1_p.txt
rm temp_hitokale_slp1_p.txt


