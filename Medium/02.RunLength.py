def RunLength(str):
  encode = 1
  pup = []
  if len(str) == 1:
      return '1' + str
  for i in range(0, len(str)-1):
    if str[i] == str[i+1]:
      encode += 1
      if i == len(str)-2:
          pup.append('%s'%encode + str[i+1])
    elif str[i] != str[i+1]:
      pup.append('%s'%encode + str[i])
      encode = 1
      if i == len(str)-2:
          pup.append('%s'%encode + str[i+1])
  return ''.join(pup)
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print RunLength(raw_input())  