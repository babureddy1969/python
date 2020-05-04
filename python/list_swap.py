# Swap function 
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
  
# Driver function 
List = [23, 65, 19, 90] 
pos1, pos2  = 1, 3
  
print(swapPositions(List, pos1-1, pos2-1))

# Swap function 
def swapPositions0(list, pos1, pos2): 
      
    # popping both the elements from list 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    # inserting in each others positions 
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list
# Driver function 
List = [23, 65, 19, 90] 
pos1, pos2  = 1, 3
  
print(swapPositions0(List, pos1-1, pos2-1)) 
# Swap function 
def swapPositions1(list, pos1, pos2): 
  
    # Storing the two elements 
    # as a pair in a tuple variable get 
    get = list[pos1], list[pos2] 
       
    # unpacking those elements 
    list[pos2], list[pos1] = get 
       
    return list
  
# Driver function 
List = [23, 65, 19, 90] 
  
pos1, pos2  = 1, 3
print(swapPositions1(List, pos1-1, pos2-1)) 
