Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Q:- Create a list with user defined inputs.
>>> L=["Rajat","Ashish","Param","Naveen","Rajat"]
>>> L
['Rajat', 'Ashish', 'Param', 'Naveen', 'Rajat']
>>> # Q2:- Add the following list to above created list:
>>> # Way 1
>>> L.append(["Google","Apple","Facebook","Microsoft","Tesla","Ashish","Verna"])
>>> L
['Rajat', 'Ashish', 'Param', 'Naveen', 'Rajat', ['Google', 'Apple', 'Facebook', 'Microsoft', 'Tesla', 'Ashish', 'Verna']]
>>> # Way 2
>>> M=["Naveen","Ayush","Shivam"]
>>> M
['Naveen', 'Ayush', 'Shivam']
>>> L.append(M)
>>> L
['Rajat', 'Ashish', 'Param', 'Naveen', 'Rajat', ['Google', 'Apple', 'Facebook', 'Microsoft', 'Tesla', 'Ashish', 'Verna'], ['Naveen', 'Ayush', 'Shivam']]
>>> # Q3:- Count the number of time an object occurs in a list.
>>> L.count("Rajat")
2
>>> L.count("Naveen")
1
>>> # Q4:- Create a list with numbers and sort it in ascending order.
>>> Numeric=[5,8,2,4,1]
>>> Numeric
[5, 8, 2, 4, 1]
>>> Numeric.sort()
>>> Numeric
[1, 2, 4, 5, 8]
>>> # Q5:- Given are 2-D arrays NEW and OLD sorted in ascending order.Merge them into single sorted array TOTAL in ascending order.
>>> NEW=[15,2,8,5,11,13]
>>> NEW
[15, 2, 8, 5, 11, 13]
>>> NEW.sort()
>>> NEW
[2, 5, 8, 11, 13, 15]
>>> OLD=[1,14,3,10,9,4,7,12,6]
>>> OLD
[1, 14, 3, 10, 9, 4, 7, 12, 6]
>>> OLD.sort()
>>> OLD
[1, 3, 4, 6, 7, 9, 10, 12, 14]
>>> TOTAL=NEW+OLD
>>> TOTAL
[2, 5, 8, 11, 13, 15, 1, 3, 4, 6, 7, 9, 10, 12, 14]
>>> TOTAL.sort()
>>> TOTAL
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> 
