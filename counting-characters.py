#Counting_Characters app
#author - Nick Paisley
#created - 3.4.19

#Write a program that calculates the number of times each character occurs in a string and prints these stats to the console.
#Here’s a test string, for your convenience

test_string = "CCBBAA"

char_dict = {}
def char_add(test_string): 
        
    for char in test_string:
        char_dict[char] = test_string.count(char)
    return (char_dict)
    

char_add(test_string)
chars = char_dict.values()
for keys in (char_dict):
    print(keys, chars)