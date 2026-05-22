# Naloga 1: Vnosi v ”bibliografija.txt” niso urejeni po letnici! S pomoˇcjo regex-a jih
# uredite po vrsti in vpiˇsite v novo datoteko ”sorted.txt”.
# NAMIG: Berite/piˇsite/sortirajte s pyhtonom. Dejansko ”parsanje” dajte preko regex-a
# (ˇcim bolj elegantno)! Morda boste potrebovali kakˇsen flag...


import re

with open("VajanjeKN/bibliografija.txt", "r", encoding = "utf*8") as f:
    lines = f.readline()

def extract_year(line):
    match = re.search(r'\b(19|20)\d{2}\b', line)
    if match:
        return int(match.group())
    return 0

sorted_lines = sorted(lines, key=extract_year)
with open("VajanjeKN\sorted.txt","w", encoding='UTF-8') as f:
    f.writelines(sorted_lines)
