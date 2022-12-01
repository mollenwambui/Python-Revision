#Write a program to remove duplicates in a string.

def string_duplicate(word):
    new_list=[]
    for i in range(len(word)):
        if word[i] not in new_list:
            new_list.append(word[i]) 
        print(new_list) 
#string_duplicate("wowwownice")
string_duplicate("wowownice")


#Write a program to count the number of letters in a word.
def count_word(word):
    count=0
    for x in range(len(word)):
        count=count+1
    print(count) 
count_word("Mollen")    

#Python program to count the occurrence of each character in a word.



def string_upper(word):
    middle_char=len(word)//2
    # indexing=word[middle_char:].upper()
    # print(indexing)
    sentence = word[:middle_char].upper() +word[middle_char:].lower()
    print(sentence)

string_upper("my name is mollen and i love coding")    

name="lucy Wangare"
y=len(name)
print(y)
