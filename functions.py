#Define a function that accepts 2 values and return its sum, subtraction and multiplication.
from operator import sub
def two_intergers(a,b):
    sum=a+b
    multiplication=a*b
    subtraction=a-b
    return sum ,multiplication,subtraction

# Define a function that accepts roll number and returns whether the student is present or absent    
def roll_number():
    list=[10,14,54,46,78,23,5,6,8]
    attendance=input("Enter your roll number \n")
    if attendance in list:
            print("Present")
    else:
            print("Absent")    
#roll_number()   

# Define a function in python that accepts 3 values and returns the maximum of three numbers.
def max_value(a,b,c):
    if a>b and a>c:
        print(f"{a} is the greatest number")
    elif b>a and b>c:
        print(f"{b} is the greatest number" )   
    elif c>a and c>b:
        print(f"{c} is the greatest number")   
    else:
        print("None is greater than the other")  

         
#Define a function which counts vowels and consonant in a word.
def vowels_consonants(val):
    vowels=0
    consonants=0
    for i in range (len(val)):
        if val[i] in ['a','e','i','o','u']:
            vowels=vowels+1
        else:
            consonants=consonants+1
            print("count of vowels is ",vowels) 
            print("count of consonants is ",consonants)       

#: Define a function that accepts radius and returns the area of a circle.
def area_ofcircle(radius) :
    area=3.14*(radius*radius)
    return area



def numberof_vc(word):
    word=word.lower()
    vowels=0
    cons=0
    list=['a','e','i','o','u']  
    for x in word:
        if x in list:
            vowels+=1
        else:
            cons+=1
        print(f"the number of vowels is {vowels}")  
        print(f" the number of consonants is {cons}")   

    
numberof_vc("Mollen")