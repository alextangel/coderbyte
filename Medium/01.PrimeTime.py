def PrimeTime(num): 
  if num < 2:
    return "false"
  if num == 2:
    return "true"
  if num % 2 == 0:
    return "false"
  for i in range (3, num/2 +1):
    if num % i == 0:
      return "false"
  return "true"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeTime(raw_input())           
