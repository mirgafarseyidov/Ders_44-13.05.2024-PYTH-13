"""

Taskınız sadə bir task olacaq, gecikmə səbəbiylə

Bir funksiyanız olacaq, funksiyada random kitabxanadan istifadə edərək 20 nən 50 arası 
5 rəqəm listə append edin. Həmən listdəki cüt  rəqəmləri math kitabxanası istifadə edərək 
kvadrata yüksəldin.

"""


import math
import random

def cüt_eded_kvadratlar():
    
    random_cüt_rəqəmlər = [num for num in random.sample(range(20, 51, 2), 5)]
    

    kvadratlar = [math.pow(num, 2) for num in random_cüt_rəqəmlər]
    
    return kvadratlar


print(cüt_eded_kvadratlar())