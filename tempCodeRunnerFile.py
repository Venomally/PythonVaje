# ## Naloga 1

# playlist = ["Lo-Fi Beats", "Classic Rock", "Synthwave", "Jazz Fusion", "Techno", "Indie Pop"]

# 1. Skopirajte "playlist"
# 2. dodajte kopiji "Metal"
# 3. odstranite kopiji vse glasbene zvrsti, ki imajo v imenu več kot eno besedo
# 4. izpišite vse glasbene zvrsti, ki so v "playlist", ne pa v kopiji

#1. Skopirajte "playlist"
# playlist = ["Lo-Fi Beats", "Classic Rock", "Synthwave", "Jazz Fusion", "Techno", "Indie Pop"]

# copy = playlist[:]

# # 2. dodajte kopiji "Metal"
# playlist.append("Metal")

# print("Original playlist:", copy)
# print("Copied playlist:", copy)

# # 3. odstranite kopiji vse glasbene zvrsti, ki imajo v imenu več kot eno besedo


# playlist = [genere for genere in playlist if len(genere.split()) == 1]
# print("Original playlist after removing genres with more than one word:", playlist)
# # 4. izpišite vse glasbene zvrsti, ki so v "playlist", ne pa v kopiji

# unique_genres = [genere for genere in playlist if genere not in copy]
# print("Genres in playlist but not in playlist_copy:", unique_genres)


# ## Naloga 2


# Nekdo je zamešal vrstico in stolpec pri izdelavi aplikacije za sedežni red kinodvorane!

# Spremenite "theater" tako, da bo pravilno!

# theater = [
#     ['O', 'X', 'O', 'O'],  # Row 0
#     ['X', 'X', 'O', 'X'],  # Row 1
#     ['O', 'O', 'O', 'O']   # Row 2
# ]
# dim_1 = len(theater)
# dim_2 = len(theater[0])
# #ustvarimo prazno matriko pravilnih dimenzij
# theater2 = [[0 for i in range(dim_1)] for j in range(dim_2)]

        
# for i in range(0, len(theater)):
#     for j in range(0, len(theater[i])):
#         theater2[j][i] = theater[i][j]
        
# print(theater)
# print(theater2)

# #ali pa hitreje!
# theater3 = [list(vrstica) for vrstica in zip(*theater)]
# print(theater3)


## Naloga 3

# Napišite funkcijo, ki posodablja zalogo v trgovini. Če predmet ne obstaja, ga ustvari. Zaloga se lahko polni in prazni (ne more pa iti pod nič!). Zgodovina se beleži kot "+-5 jabolk - uspešno/neuspešno."

