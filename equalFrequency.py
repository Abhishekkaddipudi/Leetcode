def equalFrequency(word: str) -> bool:
    freq={}
    flag=True
    for i in word:
        if i in freq:
            freq[i]+=1
            flag=False
        else:
            freq[i]=1
    print(freq)
    if flag:
        return True
    val=list(freq.values())
    n=len(val)
    for i in range(n):
        val[i]-=1

            
        if len(set(val))==1 or (len(set(val))==2 and 0 in set(val)):
            return True
        else:
            val[i]+=1

    return False
print(equalFrequency("abbcc"))