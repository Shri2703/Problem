#Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.


#solution

def double_characters(input_string):
    double_string =''.join([char*2 for char in input_string]) 
    return double_string


input_str="WoW"
double_str=double_characters(input_str)
print(double_str)

input_str="123a!"
double_str=double_characters(input_str)
print(double_str)