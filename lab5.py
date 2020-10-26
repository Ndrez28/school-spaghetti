def main():
    #Accepts the message
    message = input("Please enter a message: ")
    message = message.lower() 
    formatted_message =""
    #This will remove any commas, apostraphes, and spaces
    for i in range(len(message)):
        if message[i] != " ":
            formatted_message = formatted_message + message[i]
        elif message[i] != "'":
            formatted_message = formatted_message + message[i] 
        elif message[i] != ",":
            formatted_message = formatted_message + message[i] 
    #Here we will create a dictionary that will match the index(letter) to the variable with the list
    #Here will be another for loop that will print the list without brackets and do the above
    #*Review Previous lab for how to do it*
    
    banner_A = [
    ['        #         '],
    ['      ## ##       '],
    ['     ##   ##      '],
    ['    #########     '],
    ['   ##       ##    '],
    ['  ##         ##   '] 
        ]

    banner_B = [
    ['  #############   '], 
    ['  #           ##  '],
    ['  #          ##   '],
    ['  ############    '],
    ['  #          ##   '],
    ['  #############   ']
        ]
    
    banner_C = [
    ['     ##########   '],
    ['    ##            '],
    ['   ##             '],
    ['   ##             '],
    ['    ##            '],
    ['     ##########   ']        
        ]
    
    
    banner_N = [
    ['  ##      ##      '],
    ['  ###     ##      '],
    ['  ## ##   ##      '],
    ['  ##  ##  ##      '],
    ['  ##   ## ##      '],
    ['  ##    ####      ']
        ]
    
    banner_O = [
    ['     #######      '],
    ['    ###    ###    '],
    ['  ###       ###   '],
    ['  ###       ###   '],
    ['    ###    ###    '],
    ['     #######      ']
        ]
    
    banner_P = [
    ['   ######         ']
    ['   ##   ###       ']
    ['   ##    ###      ']
    ['   #######        ']
    ['   ##             ']
    ['   ##             ']
        ]
   
    banner_Q

    print(*banner_C , sep = '/n')
if __name__ == "__main__": 
    main()
