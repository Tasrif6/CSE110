# -*- coding: utf-8 -*-
"""Lab Assignment 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aeCmkWuJ9TnMisrsUmHkBLcDAki6wnuw
"""

#Task-1: 
a_list=[]
for iteration in range(5):
       number=int(input('Sir, please enter your desire  number: '))
       a_list.append(number)
       print('Number in the list:', a_list)

#task-2:
a_list= []
for i in range (0,7):
    number= input("Enter the numbers: ")
    a_list.append(number)
new_list=[]
length=len(a_list)
if length>3:
    new_list=a_list[2:length-2]
    print(new_list)
elif length<=3:
    new_list=a_list[2:length-1]
    print(new_list)
else:
    print("Not possible")

#Task-3:
numbers=[5,-5,100,-1,0]
pos_index=len(numbers)-1
print('LAST INDEX', pos_index, 'LAST VAL', numbers[pos_index])

for interation in range(5):
      print('pos_index', pos_index, numbers[pos_index])
      pos_index=pos_index-1

#extra:
numbers=[5,-5,100,-1,0]
neg_index=-1  #for negative indexing
print('LAST INDEX', neg_index, 'LAST VAL', numbers[neg_index])

for interation in range(5):
      print('neg_index', neg_index, numbers[neg_index])
      neg_index=neg_index-1

#task-3:
a_list=[]
for i in range(0,5):
    number=input('Please enter your desired number: ')
    a_list.append(number)
print('Input data: ', a_list)
print('Printing values from the list in reverse order: ',)

length=-1
for count in range(0,5):
    print(length, a_list[length])
    length=length-1

#task-4:
a_list=[1, 2, 3, 4, 5, 6, 7]
b_list=[]
for i in range(len(a_list)):
   b_list.append(a_list[i]**2)
print(b_list)

#task-5:
a_list=["hey", "there", "", "what's", "", "up", "", "?"]
ans_list=[]
for i in range(len(a_list)):
       while("" in a_list):
          a_list.remove("")
print(a_list)

#task-5:
a_list=["hey", "there", "", "what's", "", "up", "", "?"]
b_list=[]
for i in range(len(a_list)):
  if len(a_list[i])>0:
      b_list.append(a_list[i])
  else: 
      pass
print(b_list)

#task-6:
my_list=[]
for x in range(0,5):
    user_input=int(input("Please enter your number: "))
    my_list.append(user_input)
maximum=my_list[0]
index=0
for k in range(0,5):
    if my_list[k]>maximum:
        maximum=my_list[k]
        index=k
    else:
        pass
print("My list:",my_list)        
print("Largest number in the list is",maximum,"which was found at index",index)

#task-7:
List_one = [1, 4, 7, 5]
List_two = [6, 1, 3, 9]
length=len(List_one)
new_list_xyz=List_one[0:length-1]
for i in range(len(List_two)):
    new_list_xyz.append(List_two[i])
print("Output is:",new_list_xyz)

#task-8:
list_1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2=[10, 11, 12, -13, -14, -15, -16]
new_list=[]
for i in range(0,len(list_1)):
    if list_1[i]%2==0:
        new_list.append(list_1[i])

for count in range(0,len(list_2)):
    if list_2[count]%2==0:
        new_list.append(list_2[count])
       
print(new_list)

#task-9:
a_list=[]
add=''
for i in range(0,10):
    number=input('Enter your word: ')
    a_list.append(number)
print('Modified list: ', a_list)
new_list=[]
length=len(a_list)
for count in range(0,length):
    if a_list[count]%2!=0:
        new_list.append(a_list[count])
    else:
        pass
print('Original list: ', new_list)

#task-9:
number=input()
a_list=[]
add=''
for i in range(0,10):
    if i!='':
        add+=i
    else:
        a_list.append(add)
        add=''
if add!='':
    a_list.append(add)
b_list=[int[i] for i in a_list]
print('a_list: ', b_list)
odd=[]
for i in b_list:
    if i%2!=0:
        odd.append[i]
print("Modified list: ", odd)

#task-10:
a_list=[]
for i in range(0,16):
    word=input('Please enter your desired number: ')
    a_list.append(word)
print('Input list: ', a_list)
b_list=[]
for i in range(len(a_list)):
    if a_list[i] not in b_list:
        b_list.append(a_list[i])
print('Modified list: ', b_list)

#task-11:
a_list=[1, 4, 3, 2, 6]
b_list=[5, 6, 9, 8, 7]

length=len(a_list)
for i in range(0,length):
    if a_list[i] not in b_list:
        print("True")
        break
    else:
        pass
    if i==length-1:
        print("False")

#task-12:
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0
index1 = 1
while(index1<10):
  myList[index1] = index1+4
  index2 = 1
  while(index2<index1):
      myList[index1] = myList[index1] + myList[index2]-index1
      index2 = index2+1
  print(myList[index1])
  index1 = index1+1

#task-13:
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0
index1 = 1
while (index1 < 10):
    myList[index1] = index1 + 4
    index2 = 1
    while (index2 < index1):
        myList[index1] = myList[index1-1] - myList[index2-1] - index1
        index2 = index2 + 1
    print(myList[index1])
    index1 = index1 + 1

#task-14:
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while(index1<10):
    myList[index1] = index1+2
    index2 = 1
    while(index2<index1):
        myList[index1] = b[index1]+myList[index2]-index1
        index2 = index2+1
    print(myList[index1])
    index1 = index1+1

#task-15:
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while (index1 < 10):
    myList[index1] = index1 + 1
    index2 = 1
    while (index2 < index1):
         myList[index1] = b[index2-1] + myList[index2] - index1
         index2 = index2 + 1
    print(myList[index1])
    index1 = index1 + 1

#task-19:
a_list=[1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
b_list=[1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
new_list=[]
for i in range(0,len(a_list)):
    if a_list[i] not in new_list:
        new_list.append(a_list[i])
for count in range(0, len(b_list)):
    if b_list[count] not in new_list:
        new_list.append(b_list[count])
print(new_list)

#task-20:
word=('1,   2 ,          3, 50, 4')
a_list=[]
for i in range(len(word)):
        
        a_list.append(word)
print(a_list)

#task-16:
my_list=[]
for x in range(0,7):
    user_input=int(input("Please enter your number: "))
    my_list.append(user_input)
print("My list:",my_list) 
maximum=my_list[0]
index=0
for k in range(2,7):
    if my_list[k]>maximum:
        maximum=my_list[k]
        index=k
    else:
        pass        
print("Second largest number in the list is",maximum,"which was found at index",index)

#task-18:
a_list=input()
b_list=input()
l=[(i)for i in a_list.split(',')]
k=[(i) for i in b_list.split(',')]

new_list=[]

for element in l:
    if element in k:
        new_list.append(element)
print(new_list)

#extra:
word=input()
add=''
count=0
for i in range(0,len(word)):
    if ord(word[i])>=48 and ord(word[i])<=57:
        var=chr(ord(word[i]))
        add=add+var
    elif ord(word[i])>=65 and ord(word[i])<=90:
        var=chr(ord(word[i])+32)
        add=add+var
    elif ord(word[i])>=97 and ord(word[i])<=122:
        var=chr(ord(word[i])-32)
        add=add+var
print(add)

for i in range(len(add)):
    if i==4:
        count=count+i
    else:
        pass
print(count)