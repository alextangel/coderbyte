def SecondGreatLow(arr): 
  arr = sorted(arr)

  for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            low = i+1
        elif arr[i] < arr[i+1]:
            low = i+1
            break          
  return str(arr[low]) + ' ' + str(arr[-2]) 
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SecondGreatLow(raw_input()) 