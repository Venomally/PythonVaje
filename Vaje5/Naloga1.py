# U ovom zadatku simuliramo dijeljenje posla na workere. Za ovaj zadatak napravite svoj novi jedinstveni queue.

# (a) Napišite program koji šalje 10 poruka na vaš queue. Poruke neka budu nasumični brojevi između 5 i 15.
# (b) Napišite program za workera. Worker prima poruku u obliku broja N. Na osnovu tog broja nešto izvršava.

# Pošto nemamo stvarne zadatke, nemamo ni stvarni posao. Worker nakon primljene poruke treba sačekati N sekundi (broj koji je primio).

# Pobrinite se da se svi raspodijeljeni zadaci završe, čak i ako se neki od programa ugasi — koristite durable queue, durable poruke i manuelni acknowledgement.

# Svoj kod testirajte tako što ćete pokrenuti više workera (npr. 2) koji čitaju iz istog queue-a, te na queue šaljete poruke. Također, worker ne treba dobiti novi zadatak dok ne završi prethodni (prefetch count).
