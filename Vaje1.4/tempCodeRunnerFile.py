import re 
import sys
print(sys.version)

# p = re.compile(r'\b(?:(?<=and)\s|^|\.\s)([a-z]+)', re.IGNORECASE)
# m = p.findall('Buying chesse AND salami AND wine AND bread.Soup AND veggies. ')
# print(m)



# p = re.compile(r'(^\w+\b)|and\s*(\b\w+\b)|[.]\s+(\b\w+\b)', re.IGNORECASE)
# m = p.findall('Buying chesse AND salami AND wine AND bread.Soup AND veggies.')
# print(m)

# p = re.compile(r'\b([aeiou][a-z]*[^aeiou.])(?:\s|$|[.])', re.IGNORECASE)
# m = p.findall('ABC ded aba UEB AOB. aaa ded aba UEB aoa.')
# print(m)


# p = re.compile(r'.')
# m = p.findall('a.b!c')
# print(m)

# p = re.compile(r'\.')
# t = p.findall('a.b!c')
# print(t)


# p = re.compile(r'[.]')
# m = p.findall('a.b!c')
# print(m)


# p = re.compile(r'\d+')
# t = p.findall('Imam 2 jabuke i 15 krušaka, te 300 grama šećera.')
# print(t)


# p = re.compile(r'\b\w+\b')
# t = p.findall('Imam 2 jabuke i 15 krušaka, te 300 grama šećera.')
# print(t)



# p = re.compile(r'(?<=\().*?(?=\))',re.IGNORECASE)
# m = p.findall('Tezka naloga (3.naloga) je tezka ampak ni tako tezka kot (prva) naloga.')
# print(m)


# p = re.compile(r'([1-9])([1-9])([1-9])(\2)(\1)', re.IGNORECASE)
# m = p.findall('12321 balsadas dsaa  11111 spijdsodsdsoi98789 as21234 ')
# print(m)


p = re.compile(r'(?<![1-9])(.{3,3})(?![1-9])',re.IGNORECASE)
m = p.findall('12321balsadasdsaa11111spijdsodsdsoi98789 as21234 ')
print(m)
