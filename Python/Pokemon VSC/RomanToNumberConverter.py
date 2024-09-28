# def RNC(roman):
#     roman_numerals_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
#     count, add, prev = 0
#     for i in range(len(roman)):
#         for x in range(len(roman_numerals_dict)):
#             if roman[i] == list(roman_numerals_dict.keys())[x]:
#                 count += list(roman_numerals_dict.values())[x]
#                 prev = add
#                 add = list(roman_numerals_dict.values())[x]
#                 if prev < add and i != 0:
#                     count -= prev * 2
#     return count
# roman = input('')
# number = RNC(roman)
# print(number)

# text = input("")
# def reverse(text):
#     new_text = text[:: -1]
#     return new_text
# palindrome = reverse(text) 
# print(palindrome)

# try:
#     x = open('words.txt')
# except(FileNotFoundError):
#     print('No such file exists')

def factorial(number):
    new_number = 1
    for i in range(0, number):
        new_number *= number - i
    return new_number
    factorial(5)
    

a = int(input('What number do you want to factorilize: '))
b = factorial(a)
print(b)
from functools import reduce
print(reduce(lambda x, y: x*y,list(range(1,6)), 1))