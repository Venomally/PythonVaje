
import json
import requests
import numpy as np
import matplotlib.pyplot as plt

# Preuzimanje podataka
response = requests.get('https://api.sledilnik.org/api/stats')
res = response.json()

# Testni podaci (primjer)
datum = [1, 2, 3]
stevilo_primerov_dnevno = [3, 2, 3]
plt.plot(datum, stevilo_primerov_dnevno, '.')

# Prikaz dijela podataka (pozitivni testovi)
plt.plot([res[i]['tests']['positive']['today'] for i in range(200, 300)])

# Prebroji koliko je bilo pozitivnih testova po danima
pozitivni = [
    res[i]['tests']['positive']['today']
    if 'today' in res[i]['tests']['positive'] else 0
    for i in range(0, len(res) - 1)
]

# Koji dan je bio
dan = [res[i]['dayFromStart'] for i in range(0, len(res) - 1)]

# Crtanje grafa
plt.plot(dan, pozitivni)
plt.show()

# Podaci po regijama (Maribor - 'mb')
plt.figure()
plt.plot([res[i]['statePerRegion']['mb'] for i in range(200, 300)])
plt.show()

# Primjer kumulativnog računa
dan1 = 10
dan2 = 20
dan3 = 30

kumulativa_na_treci_dan = dan1 + dan2 + dan3
kumulativa_na_drugi_dan = dan1 + dan2

primerov_na_treci_dan = kumulativa_na_treci_dan - kumulativa_na_drugi_dan

print(primerov_na_treci_dan)
