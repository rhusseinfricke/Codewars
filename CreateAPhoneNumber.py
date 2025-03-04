#Write a function that accepts an array of 10 integers 
(between 0 and 9), that returns a string of those numbers in the form of a phone number.



def create_phone_number(n):
    string = ""
    for i in n:
        string += str(i)
    return "("+string[0:3]+") "+string[3:6]+"-"+string[6:]
    
        