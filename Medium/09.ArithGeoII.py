def ArithGeoII(arr): 
  flagA = flagG = 0
  for i in range(1, len(arr)-1):
    if arr[i]-arr[i-1] == arr[i+1] - arr[i]:
      flagA += 1
    elif arr[i]/arr[i-1] == arr[i+1]/arr[i]:
      flagG += 1
    else:
      return  -1
  if flagA == len(arr)-2:
      return 'Arithmetic'
  elif flagG == len(arr)-2:
      return 'Geometric'
  else:
      return -1  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeoII(raw_input())  






  