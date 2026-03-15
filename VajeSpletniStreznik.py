# var = complex (3.1)

# var 
# print (var)

# var_str = "1,2,3"
# var_array = [1,2,3]
# var_tuple = (1,2,3)

# var_array[0] = 2
# print (var_array)

# var_dict = {"faks" : "FERI", "mesto" : "Maribor"}
# var_dict["faks"]
# print (var_dict)


# var_set = {"ena", "dve"}
# var_set.add("tri")
# var_set.add("tri")
# var_set.add("tri")

# print (var_set)

# num = [1,2,3,4,5]

# print(num[1:4])

# print(num[1:4:2])

# print(num[5:-6:-1])

# event = [i for i in num if i%2 ==0]

# print(sorted((num[5:-6:-1])))


# num.append(6)
# print(num)

# print(num.index(3))

# num2 = num
# num2.append(7)
# print(num)

# s = "Hello World"
# print(s.upper())
# print(s.strip(),"a")

# print("elo" in s)

# s_list = "a,b,c,d"
# print(s_list.split(","))
# print([x.strip() for x in s_list.split(",")])

# abc = ['a', 'b', 'c']
# print("\n". join(abc))

# print(s+s)

# # a = [1,2,3]
# # for i in a:
# #     print(i)
# # for i in range(len(a)):
# #     print(a[i])
# # while True:
# #     if(i>3):
# #         break
# #     print(a[i])
# #     i+=1

# # a = [[1,2,3], [4,5,6]]
# # for i in a:
# #     for j in i:
# #         print(j)
# # for i in range(0,3):
# #     for j in range(0,3):
# #         print(a[i][j])
# a = 3
# if a<1:
#     print(0)
# elif a<2:
#     print(1)
# else:
#     print(2)

# def func(a,b,c = 19):
#     return max(a,b,c)
# a = 2
# print(func(a,1,2))


# def func(a):
#     a = a + a
#     print(a)
# a = 10
# print(func(a), a)


# def func(a):
#     a.append(10)
#     print(a)
# a = [10]
# func(a)
# print(a)

# def func(item, seznam=[]):
#     seznam.append(item)
#     return seznam
# func("a")
# func("a")
# print(func("a"))

# import math 

# math.sqrt(16)
# import math as m
# m.sqrt(16)
# from math import sqrt as s 
# s(16)

# from math import *
# sqrt(16)

# import traceback

# def age_ratio(age1, age2):
#     if age1 < 0 or age2 < 0:
#         raise ValueError("Age cannot be negative")
#     print(f"The age ratio is: {age1/age2}")

# try: 
#     age_ratio(0, 0)
# except ValueError as e:
#     print("error:", e)
#     traceback.print_exc()
# print('END')


# a = [1,2,3]

# B = A 
# print(id(A),id(B))


# x = 10
# y = x
# print(id(x), id(y))


# import gc
# import time 

# def log_execution_time(func):
#     print("starting")

#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         print(f"Finished in {time.time() - start_time} seconds")
#         return wrapper
    
#     def func(a):
#         print(a)
#     func(10)


# def cycle(n):
#     w = []
#     y = []
#     w.append(y)
#     y.append(w)
# cycle()
# gc.collect()  

# import sys
# a = [1,2,3]
# print(sys.getrefcount(a))
# gc.collect()
# print(b)

# class Car: 
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display_info(self):
#         print(f"Car make: {self.make}, model: {self.model}")

# avto1 = Car("Toyota", "Corolla", "red")


# ## Naloga 1

# playlist = ["Lo-Fi Beats", "Classic Rock", "Synthwave", "Jazz Fusion", "Techno", "Indie Pop"]

# 1. Skopirajte "playlist"
# 2. dodajte kopiji "Metal"
# 3. odstranite kopiji vse glasbene zvrsti, ki imajo v imenu več kot eno besedo
# 4. izpišite vse glasbene zvrsti, ki so v "playlist", ne pa v kopiji


playlist = ["Lo-Fi Beats", "Classic Rock", "Synthwave", "Jazz Fusion", "Techno", "Indie Pop"]

playlist_copy = playlist.copy()

playlist_copy.append("Metal")

kopija = [zanr for zanr in playlist_copy if len(zanr.split()) == 1]

for zanr in playlist:
    if zanr not in kopija:
        print(zanr)

print(kopija)
print(playlist_copy)

# ## Naloga 2
theater = [
    ['O', 'X', 'O', 'O'],  # Row 0
    ['X', 'X', 'O', 'X'],  # Row 1
    ['O', 'O', 'O', 'O']   # Row 2
]


theater_popravljeno = [list(vrstica) for vrstica in zip(*theater)]

for vrstica in theater_popravljeno:
    print(vrstica)


# Nekdo je zamešal vrstico in stolpec pri izdelavi aplikacije za sedežni red kinodvorane!

# Spremenite "theater" tako, da bo pravilno!


# ## Naloga 3

# Napišite funkcijo, ki posodablja zalogo v trgovini. Če predmet ne obstaja, ga ustvari. Zaloga se lahko polni in prazni (ne more pa iti pod nič!). Zgodovina se beleži kot "+-5 jabolk - uspešno/neuspešno."


zaloga = {"jabolka": 10, "banane": 5}
#zaloga.update({"ananas":20}}) za neposredno spreminjanje recimo

# Napišite funkciju koja ažurira zalihu u prodavnici. Ako predmet ne postoji, treba ga kreirati. Zaliha se može povećavati i smanjivati (ali ne može pasti ispod nule). Historija se bilježi u obliku: "+-5 jabuka - uspješno/neuspješno."

def posodobi_zalogo(artikel, kolicina, zgodovina=[]):
    
    pass
