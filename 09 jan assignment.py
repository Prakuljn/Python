# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hDhZOpnUB-7UnZ_JRquIvQEJD4Si8u65
"""

data= "prakuljain"
for i in range(len(data)):
    print(data[i])

str=input("enter the string: ")
for i in range(len(str)):
    if(str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        print(str[i])

count=0
str=input("enter the string: ")
for i in range(len(str)):
    if(str[i]!="a" or str[i]!="e" or str[i]!="i" or str[i]!="o" or str[i]!="u"):
      count+=1
print(count)

str=input("enter the string: ")
for i in range ((len(str))//2):
  print(str[i])

for i in range(1,21):
  if (i%3==0):
    continue
  else:
    print(i)

a=int(input("enter number to check prime or not: "))
b=0
for i in range(2,a):
  if(a%i==0):
    print("not prime")
    break
else:
  b+=1
if(b==1):
  print("prime")

# while loop
''' we use for for loop for finite iritatetation
    while for infinite iteration '''

a=0
b=1
while a<5:
  if(b%3==0):
    print(b)
    a+=1
  b+=1

a=8
b=a
while a<100:
  a=a+b
  b+=1
  print(b)

