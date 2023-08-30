#Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.			

#Solution


def c_d_p(full_price,discount_percentage):
    if discount_percentage <0 or discount_percentage>100:
        raise ValueError("price must be between 0 to 100")
    
    discount_amount =(full_price * discount_percentage)/100
    discount_price = full_price-discount_amount
    return discount_price

try:

    full_price= int(input("Enter the Full Price of the item:"))
    discount_percentage =int(input("Enter the discount percentage: "))

    discounted_price= c_d_p(full_price,discount_percentage)
    print("Discount Price",discounted_price)

except ValueError as e:
    print("Error :",e)



    '''  OUTPUT
    Enter the Full Price of the item:550
Enter the discount percentage: 5
Discount Price 522.5
    
    '''