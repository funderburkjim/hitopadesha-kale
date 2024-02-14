<?php
 echo "<p>hello, world</p>";
 $ans = `python syllables.py deva 'वाचां सर्वत्र वैचित्र्यं'`;
 if ($ans === false) {echo "answer is false";}
 if ($ans === null)  {echo "answer is null";}
 //$ans = shell_exec($command);
 echo "ans = $ans";
?>
