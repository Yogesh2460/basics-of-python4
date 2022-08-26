#lambda is used to create anonymous function i.e is used to create function ,use it and delete it
#map is used to map something
#reduce to cmp and get max valuew from it
""" all this can printed in shell
f=lambda a,b,c:(a*b)+c
f(10,6,4)
print(f)


big=lambda x,y:x if x>y else y
big(10,2)
print(big)
"""
"""
#three functions using lamdda
#map
t1=40,34,37,38
f=map(lambda x:float(9/5)*x+32,t1)
 for ele in f:
...    print(ele)
... 
104.0
93.2
98.60000000000001
100.4

#filter
fb=[0,1,1,2,3,5,8,13]
>>> result=filter(lambda x:x%2,fb)
 for ele in result:
...     print(ele)
... 
1
1
3
5
13
>>> result=filter(lambda x:x%2==0,fb)
>>> for ele in result:
...     print(ele)
... 
0
2
8

#reduce

l1=[12,14,5,64]
>>> import functools
>>> import functools as ft6
>>> ft6.reduce(lambda x,y:x if (x>y) else y,l1)
64
"""
# solution of assignment
fb=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x:x%2==0,fb)
f=map(lambda x:x**2,result)
for ele in f:
   print(ele)

"""	
1
9
25
49
81
>>> result=filter(lambda x:x%2==0,fb)
>>> f=map(lambda x:x**2,result)
>>> for ele in f:
	print ele

	
4
16
36
64
100
"""


#exceptions
 t=[1,2,3]
>>> pos=5
>>> try:
...    t(pos)
... except:
...    print("position is from 0 to 2")
... 
position is from 0 to 2

