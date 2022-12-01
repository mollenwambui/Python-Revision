#Write a program to check whether a given key exists in a dictionary or not.
from os import remove


def exist():
    my_dict={"Mollen":1,"Joy":2,"Lucy":3}
    if "Mollen" in my_dict.keys():
        print("True")
    else:
        print("False")    

exist()        

#Write a program to iterate over dictionary items using for loop.
def iterate():
    dict={"Sakina":10,"Maureen":15,"Faith":25,"Linda":45}
    for x in  dict.items():
        print(x)
iterate()  

#Write a program in python to map 2 lists into a dictionary.
def map_list():
    keys=[1,2,3]
    values=["Value 1","Value 2","Value 3"]
    dict2=dict(zip(keys,values))
    print(dict2)

map_list() 

#Python program to remove a set of keys.
 
def remove_keys():
    this_dict={1:"Wambui",2:"Macharia",3:"Wanjiku",4:"Lona"}
    removes=this_dict.pop(3)
    print(removes)
remove_keys()  

#Write a program to concatenate two dictionaries to create one.
def dict_concatenation():
    dict1={"key1":1,"key2":2,"key3":3}
    dict2={"key4":4,"key5":5,"key6":6}
    dict1.update(dict2)
    print(dict1)

dict_concatenation()   

#Write a program to sum all the values of a dictionary
def sumof_dicts():
    sum_dict={"num1":100,"num2":200,"num3":300}
    sum=0
    sumlist=[]
    for x in sum_dict.values():
        sumlist.append(x)
        sum+=x
        print(sum)
sumof_dicts()       

    

# Write a program in Python to choose a random item from a list.
def random_item() :
    sec_dict={"a":10,"tb":20,"c":30,"d":40}  
    val=sec_dict.values()
    if 90 in val:
        print("The value exists in the dictionary")
    else:
        print("The value does not exist")    

random_item()        

# Write a program in python to map lists to dictionary.
def map_dict():
    key=["fruit","vegetables"]
    values=["mango","tomato"]
    dict1=dict(zip(key,values))
    print(dict1)

map_dict()   





#Ask user to give name and marks of 10 different students .store them in a dictionary.then print the dictionary


# def name_marks():
#     dictionary=dict(keys,values)
#     keys= str(input("Enter the names \n"))
#     while keys >10:
#         return keys
#     values=str("Enter the marks \n")

# name_marks()     


def marks_names():
    keys=[]
    values=[]
    while len(keys)!=10:
        marks=int(input("Enter the marks: \n"))
        keys.append(marks)
    while len(values)!=10:
        names=str(input("Enter the names : \n"))
        values.append(names)

        print(dict(zip(keys,values)))

marks_names()  

#How to map two dictionaries
  
sec_dict={"a":10,"tb":20,"c":30,"d":40}  
sum_dict={"num1":100,"num2":200,"num3":300}
new_dict={**sec_dict,**sum_dict}
print(new_dict)



def studentsMarks():
    key=[]
    values=[]
    while len(key)!=10:
        names=input(str("Enter your name \n"))
        key.append(names)
    while len(values)!=10:
        marks=input(int("Enter your marks \n"))
        values.append(marks)

        print(dict(zip(key,values)))