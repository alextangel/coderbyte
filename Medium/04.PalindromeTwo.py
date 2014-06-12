def PalindromeTwo(str):
  pup = ''
  for i in str:
    if i.isalpha():
      pup += i.lower()
  if pup == pup[::-1]:
    return "true"
  else:
    return "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PalindromeTwo(raw_input())           
