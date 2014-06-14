def ArrayAddition(arr): 
  pup = 0
  new = arr[:]
  past = []
  new.pop(arr.index(max(arr)))
  for i in range(0, len(new)):
      pup = new[i]
      if i > 0:
          past.append(new[i-1])
      for j in range(i+1, len(new)):
            pup += new[j]
            if pup == max(arr):
                return "true"
      for x in past:
            pup += x
            if pup == max(arr):
                return "true"               
  return "false"
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArrayAddition(raw_input())  
