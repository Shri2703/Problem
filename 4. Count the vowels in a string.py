#Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.			


#Solution


def Count_Vowels(Word):
   Vowels="aeiou"
   count=0 
   for Char in Word:
            if Char.lower() in Vowels:
                count += 1
                return count;

#User Input


Word = input("Enter A Word")
Num_Vowels =Count_Vowels(Word)
print(f"The number of vowels in '{Word}' is: {Num_Vowels}")