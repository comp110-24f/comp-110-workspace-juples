'''this is comp 110 EX04 - list Utility Functions'''
__author__ = "730511752"



def all(newlist: list[int], check: int) -> bool: 
    x = 0 
    index = 1
    length = len(newlist)
    while index < length:    
        newlist[x] == check
        x +=1
        index +=1 
    
        if newlist[x] != check:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = len(input) - 1 
    great =  sorted(input)
    check = great[index]
    return(check)
    

def is_equal(list1: list[int],list2: list[int]) -> bool:
    x = 0 
    index = 1
    length = len(list1)
    while index < length:    
        list1[x] == list2[x]
        x +=1
        index +=1 

        if list1[x] != list2[x]:
            return False
    return True



def extend(list1: list[int],list2: list[int]) -> None:
    list1 += list2 








