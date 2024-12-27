#1-misol
# class Student:
#     def __init__(self, student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name
#     def get_info(self):
#         return f'Student id = {self.student_id}, Student ismi {self.student_name}, Sinfining nomi {self.class_name}'
    
# a = Student(2, 'Ali', 'alo')
# print(Student.get_info(a))

#2-misol
# import json
# python_obj = {
# "name": "David",
# "class":"I",
# "age": 6
# }
# json_obj = json.dumps(python_obj, indent=4)
# print(json_obj)

#3-misol
# import datetime
# sana1_str = (input('Birinchi sanani kiriting (YYYY-MM-DD): '))
# sana2_str = (input('Ikkinchi sanani kiriting (YYYY-MM-DD): '))
# sana1 = datetime.datetime.strptime(sana1_str, '%Y-%m-%d')
# sana2 = datetime.datetime.strptime(sana2_str, '%Y-%m-%d')
# print((sana2 - sana1).days)

#5-misol
# import datetime
# kun = datetime.datetime.now()
# bugun = kun.strftime('%d')
# kecha = kun - datetime.timedelta(days=1)
# ertaga = kun + datetime.timedelta(days=1)
# print(bugun, kecha, ertaga)

#6-misol
# L = [2, 2, 3, 4, 5]
# kub = list(map(lambda x: x ** 3, L))
# print(kub)

#8-misol
# son = int(input('Son kiriting: '))
# result = []
# for i in range(2, son):
#     for j in range(2, int(son/2)):
#         if i % j == 0:
#             break
#     else:
#         result.append(i)
#         print(result)

#9-misol
# text = 'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.Its design philosophy emphasizes code readability'
# ozgargan_text = text.replace('a', '9')
# print(ozgargan_text)

#10-misol
# matn1 = input('Birinchi matnni kirting: )
# matn2 = input('Ikkinchi matnni kirting: )
# if len(matn1) > len(matn2):
#     max_str = matn1
#     min_str = matn2
# else:
#         max_str = matn2
#         min_str = matn1

# max_i = 0
# min_i = 0
# difference = 0
# while difference <= 1 and min_i < len(min_str) and max_i < len(max_str):
#         if len(max_str) == len(min_str) + 1:
#                 if max_str[max_i] == min_str[min_i]: 
#                         max_i += 1
#                         min_i += 1
#                 else:  
#                         difference += 1
#                         max_i += 1
#         elif len(max_str) == len(min_str):
#                 if max_str[max_i] == min_str[min_i]: 
#                         max_i += 1
#                         min_i += 1
#                 else:  
#                         difference += 1
#                         max_i += 1
#                         min_i += 1
#         else:
#               break
# if difference <= 1:
#         print(True)
# else:
#         print(False)