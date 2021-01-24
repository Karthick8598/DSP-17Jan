# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:55:17 2021

@author: vikas
"""

#List, Tuple, Set, Dictionary, FrozenSet, Enumerate, String, Zip

# Hetrogeneous

# array = [1,2,3,4,5,7] Hemogeneous

# array = [1,1.3,True, 'string'] Hetrogeneous

# Mutable or Changeable

# Ordered or Unordered

# Indexed
'''
a=10
b=20
c=30

L1 = [10,20,30]
'''


#List

L1 = [2,1,3,4]

type(L1)

print (L1)

#Unordered


L2 = ['Vikas', True, 1, 5.6] #Iterative Element
L2

a = 10

#Hetrogeneous


L2
L2[0]
L2[1]
L2[2]
L2[3]
L2[4] #IndexError: list index out of range

#Indexed

'''
for i in L2
{
  print(i) 
}

'''

# Iterative

for i in L2:
    print (i) #Intendation
    
len(L2)

r1 = range(50)
r1
type(r1)

lr1 = list(r1)
len(lr1)


r1 = range(10, 50)
r1
type(r1)

lr1 = list(r1)
lr1


r1 = range(10, 50, 5)
r1

type(r1)

lr1 = list(r1)
lr1


for i in lr1:
    print (i)



r1 = range(50, 10, -5)
r1

type(r1)

lr1 = list(r1)
lr1

lr1[0:4]
lr1[2:6]
lr1[:4]
lr1[3:]
lr1[2:5]
lr1
lr1[::2]
lr1[1:5:2]
lr1[::-1]
lr1
lr1[-1]
lr1[-3:-1]


len(lr1)

sum(lr1)

lr1 = [10, 15, 20, 25, 10, 15, 10, 45]

lr1.count(15)


#Mutable

lr1[1] = 55
lr1


lr1.append(60)
lr1

#lr1.remove([55,10])

a = lr1.remove(10)
lr1
a

b = lr1.pop()
b
lr1

c = lr1.pop(3)
c
lr1

del lr1[0]
lr1

del lr1[0]

del lr1
lr1


lr1 = [10, 15, 20, 25, 10, 15, 10, 45]

lr1.clear()
lr1

lr2 =  list(range(10,20))

lr2

lr1=[]
for i in lr2:
    lr1.append(i)
    print(lr1)


lr1

lr3 = lr1

print (lr3)
print(lr1)

lr1.append(20)

print (lr3)
print(lr1)


lr3 = lr1.copy()

print (lr3)
print(lr1)

lr1.append(20)

print (lr3)
print(lr1)

lr1 = [20, 13, 12, 11, 17, 16, 19, 18, 15, 14,  10]
lr1
lr1.reverse()
lr1

lr1.sort()
lr1.reverse()
lr1 = lr1[::-1]
lr1


'''
def rev(lr1):
    return(lr1[::-1])
    
lr1
print (rev(lr1))
'''

fruits = ['apple', 'cherry', 'banana']

fruits

fruits.insert(1,'mango')
fruits



#Set

#Not allow Duplicate Elements

s1 = {1,2,3,6}
type(s1)

s1

#Hetrog

s2= {'Vikas', True, 20, 7.44}

s2

# Not Indexed

s2[0] #TypeError: 'set' object is not subscriptable


s3 = {2,6,3,5,7}
s3

#Ordered #To remove Duplicate


for i in s3:
    print(i)


#Mutable

s3.add(4)
s3

#Unique

s3.add(5)
s3


s3.update([10,20])
s3

s3.remove(10)
s3

s3.remove(10) #KeyError: 10

s3.discard(20)

s3

s3.discard(20)
s3

s3.pop()

s3.pop(1) #TypeError: pop() takes no arguments (1 given)

s3.clear()

s3

del s3
s3


teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}
teamC = {'West Indies', 'India'}


teamA.union(teamB)

teamA.intersection(teamB)

teamC = teamA.difference(teamB)





teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}
teamC = {'West Indies', 'India'}

teamD = teamA.union(teamB)
teamE = teamD.union(teamC)


# Dictionary

#Key:Value pair

student = {'roll':1, 'name':'Vikas' }

student

type(student)


car = {'brand':'Honda', 'model': 'Jazz', 'year' : 2017}
car

#Access
car['brand']
car.get('brand')
car['year']


# Return Keys
for i in car:
    print(i)


for i in car:
    print(car[i])


car.values()
car.keys()
car.items()

for i in car.items():
    print(i)



for i, j in car.items():
    print(i)
    print(j)


len(car)


'model' in car
'model1' in car


#Mutable

car['year'] = 2000
car


car.pop() #TypeError: pop expected at least 1 argument, got 0

car.pop('year')
car

car['color'] = 'Black'
car

car.popitem()

car

car.clear()
car

del car
car



roll = list(range(1,6))

marks1 = [90,66,88,44,33]

marks2 = [50,36,58,64,43]

d1 = {'rno': roll, 'm1':marks1, 'm2': marks2}
d1




# Tuple

t1 = (2,3,1,5,6)

#Hetro

t2 = ('Vikas', True, 2, 4.3)

#Unordered

print(t1)

#Indexed

t1[0]
t1[3]

t1[5] #IndexError: tuple index out of range


#Not Mutable or not chag


t1[0] = 10 #TypeError: 'tuple' object does not support item assignment


for i in t1:
    print (i)


t1.append(1) #AttributeError: 'tuple' object has no attribute 'append'

t1.remove() #AttributeError: 'tuple' object has no attribute 'remove'

del t1

t1



l1 = [100, 200, 300, 400]

l1

for i in l1:
    print (i)


for i in l1:
    print (i)



e1 = enumerate(l1)
type(e1)
e1

for i in e1:
    print(i)


for i in e1:
    print(i)

l1

e2 = enumerate(l1, 10)
e2


for i in e2:
    print(i)


le2 = list(e2)
le2

le2[0]



for i,j in le2:
    print (i)
    print (j)



e3 = enumerate (range(1000, 1100))

list(e3)


cnt =0
for i in e3:
    print (i)
    cnt=cnt+1
    if (cnt>=50):
        break



for i in e3:
    print(i)



l1=[]

e4 =enumerate(range(0,5))

cnt=0
for i in e4:
    cnt=cnt+1
    l1.append(i[1])
    if (cnt==3):
        break

l1

for i in e4:
    l1.append(i[1])

l1





#Frozen Sets

#Not Changeble Type of Set

fs1 = frozenset([1,2,3])

s1 = {4,5,6}
s1.pop()

fs1.pop()

s1.add(5)
s1

fs1.add(3)

fs2 = frozenset([6,8,9])

fs1.union(fs2)

fs1.union(s1)




# Zip

name = [ "Virat", "Shikhar", "Ravi", "Rahul" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 


z1 = zip(name, roll_no, marks)

z1

list(z1)


for i in z1:
    print (i)




# Zipped to normal


z2 = zip(name, roll_no, marks)

z2



name1, rno1, marks1 = zip(*z2)
name1
rno1
marks1







































































































































































































