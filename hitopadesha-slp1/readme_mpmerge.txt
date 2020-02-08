12-28-2019  Have merged pages 1-45.
01-15-2020  Have merged pages 46-50 
12-28-2019  Merged pages 51-70
02-07-2020  Merged pages 71-75
pages 76-80 not done (as of 02-07-2020) search xxx
02-07-2020  Merged pages 81-90
$ python mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_003.txt temp_hitokale_slp1_p_002.txt
('hitokale_slp1_p.txt', 'has', 10783, 'lines before merger')
(7, 'lines with marma-prakASika from', 'sam-hito-p/sampada_mp_003.txt')
(12, 'total mp-lines')
copied hitokale_slp1_p.txt to temp_hitokale_slp1_p_002.txt
('hitokale_slp1_p.txt', 'has', 10795, 'lines after merger')


python mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_004.txt temp_hitokale_slp1_p_003.txt
('hitokale_slp1_p.txt', 'has', 10795, 'lines before merger')
(9, 'lines with marma-prakASika from', 'sam-hito-p/sampada_mp_004.txt')
(10, 'total mp-lines')
copied hitokale_slp1_p.txt to temp_hitokale_slp1_p_003.txt
('hitokale_slp1_p.txt', 'has', 10805, 'lines after merger')

python mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_005.txt temp_hitokale_slp1_p_004.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_006.txt temp_hitokale_slp1_p_005.txt
(let (i i2 file)
 (setq i 7)
 (setq i2 45)
 (while (<= i i2)
  (insert (format "python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_%03d.txt temp_hitokale_slp1_p_%03d.txt\n" i (- i 1)))
  (setq i (1+ i))
 )
)
; Have merged through page 45 from sampada

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_007.txt temp_hitokale_slp1_p_006.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_008.txt temp_hitokale_slp1_p_007.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_009.txt temp_hitokale_slp1_p_008.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_010.txt temp_hitokale_slp1_p_009.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_011.txt temp_hitokale_slp1_p_010.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_012.txt temp_hitokale_slp1_p_011.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_013.txt temp_hitokale_slp1_p_012.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_014.txt temp_hitokale_slp1_p_013.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_015.txt temp_hitokale_slp1_p_014.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_016.txt temp_hitokale_slp1_p_015.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_017.txt temp_hitokale_slp1_p_016.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_018.txt temp_hitokale_slp1_p_017.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_019.txt temp_hitokale_slp1_p_018.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_020.txt temp_hitokale_slp1_p_019.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_021.txt temp_hitokale_slp1_p_020.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_022.txt temp_hitokale_slp1_p_021.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_023.txt temp_hitokale_slp1_p_022.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_024.txt temp_hitokale_slp1_p_023.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_025.txt temp_hitokale_slp1_p_024.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_026.txt temp_hitokale_slp1_p_025.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_027.txt temp_hitokale_slp1_p_026.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_028.txt temp_hitokale_slp1_p_027.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_029.txt temp_hitokale_slp1_p_028.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_030.txt temp_hitokale_slp1_p_029.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_031.txt temp_hitokale_slp1_p_030.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_032.txt temp_hitokale_slp1_p_031.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_033.txt temp_hitokale_slp1_p_032.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_034.txt temp_hitokale_slp1_p_033.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_035.txt temp_hitokale_slp1_p_034.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_036.txt temp_hitokale_slp1_p_035.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_037.txt temp_hitokale_slp1_p_036.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_038.txt temp_hitokale_slp1_p_037.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_039.txt temp_hitokale_slp1_p_038.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_040.txt temp_hitokale_slp1_p_039.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_041.txt temp_hitokale_slp1_p_040.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_042.txt temp_hitokale_slp1_p_041.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_043.txt temp_hitokale_slp1_p_042.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_044.txt temp_hitokale_slp1_p_043.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_045.txt temp_hitokale_slp1_p_044.txt

; Moved all the temp_hitokale_slp1_p_xxx.txt files into temp_hitokale_slp1_p directory 


python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_046.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_045.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_047.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_046.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_048.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_047.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_049.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_048.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_050.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_049.txt

------------------------------------------------------------------------------------------------
merged 51-70  12-29-2019
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_051.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_050.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_052.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_051.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_053.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_052.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_054.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_053.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_055.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_054.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_056.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_055.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_057.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_056.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_058.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_057.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_059.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_058.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_060.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_059.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_061.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_060.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_062.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_061.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_063.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_062.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_064.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_063.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_065.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_064.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_066.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_065.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_067.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_066.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_068.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_067.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_069.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_068.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_070.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_069.txt


python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_071.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_070.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_072.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_071.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_073.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_072.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_074.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_073.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_075.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_074.txt


python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_081.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_080.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_082.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_081.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_083.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_082.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_084.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_083.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_085.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_084.txt

python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_086.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_085.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_087.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_086.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_088.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_087.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_089.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_088.txt
python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_090.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_089.txt


(let (i i2 file)
 (setq i 76)
 (setq i2 80) ; <<<xxx
 (while (<= i i2)
  (insert (format "python3 mp_merge.py hitokale_slp1_p.txt sam-hito-p/sampada_mp_%03d.txt temp_hitokale_slp1_p/temp_hitokale_slp1_p_%03d.txt\n" i (- i 1)))
  (setq i (1+ i))
 )
)
