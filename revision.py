# def consonant_vowel(word):
#     count=0
#     sum=0
#     for i in range(len(word)):
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             count+=1
#             return count
#         elif i!="a" or i!="e" or i!="o" or i!="u" or i!="i":
#             sum+=1
#         return sum

def word(names):
    names=names.lower()
    vowels=0
    cons=0
    list=["a","e","i","o","u"]
    for x in names:
        if x in list:
               vowels+=1
               print(f"The number of vowels is{vowels}") 
        else:
            cons+=1
        print(f"The number of consonants is {cons}") 
         
     
word("winfred")