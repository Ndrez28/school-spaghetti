#I am just adding a comment for the purpose of a commit. 
def main(): 
    message = input(" What would you like to do? \n      (1) encrypt \n      (2) decrypt\n")
    key = input(" Enter the key: ") 
    keyLength = len(key) 
    
    for key in range(keyLength): 
        print(key % 6,sep = " ") 


main() 
