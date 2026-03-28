# var_bool = False
# print(var_bool*True)
# var_bool1 = True
# var_a = 5
# print(var_bool1*var_a)


# var_int = int(1.0)
# var_float = float(1.1)
# var_complex = complex(1.1 +1j) ## kompleksno stevilo
# print(f'int {var_int}, float {var_float}, complex {var_complex}')

# var_str = "1,2,3"
# var_Array = [1,2,3]
# var_tuple = (1,2,3)
# var_Array[0] = 10
# print(f'string {var_str}, array {var_Array}, tuple {var_tuple}')

#dictionary

# var_dic = {"faks":"FIS", "faks2":"FAMNIT"}
# var_dicAmer = {"Ime":"Amer", "Primek":"Cengic"}
# print(f'faks {var_dic["faks"]}, faks2 {var_dic["faks2"]}')
# print(f'Ime {var_dicAmer["Ime"]}, Primek {var_dicAmer["Primek"]}')

# var_set = {"ena","dve","tri"}
# var_set.add("štiri")
# var_set.add("pet")
# var_set.add("sedam")
# var_set.remove("dve")
# print(f'set {var_set}')

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def __str__(self):
#         return f'{self.name} {self.surname}'
# print(Person("Amer", "Cengic"))


# list manipulation

# nums = [1,2,3,4,5]

# print(nums[1:4]) # slicing
# print(nums[1:4:2]) # slicing with step
# print(nums[-1]) # reverse list

# nums = [1,2,3,4,5]
# reversed_nums = nums[::-1]
# print(reversed_nums)

# print(nums[::2]) # slicing with step, every second element

# evnts = [x for x in nums if x%2==0] # list comprehension, even numbers
# print(evnts)

# print(sorted(reversed_nums))

# nums.append(6)
# print(nums)

# print(nums.index(3))

# nums2= nums[:]
# nums2.append(7)
# print(nums,nums2)

# print(nums+nums2)

# print(nums*2)


#string manipulation

# s = "hello amer"
# d = " amer cengic "

# print(s.upper())

# print(d.strip())

# print("wis" in s) 

# s_list = "a ,b ,c ,d"
# print(s_list.split(","))
# print([x.strip() for x in s_list.split(",")])


# abc = ["a", "b", "c"]
# print("\n".join(abc))

# print(s+s_list)


# a = [1,2,3]

# for i in a:
#     print(i)
# for i in range(0,len(a)):
#     print(a[i])

# for i in range(1,3+1):
#     print(i)



# i = 1
# while i <= 4:
#     print(i)
#     i+=1

# while True:
#     if(i>6):
#         break
#     print(i)
#     i+=1

# 2D array 
# equivalent loops 
# a = [[1,2,3],[1,2,3]]

# for i in a:
#     for j in i:
#         print(j)
        
# print("\n")
# for i in range(0,len(a)):
#     for j in range(0,len(a[i])):
#         print(a[i][j])

# a = 0.4

# if a <1:
#     print(0)
# elif a <2:
#    print(1)
# else:
#    print(2)


# def func(a,b,c = 10):
#     return max(a,b,c)

# a = 0
# print(func(a,1))
# print(func(a,1,-1))

# def func(a):
#     a = a +a 
#     print(a)

# a = 1
# func(a)
# print(a)

# b = [1,2]
# func(b)
# print(b)

# name = input("what is your name")
# print(f"Hello, {name}")

# lines = ["Prvi stavek.\nDrugi stavek."]

# # 'w' is for writing, this creates file
# with open('text.txt', 'w') as file:
#     file.writelines(lines)
    
# # 'r' is for reading
# with open('text.txt', 'r') as file:
#     content = file.read()
#     print(content)

# import csv

# data = [
#     ['student_ID', 'Name', 'Family name'],
#     [1, 'Peter', 'FISer'],
#     [2, 'Nastja', 'de la FIS']
# ]

# #write csv
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
    
# #read csv
# with open('students.csv', 'r') as file:
#     reader = csv.DictReader(file) # Loads each row as a dictionary
#     for row in reader:
#         print(f"Student {row['student_ID']} is {row['Name']} {row['Family name']}")


import json

# # dictionary as input
# target_profile = {
#     "id": None,
#     "name": "Sarah Connor",
#     "isTerminated": False,
#     "params": [0, 170, 60],
#     "address": None
# }

# # convert from dict to JSON
# json_string = json.dumps(target_profile, indent=1)
# print(json_string)

# # Save to a .json file
# with open('target_profile.json', 'w') as file:
#     json.dump(target_profile, file, indent=4)

# with open('target_profile.json','r') as file:
#     data = json.load(file)


# print(f"{data['name']} was terminated: {data['isTerminated']}")

x = "outside"

def my_function():
    x = "inside" # This SHADOWS the global x
    print(f"{x}")

my_function()
print(f"{x}")
