def BinaryConverter(str): 
    str = str[::-1]
    sum = 0
    for i in range(0, len(str)):
        sum += int(str[i]) * 2**i
    return sum
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print BinaryConverter(raw_input())   


