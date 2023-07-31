'''  Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.	'''

#solution

def decimal_to_binary(decimal_num):
    if not 0 <= decimal_num < 1024:
        raise ValueError("Decimal number must be between 0 and 1023.")

    binary_num = bin(decimal_num)[2:]  # Removing the '0b' prefix from the binary representation
    return binary_num.zfill(10)  # Pads with leading zeros to ensure a 10-digit binary number

# Example usage:
decimal_number =int(input("Enter the decimal Number255 "))
binary_number = decimal_to_binary(decimal_number)
print("Binary representation of", decimal_number, "is:", binary_number)
