#Write a program in Python to display the Factorial of a number.
def factorial(number):
    fact=1
    for num in range(1,number+1):
        fact*=num
        print(fact)
factorial(6)

#Write a program to display the first 7 multiples of 7
def multipleof_seven():
    for x in range(1,50):
        if x%7==0:
            print(x)

multipleof_seven()

#Write a program that appends the square of each number to a new list.
def squareof_numbers():
    list=[2,3,4,5,6]
    new_list=[]
    for x in list:
        new_list.append(x*x)
        print(new_list)
squareof_numbers()       

#using list comprehension seperate all the positive numbers from negative numbers
def positive_negative():
    list=[2,-8,-5,3,6,-8]
    positive_list=[]
    negative_list=[]
    for num in list:
        if num<0:
            negative_list.append(num)
        else:
            positive_list.append(num)
            print(negative_list)
            print(positive_list)
positive_negative()           


# Write a program that appends the type of elements from a list.
def list_type():
    list=("Mollen",21,50.7,True)
    new_list=[]
    for x in list:
        new_list.append(type(x))
        print(new_list)
list_type() 


#: Write a program to filter even and odd number from a list.
def evenand_odd():
    list=[1,2,3,4,5,6,7,8,9,10]
    even_list=[]
    ood_list=[]
    for x in list:
        if x%2==0:
            even_list.append(x)
        else:
            ood_list.append(x)  
            print(even_list)  
            print(ood_list)
evenand_odd()           

# Write a program to fetch only even values from a dictionary.
def even_dict():
    my_dict={"val1":10,"val2":13,"val3":15,"val4":16}
    for x in my_dict.values():
        if x%2==0:
            print(x,end=" ")
even_dict()  

#Takes 20 interger from the use and prints the number of positive,negative,oddnumber,evennumbers,0
def twenty_intergers():
    positive=0
    negative=0
    oddnumber=0
    evennumber=0
    
    number= list(int(input("Enter your 20 intergers \n")))
    for x in number:
        if x>0:
            positive=positive+1
        elif x<0:
            negative=negative+1
        elif x%2==0:
            oddnumber=oddnumber+1
        elif x%2!=0:
            evennumber=evennumber+1    

list=[1,2,3,4,5,6,7,8,9,10,11,]     

#Create a function that takes in list of names and returns the number of
#names longer than 5 characters

def long_names(*names):
     sum=0
     for x in names:
         if len(x)>5:
             sum+=1
        
             print(sum)

def operations(a,b):
    return a+b and a*b and a-b


def numbers():
    for i in range(1,100):
        while len(i)==10:
            if i%2==0:
                i+=1
                print(i)    
numbers()
