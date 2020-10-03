# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:47:15 2020

@author: sri
"""

# Python prog to illustrate the following in a list 
def find_len(list1): 
	length = len(list1) 
	list1.sort()
	print("Largest element is:", list1[length-1]) 
	print("Smallest element is:", list1[0]) 
	print("Second Largest element is:", list1[length-2]) 
	print("Second Smallest element is:", list1[1]) 

# Driver Code 
list1=[]
c=[]
list1=input().split()
length=len(list1)
for i in range(length):
        last=int(list1[i])
        c.append(last)
Largest = find_len(c) 
