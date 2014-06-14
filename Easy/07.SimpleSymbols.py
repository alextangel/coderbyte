def SimpleSymbols(str): 
  if str[0].isalpha() and str[-1].isalpha():
    return "false"
  for i in range(0, len(str)):
    if str[i].isalpha():
      if str[i-1] == '+' and str[i+1] == '+':
        return "true"
  return "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())           
