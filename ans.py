def stringChallenge(sen):
    word=sen.split()
    largest=len(word[0])
    largestWord=word[0]
    for i in word:
        if len(i) > largest:
            largest=len(i)
            largestWord=i
            challengetoken="h6YTyuohhi"
            newList=[]
            largestSplit=largestWord.split()
            for x in largestSplit:
                if x not in challengetoken.split:
                    newList.append(x)
                    print(newList)
            

            
    print(largest,largestWord)
    
        

stringChallenge("I enjoy  coding  in python")    