'''
Created on Jul 7, 2014

@author: root

How to join two sets in one line in Python?

¿Cómo unir dos conjuntos en una línea en Python?

union(other, ...)
set | other | ...
Return a new set with elements from the set and all others.
'''

#Create a set with values.
s = {0,1,2,3}
print(s)

s2 = {5,6}
print(s2)

#linking two sets
u = s.union(s2)
print(u)

#But be careful because, if are some values equal this values 
#are eliminated in the new set.
s3 = {0,1,4}
u = s.union(s3)
print(u)

#You can use pipe "|"
u = s | s3
print(u)