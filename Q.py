# Interview questions :-
"""
Q-1. What does it mean that Python is a dynamically-typed language?
A) Variables in python can implicitly change to other types when comparing. For examples you can compare a string "2" and the number 2 using ==.
B) Python variables can be assigned to different types and changes types at will.
C) Python is a more efficient language than C++
D) All of the above

Answer: Python variables can be assigned to different types and changes types at will.


Q-2. What do we call it when we convert from one data type to another?
A)casting
B) converting
C) changing

Answer:casting


Q-3. What are the common built-in data types in Python?

Ans: The common built in data types in python are-

Numbers– They include integers, floating point numbers, and complex numbers. eg. 1, 7.9,3+4i

List– An ordered sequence of items is called a list. The elements of a list may belong to different data types. Eg. [5,’market’,2.4]

Tuple– It is also an ordered sequence of elements. Unlike lists , tuples are immutable, which means they can’t be changed. Eg. (3,’tool’,1)

String– A sequence of characters is called a string. They are declared within single or double quotes. Eg. “Sana”, ‘She is going to the market’, etc.

Set– Sets are a collection of unique items that are not in order. Eg. {7,6,8}

Dictionary– A dictionary stores values in key and value pairs where each value can be accessed through its key. The order of items is not important. Eg. {1:’apple’,2:’mango}

Boolean– There are 2 boolean values- True and False.


Q-4. What is slicing in Python?

Ans: Slicing is used to access parts of sequences like lists, tuples, and strings. 
The syntax of slicing is-[start:end:step]. The step can be omitted as well. 
When we write [start:end] this returns all the elements of the sequence from the 
start (inclusive) till the end-1 element. If the start or end element is negative i,
it means the ith element from the end. The step indicates the jump or how 
many elements have to be skipped. 
Eg. if there is a list- [1,2,3,4,5,6,7,8]. Then [-1:2:2] will return elements 
starting from the last element till the third element by printing every 
second element.i.e. [8,6,4].


Q-5. What are local variables and global variables in Python?
Global Variables:

Variables declared outside a function or in global space are called global variables.
These variables can be accessed by any function in the program.

Local Variables:

Any variable declared inside a function is known as a local variable. 
This variable is present in the local space and not in the global space.


Q-6. Is python case sensitive?
Ans: Yes. Python is a case sensitive language.


Q-7. Is indentation required in python?
Ans: Indentation is necessary for Python. It specifies a block of code. 
All code within loops, classes, functions, etc is specified within an 
indented block. It is usually done using four space characters. 
If your code is not indented necessarily, it will not execute accurately 
and will throw errors as well.


Q-8. What is the difference between Python Arrays and lists?
Ans: Arrays and lists, in Python, have the same way of storing data. 
But, arrays can hold only a single data type elements whereas lists can 
hold any data type elements.


Q-9. What is the purpose of is, not and in operators?
Ans: Operators are special functions. They take one or more values and produce 
a corresponding result.

is: returns true when 2 operands are true  (Example: “a” is 'a')

not: returns the inverse of the boolean value

in: checks if some element is present in some sequence


Q-10. Does python support multiple inheritance?
Ans: Multiple inheritance means that a class can be derived from more 
than one parent classes. Python does support multiple inheritance, unlike Java.

Q-11. What is Polymorphism in Python?
Ans: Polymorphism means the ability to take multiple forms. 
So, for instance, if the parent class has a method named ABC then the 
child class also can have a method with the same name ABC having its own 
parameters and variables. Python allows polymorphism.

Q-12. Define encapsulation in Python?
Ans: Encapsulation means binding the code and the data together. 
A Python class in an example of encapsulation.

Q-13. How do you do data abstraction in Python?
Ans: Data Abstraction is providing only the required details 
and hiding the implementation from the world. It can be achieved in 
Python by using interfaces and abstract classes.


Q.14 :- How to find the characters at an odd position in string input by User?

sen = "My name is Gaurav Poonia."
str = ""
for i in range(len(sen)):
    if i % 2 == 0:
        str += sen[i]

print(str)



# Q-15 :- Write a program to find out the largest and smallest word in the string?

str = "My name is Gaurav"
str = str.split()  
maxx = str[0]
ml = len(str[0])
for i in str:
    if len(i) > ml:
        ml = len(i)
        maxx = i
print(maxx)


# Q-16. Python program to swap first and last element of the list.

lst = [1,2,6,5,7]
def swap():
    for i in lst:
        temp = lst[0]
        lst[0] = lst[len(lst)-1]
        lst[len(lst)-1] = temp
    return lst
data = swap()
print(data)


# Q.18 get only the domain name?

email = input("enter your mail id : ")
gd = email.split('@')[1]
gd = gd.split('.')[0]
print(gd)


Q-19. Write a program in Python to check if a number is prime?

a=int(input("enter number"))
if a=1:
   for x in range(2,a):
         if(a%x)==0:
          print("not prime")
   break
   else:
      print("Prime")
else:
   print("not prime")

Q-20. What is the output of the following?

f = None
 
for i in range (5):
    with open("data.txt", "w") as f:
        if (i > 2):
            break
 
print f.closed
a) True
b) False
c) None
d) Error
Answer: a) True 








"""