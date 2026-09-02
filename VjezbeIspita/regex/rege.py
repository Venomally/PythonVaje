import re 

# with open("bibliografija.txt", "r", encoding="utf-8") as f:
#     sadrzaj = f.read()

# unosi = re.findall(r"@\w+\s*\{[^}]+\}", sadrzaj)

# brojac_bez_volime = 0
# for unos in unosi:
#     if not re.search(r"\bvolume\b",unos):
#         brojac_bez_volime += 1

# print("Broj unosa koji nemaju 'volumen' : "
#       f"{brojac_bez_volime}"

#       )

with open("bibliografija.txt", "r", encoding="utf-8") as f:
    sadrzaj = f.read()
unosi = re.findall(r"@\w+\s*\{[^}]+\}", sadrzaj)

brojac_bez_volumena = 0

for unos in unosi:
    if(not re.search(r"\bvolume\b", unos)):
        brojac_bez_volumena +=1

print("Broj unosa koji nemaju 'volumen' :"
       f"{brojac_bez_volumena}"
      )
