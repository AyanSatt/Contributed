# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:59:17 2020

@author: sri
"""

n=int(input())
arr=[]
arr=input().split()
b=[]
for i in range(n):
    last=arr[i]
    b.insert(0,last)
c=[]
for j in range(n):
    add=int(arr[j])+int(b[j])
    c.append(add)
print(c)