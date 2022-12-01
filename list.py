#. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1=[10,20,30,40]
list2=[1,2,3,4,5]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

#Remove empty strings from the list of strings
def empty_string():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    filtered=list(filter(None,list1))
    print(filtered)

empty_string()   


list_a=[1452,11.23,1+2j]
for x in list_a:
    print(type(x))


def numbers():
    for num in range(1,6)  :
        if num==3:
         continue
        print(num)
numbers()    
