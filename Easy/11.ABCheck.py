def ABCheck(str): 
  for i in range(len(str)-4):
    if str[i] == 'a' and str[i+4] == 'b':
      return 'true'
    elif str[i] == 'b' and str[i+4] == 'a':
      return 'true'
  return 'false'
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ABCheck(raw_input())           
