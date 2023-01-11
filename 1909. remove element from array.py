import sys
from functools import reduce
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

def is_sorted(lst):
    it = iter(lst)
    try:
        prev = next(it)
    except StopIteration:
        return True
    for x in it:
        print(x,prev)
        if prev >= x:  # For reverse, use <
            return False
        prev = x
    return True

def canBeIncreasing(nums) -> bool:
    temp=[]
    flag=True
    for i in range(1,len(nums)+1):
        #print(nums[:i-1]+nums[i:])
        if is_sorted(nums[:i-1]+nums[i:]):
            return True
        
    return False

        
print(canBeIncreasing([512,867,904,997,403]))
