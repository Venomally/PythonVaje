import re
import sys

# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

# print("Enter valid email")
# user_input = input()
# if(re.search(pattern, user_input)):
#     print("valid email")
# else:
#     print("invalid email")

# p = re.compile('\\\\next')
# m = p.match('\\next')
# print(m)


# p = re.compile(r'\\next')
# m = p.match(r'\next')
# print(m)

# p = re.compile(r'.*abc')
# m = p.match(r'abcdadadsdasd')
# print(m)


# print(m.group(), m.start(),m.end(),m.span())


# p = re.compile('ab*', re.IGNORECASE)
# m = p.match('AB')
# print(m)


# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))


# s = '<html><head><title>Title</title>'
# print(re.match('<.*>', s))
# print(re.match('<.*?>', s))


# import re 

# patten = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
# new_pattern = r"\1\2\3"
# user_input = input()
# new_user_input = re.sub(patten,new_pattern,user_input)
# print(new_user_input)


# p = re.compile('(a(b)c)d')
# m = p.match('abcd')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))


# p = re.compile('(ted)(ajble)')
# m = p.match('tedajble')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# p = re.compile(r'\b(\w+)\s+\1\b')
# m = p.search('Paris in the the spring')

# print(m.group(0))  
# print(m.group(1))  

# p = re.compile(r'(?P<word> hello) world')
# m = p.search('hello hello world')
# print(m.group('word'))
# print(m.group(1))
# print(m.group(0))


# p = re.compile(r'(?P<dan>\d\d)-(?P<mjesec>\d\d)-(?P<godina>\d\d\d\d)')
# m = p.search('25-12-2024')

# print(m.group('dan'))     # 25
# print(m.group('mjesec'))  # 12
# print(m.group('godina'))  # 2024


# m = re.match("([abc])+", "abc")
# print(m.groups())
# print(m.group(0))
# print(m.group(1))


# p = re.compile(r'\d+(?= dollars)')
# m = p.search('100 dollars')

# print(m.group(0))

# p = re.compile(r'\d+(?! euro)')
# m = p.search('200 dolar')

# print(m.group(0))

# p = re.compile(r'(?<=€)\d+')
# m = p.search('€100')

# print(m.group(0))  


# p = re.compile(r'(?!=€)\d+')
# m = p.search('100 euro')


# print(m.group(0))  



# brojevi = ['€100','£400','$200','£400','€500','€200']


# for broj in brojevi:
#     p = re.compile(r'(?<=€)\d+')
#     m = p.search(broj)

#     if m:
#         print(f"Pronašao euro iznos: {m.group(0)}")
#     else:
#         print(f"Nije euro: {broj}")


# p = re.compile(r'.*[.](?!bat$|exe$)([^.]*)$')
# m = p.search('ah.bat.exe.wow.pdf')
# m = p.search('document.bat')
# m = p.search('document.exe')


# if m:
#     print(m.groups())
# else:
#     print('Empty!')


# fajlovi = ['dokument.pdf', 'program.exe', 'skripta.bat', 'slika.jpg', 'music.mp3']

# for fajl in fajlovi:
#     p = re.compile(r'.*\.(?!bat$|exe$)([^.]+)$')
#     m = p.search(fajl)
    
#     if m:
#         print(f"{fajl} → ekstenzija: {m.group(1)}")
#     else:
#         print(f"{fajl} → BLOKIRAN! ❌")


p = re.compile(r'\b(?:(?<=and)\s|^|\.\s)([a-z]+)', re.IGNORECASE)
m = p.findall('Buying chesse AND salami AND wine AND bread. Soup AND veggies.')
print(m)

