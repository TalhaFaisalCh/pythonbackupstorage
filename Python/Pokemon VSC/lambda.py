li = list(range(1, 101))
li = {i:'odd' if i%2 == 1 else 'even' for i in li}
#print(li)
my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
#my_dict = {my_dict.keys == my_dict.values:my_dict.values == my_dict.keys}
print(my_dict.items())
word = 'word'
word = [w for w in word if w in 'aeiouAEIOU' ] 
print(word)
sentence = 'This is a sentence while YOU are not you little peasant'
words = sentence.split()
print(words)
words = [s for s in words if len(s) % 2 == 0]
print(words)
words = ["apple", "banana", "grape", "orange", "peach"]
words = [s.upper() for s in words if s.startswith('a')]
print(words)
words = ["apple", "banana", "grape", "orange", "peach"]
words = [s.upper() for s in words]
print(words)
mydict2 = {}
my_dict = {'a':1,'b':2,'c':3, 'd':4, 'e':5, 'f':6}
print(my_dict.items())
mydict2 = {v : k for k, v in my_dict.items()}
print(mydict2.items())
mydicteven = {i:my_dict[i] for i in my_dict.keys() if my_dict[i] % 2 == 0}
print(mydicteven)
original_dict = {'apple':3,'banana':5,'orange':2}
original_dict = {i for i in original_dict.keys()}
print(original_dict)
original_dict = {'apple':3,'banana':5,'orange':2}
original_dict =  {i:'high'for i in original_dict.keys() if original_dict[i] >= 3}
print(original_dict)
original_dict = {'apple':3,'banana':5,'orange':2}
original_dict =  [i for i in original_dict.keys() if i.startswith('a')]
print(original_dict)
original_dict = {'apple':3,'banana':5,'orange':2}
original_dict =  {i:str(original_dict[i]) for i in original_dict.keys()}
print(original_dict)

print([(x, y) for x in range(0, 5) for y in range(0,5)])

































