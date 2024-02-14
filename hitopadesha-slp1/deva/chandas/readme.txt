Begun 02-03-2024.

First goal: Take a 'pada' in slp1, construct syllables, and
 identify as guru or laghu.

; 2 = guru, 1 = laghu
python syllables.py slp1 'jAhnavIPenaleKeva'
jA hna vI Pe na le Ke va
2 1 2 2 1 2 2 2

  This also works with 'deva'
python syllables.py deva 'वाचां सर्वत्र वैचित्र्यं'
वा चां स र्व त्र वै चि त्र्यं
2 2 2 2 1 2 2 2

python syllables.py deva 'भृत्यैः स्वामी कदाचन'
भृ त्यैः स्वा मी क दा च न
2 2 2 2 1 2 1 1


python syllables.py deva 'प्रसह्य मणिमुद्धरेन्मकरवक्त्रदंष्ट्रान्तरात्'
प्र स ह्य म णि मु द्ध रे न्म क र व क्त्र दं ष्ट्रा न्त रात्
1 2 1 1 1 2 1 2 1 1 1 2 1 2 2 1 2

-------------------------------------------
syllables.php
  Not working
  uses exec_shell of php to run syllables.py

-------------------------------------------
syllables.html
web-page using javascript.
manual conversion of syllables.py to Javascript
