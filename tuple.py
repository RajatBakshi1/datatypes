Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # TUPLE
>>> # Q1:- Create a tuple with different data types and do the following operations.
>>> Tuple1=(2,4,6,8,10)
>>> Tuple1
(2, 4, 6, 8, 10)
>>> type(Tuple1)
<class 'tuple'>
>>> Tuple2=('Rajat','Ashish','Param','Naveen','Sahil','Vedant')
>>> Tuple2
('Rajat', 'Ashish', 'Param', 'Naveen', 'Sahil', 'Vedant')
>>> type(Tuple2)
<class 'tuple'>
>>> # 1:- Find the length of tuples.
>>> len(Tuple1)
5
>>> len(Tuple2)
6
>>> # Q2:- Find largest and smallest elements of a tuples.
>>> max(Tuple1)
10
>>> min(Tuple1)
2
>>> # Q3:- Find the product of all elements of a tuple.
>>> Tuple1product=(2*4*6*8*10)
>>> Tuple1product
3840
>>> # SETS
>>> # Q1:- Create two set using user defined values.
>>> SetA={1,2,3,4,5,7}
>>> SetA
{1, 2, 3, 4, 5, 7}
>>> type(SetA)
<class 'set'>
>>> 7 in SetA
True
>>> SetB={2,5,4,7,,6,9,15}
SyntaxError: invalid syntax
>>> SetB={2,5,4,7,6,9,15}
>>> SetB
{2, 4, 5, 6, 7, 9, 15}
>>> 5 in SetB
True
>>> # 1:- Calculate difference between two sets.
>>> SetA-SetB
{1, 3}
>>> SetB-SetA
{9, 6, 15}
>>> # 2:- Compare two sets.
>>> SetA==SetB
False
>>> # 3:- Print the result of intersection of two sets.
>>> SetA & SetB
{2, 4, 5, 7}
>>> SetB & SetA
{2, 4, 5, 7}
>>> # DICTIONARIES
>>> # Q1:- Create a dictionary to store name and marks of 10 students by user input.
>>> Result={'Rajat':85,'Ashish':83,'Param':73,'Naveen':80,'Sahil':88,'Vedant':77,'Pritam':65,'Shivam':69,'Ayush':75,'Ravi':61}
>>> Result
{'Rajat': 85, 'Ashish': 83, 'Param': 73, 'Naveen': 80, 'Sahil': 88, 'Vedant': 77, 'Pritam': 65, 'Shivam': 69, 'Ayush': 75, 'Ravi': 61}
>>> # Q2:- Sort the dictionary created in previous question according to marks.
>>> sorted(Result.values())
[61, 65, 69, 73, 75, 77, 80, 83, 85, 88]
>>> # Q3:- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
>>> word="MISSISSIPPI"
>>> m=word.count("M")
>>> m
1
>>> i=word.count("I")
>>> i
4
>>> s=word.count("S")
>>> s
4
>>> p=word.count("P")
>>> p
2
>>> Store=dict()
>>> type(Store)
<class 'dict'>
>>> Store={'M':m,'I':i,'S':s,'P':p}
>>> Store
{'M': 1, 'I': 4, 'S': 4, 'P': 2}
>>> 
