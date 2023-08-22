#Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent “4444444444444444”, then it should return “4444”.							


#Solution
def hide_credit_card(card_number):
    card_str = str(card_number)  # Convert the card number to a string
    
 
    last_four = card_str[-4:]
    
    hidden_card = '*' * (len(card_str) - 4) + last_four
    
    return hidden_card


credit_card_number = 4444444444444444  
hidden_number = hide_credit_card(credit_card_number)
print(hidden_number) 



 # Output: "************4444"
