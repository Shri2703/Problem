#Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. It should then return a boolean value of either True or False.				

#Solution

def has_equal_xo_count(inputString):
    lower_string = inputString.lower()
    
    # Count the occurrences of 'x' and 'o' in the string
    x_count = lower_string.count('x')
    o_count = lower_string.count('o')
    
    # Return True if the counts are equal, otherwise return False
    return x_count == o_count


input_str = "xoxoXoXo"
result = has_equal_xo_count(input_str)
print(result) 

# check if the character is present in string
def check_XO(srt):
    lower_string= srt.lower()
    return 'x' in lower_string and 'o' in lower_string

srt="XOXOXO"

result = check_XO(srt)
print(result)