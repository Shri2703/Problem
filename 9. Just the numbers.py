#Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.


#Solution

def filter_integers(input_list):
    result=[x for x in input_list if isinstance(x,int) and x >=0]
    return result

input_list=[3,'hello',7,'World',0,3.4,'!!!!']
filter_list=filter_integers(input_list)
print(filter_list)