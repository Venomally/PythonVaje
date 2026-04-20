import requests
import json
import numpy as np
import matplotlib.pyplot as plt

# Podatke dobimo z response
# v ozadju je HTTP GET
response = requests.get('https://api.sledilnik.org/api/stats')

# Spravimo jih v json format iz suroave oblike (če ni JSON itak javi error)
res = response.json()

#prešteje, koliko testov je bilo pozitivnih za vsak dan posebej
pozitivni = [res[i]['tests']['positive']['today'] if 'today' in res[i]['tests']['positive'] else 0 for i in range(0,len(res)-1)]
#kateri dan je bil
dan = [res[i]['dayFromStart'] for i in range(0,len(res)-1)]

#izrišemo rezultat
plt.plot(dan,pozitivni)

#koliko ljudi je zbolelo v MB za vsak dan posebej
mb_oboleli = [res[i]['statePerRegion']['mb']  for i in range(0,len(res)-1)]
#pretvorimo v numpy array, da lahko naredimo np.diff
mb_oboleli = np.array(mb_oboleli, dtype=float)
#np.diff naredi razliko med 2. in 1. dnem, med 3. in 2. dnem itd.
mb_oboleli = np.diff(mb_oboleli)


#naredimo tedensko povprecje
tedensko_povprecje = [np.average(mb_oboleli[i:i+7]) for i in range(0,len(mb_oboleli))]
#narišemo
plt.plot(tedensko_povprecje)
   