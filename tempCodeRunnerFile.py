# ## Naloga 1

# playlist = ["Lo-Fi Beats", "Classic Rock", "Synthwave", "Jazz Fusion", "Techno", "Indie Pop"]

# 1. Skopirajte "playlist"
# 2. dodajte kopiji "Metal"
# 3. odstranite kopiji vse glasbene zvrsti, ki imajo v imenu več kot eno besedo
# 4. izpišite vse glasbene zvrsti, ki so v "playlist", ne pa v kopiji

#1. Skopirajte "playlist"
playlist = ["Lo-Fi Beats", "Classic Rock", "Synthwave", "Jazz Fusion", "Techno", "Indie Pop"]

copy = playlist[:]

# 2. dodajte kopiji "Metal"
playlist.append("Metal")

print("Original playlist:", copy)
print("Copied playlist:", copy)

# 3. odstranite kopiji vse glasbene zvrsti, ki imajo v imenu več kot eno besedo


playlist = [genere for genere in playlist if len(genere.split()) == 1]
print("Original playlist after removing genres with more than one word:", playlist)
# 4. izpišite vse glasbene zvrsti, ki so v "playlist", ne pa v kopiji

unique_genres = [genere for genere in playlist if genere not in copy]
print("Genres in playlist but not in playlist_copy:", unique_genres)
