def Division(num1,num2): 
  if num2 == 0:
    return num1
  return Division(num2, num1%num2)
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print Division(raw_input())         
 
