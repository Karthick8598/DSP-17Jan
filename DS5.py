# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:12:17 2021

@author: vikas
"""

teamA = ['India', 'Australia','Pakistan', 'England']   # 4elements   list index 0-3


for i in teamA:
    print (i)



for i in range(len(teamA)):
    print (teamA[i])



r1 = range(1,11)

for i in range(1,11):
    print ('2 * ' + str(i) + ' = '  + str(2*i))
    
    

for j in range(1,11):    
    for i in range(1,11):
        print (str(j) + ' * ' + str(i) + ' = '  + str(j*i))
        

teamA

for i in teamA:
    if i == 'Pakistan' :
        print(i , "Inner")
        break
    print(i, "Outer")

print("end")

    
   
for i in teamA:
    if i == 'Pakistan' :
        print(i , "Inner")
        continue
    print(i, "Outer")

print ('end')




for i in teamA:
    if i == 'Australia_A' :
        print(i , "Inner")
        pass
    print(i, "Outer")
    
    
    
for j in range(1,6):    
    for i in range(1,6):
        print(i)
        if(i==3):
            print ('breaki')
            break
        




while (False):
    print("infinite")



cnt = 1
while (cnt<=10):
    print(cnt)
    cnt = cnt + 1


cnt = 1
while (True):
    print(cnt)
    cnt = cnt + 1
    if (cnt>10):
        break

















    
    
