# -*- coding: utf-8 -*-
"""Lab Assignment 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kkjmQEr8qGNKfkUSNxgxjEt0mqHiPVnP
"""

print('Hello This is Tasrif coding....')

user_given=input('CSE110')
index= len(user_given)

loop: index
print(user_given)

user_input= input('Please enter a string: ')
index= len(user_input)-1

while index!=-1:
      print(user_input[index], end='')
      index= index-1

#to do-1
user_given= input(' Please enter your string: ')
index= len(user_given)-1
while index!=-1:
      print(user_given[index], end='')
      index=index-1

#to do-2
my_str=input('Please enter your number: ')
index=int(input())
count= index
ans=''
while count!=-1:
  ans=ans+my_str[count]
  count=count-1
ans=ans+my_str[index+1:]
print(ans)

#to do-3

number = input("Enter something: ")
count = 0
length = 0
for i in number:
    if i == "0" or i == "1":
        count+=1
        length+=1
if count == len(x) and length == len(x):
  print("Binary num")
else:
  print("Not a binary num")

#to do-3
number= input("Enter something: ")
count = 0

for i in number:
  if i != "0" and i != "1":
    count+=1
if count==0 or count==1:
  print('Binary number')
else:
  print("Not a binary num")

#to do-4
word=input("Enter your word: ")
length=len(word)
output=""

if length<4:
    output=word
elif length>3:
    if (word.endswith("er")):
        output=word[:length-2]
        output=output+"est"
    elif (word.endswith("est")):
         output=word
    else:
         output=word+"er"
print(output)

#to do-5
user_input=input("Enter a word: ")

for row in range(0,len(user_input)):
    for coloumn in range(0,row+1):
        print(user_input[coloumn],end="")
    print()

#to do-6
word=input("Enter ur word: ")
for count in range(0,len(word)):
    convert=ord(word[count])
    char=chr(convert)
    print(char,":",convert)

#to do-7

word=input("Enter a word: ")
for count in range(0,len(word)):
    if word[count]=="z":
        print("a",end="")
    else:
        convert=ord(word[count])+1
        print(chr(convert),end="")

#to do-8

word_input=input("Enter a word: ")
add=""
for count in range(0,len(word_input)):
    if count%2==0:
         pass
    else:
        result=ord(word_input[count])-32
        character=chr(result)
        add=add+character
print("Output is:",add)

#to do-9
word=input("Enter word: ")
add=word[0]
for count in range(1,len(word)):
    if(word[count])!=(word[count-1]):
        add=add+word[count]
print("Output is: ",add)

#todo-10
word_1=input("Enter first word: ")  
word_2=input("Enter second word: ")              


larger_value=len(word_1)
smaller_value=len(word_2)

if larger_value>smaller_value:
    for counter in range(0,smaller_value):
        print(word_1[counter]+word_2[counter],end="")
        remaining=word_1[smaller_value:]
    print(remaining)
elif smaller_value>larger_value:
    for counter in range(0,larger_value):
        print(word_1[counter]+word_2[counter],end="")
        remaining_2=word_2[larger_value:]
    print(remaining_2)

word=input()
number=input()

l=len(word)
k=len(number)
if l>k:
    for i in range(0,k):
        print(word[i]+number[i],end='')
        remaining=word[k:]
    print(remaining)
elif k>l:
    for count in range(len(l)):
        print(word[count]+number[count],end='')
        remaining=number[l:]
    print(remaining_2)

str=input('Please enter your number: ')
for char in str: 
    print(char, ':', ord(char))

-5/2

-5//2

i = 10
while(i >= -20):
    if(i < 0):
        test = " != "
        test = str(i//2) + test + str(int(i/2))
    else:
        test = " == "
        test = str(i//2) + test + str(int(i/2))
    print(test)
    i -= 5

test = ""
i = 0
j = 0
k = 15
test = "-->"
while i < 5:
    j = k - 1
    k -= 1
    while j > 10:
       test = str(i + j) + "-->" + test
       print(test)
       j -= 1
    i += 1

str(int(14/2))

word=input()
num1=0
ind1=0
while word[num1]!=',':
      num1+=1
ind2=num1+2
num2=len(word)
add=''
while ind1<num1 and ind2<num2:
      add+=word[ind1]+word[ind2]
      ind1+=1
      ind2+=1
if ind1<num1:
      add+=word[ind1: num1]
else: 
      add+=word[ind2: num2]
print(add)