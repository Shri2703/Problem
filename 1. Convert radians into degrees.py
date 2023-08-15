'''
Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.					
'''

#Solution
pi=3.141592653589793;
 
 #Call the Function
def radians_to_degrees(radians):
    degrees = radians * (180 / pi)
    return degrees


if __name__ == '__main__':
    #user input
    radians_input = float(input("Enter the angle in radians: "))
    degrees_output = radians_to_degrees(radians_input)
    print(f"{radians_input} radians is approximately {degrees_output} degrees.")