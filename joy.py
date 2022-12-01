# # Remove empty string from the list below

list1=["Milka","Terryann","","Enzoo","Kimani","",""]
filtered_list=list(filter(None,list1))
print(filtered_list)

# # Write a program to iterate two lists simultaneously, display the items from list1 in original order
# # And items in list2 in reversed 

list1=[10,20,30,40,50,60]
list2=[1,2,3,4,5,6,]
for x,y in zip(list1,list2[::-1]):
    print(x,y)


# # Append 7000 ater 6000
list_x=[10,20,[300,400,[5000,6000],500],30,40] 
list_x[2][2].append(7000)
print(list_x)
 

# #A program to remove all duplicate values from a word
def duplicate_word(word):
    new_list=[]
    for i in range(len(word)):
        if word[i] not in new_list:
            new_list.append(word[i])
            print(new_list)
duplicate_word("wowownice")

# # From a given list of names user should input a random guess if the guess is equal to the names in the list
# # Print a congratulations statement if not allow user to guess again until the list is exhausted

names=["Shadrack","Meshack","Abednego","Samuel","Mathew",]
guess_name=input("Guess a name: \n")
if guess_name in names:
    print("Congratulations you've guessed th correct name")
else:
    print("Invalid Name")    


days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
new_days=set(days)
print(new_days) 


def iteration():
    y=range(0,10)
    for x in y:
        sum=0
        if x<len(y):
            sum+=x
iteration()

# for x in range(1,10+1):
#     y=x+[:1]
#     print(y)

x=range(1,10+1)
for n in x:
    sum=n+(n-1)
    print(f"current number is {n} the previous number is {n-1} and the sum is {sum} ")

    1,2,3,4,5,6,7,8,9,10

def iterate():
    i=1
    while i<=10:
        prev_num=1
        prev_num+=1
        sum=prev_num+1
        print(f"The sum is {sum}")   
        i+=1

iterate()        

days=['Mon','Tue','Wed','Mon','Sat']
x=days.count('Mon')
print(x)

days=['Mon','Tue','Wed','Mon','Sat']
print(days[::-1])


y=["John","Avril","Jude","Zuri"]
x=y[::-1]
print(x)


def zip_function():
    list1=['m','na','I','Ke']
    list2=['y','me','s','lly']
    list3=[i+j for i,j in zip(list1,list2)]
    print(list3)

zip_function()  

def get_index(word):
    middle=len(word)//2
    print(word[0],word[middle],word[-1] )

get_index("Mollen")    
