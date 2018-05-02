# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:41:55 2018

@author: Daksh
"""

def mergesort(x):
    if len(x)<=1:
        return x
    else: m=len(x)//2
    a=mergesort(x[:m])
    b=mergesort(x[m:])
    return merge(a,b)

def merge(a,b):
    k=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            k.append(a[i])
            i=i+1
        else: 
            k.append(b[j])
            j=j+1
              
    if len(a)==i:
         k=k+b[j:]
    else: k=k+a[i:]
     
    return k
    
            
            
        
        