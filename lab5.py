#Andrez Alcazar and Jacob Orozco
def main():
    #Accepts the message
    message = input("Please enter a message: ")
    message = message.upper() 
    formatted_message =""
    #This will remove any commas, apostraphes, and spaces
    for i in range(len(message)):
        if message[i] != " " and message[i] != "'" and message[i] != ",":
            formatted_message = formatted_message + message[i]
    #Creating the letter art
    banner_A = [
    ['        #         '],
    ['      ## ##       '],
    ['     ##   ##      '],
    ['    #########     '],
    ['   ##       ##    '],
    ['  ##         ##   \n'] 
        ]
    banner_B = [
    ['  #############   '], 
    ['  ##           ## '],
    ['  ##          ##  '],
    ['  ############    '],
    ['  ##          ##  '],
    ['  #############  \n']
        ]
    banner_C = [
    ['     ##########   '],
    ['    ##            '],
    ['   ##             '],
    ['   ##             '],
    ['    ##            '],
    ['     ##########   \n']        
        ]
    banner_D = [
    ['   ##########     '],
    ['   ##         ##  '],
    ['   ##          ## '],
    ['   ##          ## '],
    ['   ##         ##  '],
    ['   ###########   \n']             
        ]
    banner_E = [
    ['   ###########    '],
    ['   ##             '],
    ['   ##             '],
    ['   #########      '],
    ['   ##             '],
    ['   ###########   \n']             
        ]   
    banner_F = [
    ['   ############   '],
    ['   ##             '],
    ['   ##             '],
    ['   ##########     '],
    ['   ##             '],
    ['   ##             \n']          
        ]   
    banner_G = [
    ['    #########        '],
    ['   ##                '],
    ['   ##                '],
    ['   ##   ######       '],
    ['   ##       ##       '],
    ['     ########       \n']            
        ]
    banner_H = [
    ['   ##        ##      '],
    ['   ##        ##      '],
    ['   ##        ##      '],
    ['   ############      '],
    ['   ##        ##      '],
    ['   ##        ##     \n']        
        ]
    banner_I = [
    ['   ############      '],
    ['       ###           '],
    ['       ###           '],
    ['       ###           '],
    ['       ###           '],
    ['   ############     \n']         
        ]
    banner_J = [
    ['   ############      '],
    ['        ##           '],
    ['        ##           '],
    ['        ##           '],
    ['  ##    ##           '],
    ['     ##             \n']        
        ]
    banner_K = [
    ['   ##      ##        '],
    ['   ##    ##          '],
    ['   ##  ##            '],
    ['   ####              '],
    ['   ##  ##            '],
    ['   ##    ###        \n']         
        ]
    banner_L = [
    ['   ##                '],
    ['   ##                '],
    ['   ##                '],
    ['   ##                '],
    ['   ##                '],
    ['   ############     \n']             
        ]
    banner_M = [
    ['  ###            ### '],
    ['  ## ##        ## ## '],
    ['  ##   ##     ##  ## '],
    ['  ##    ##   ##   ## '],
    ['  ##     ## ##    ## '],
    ['  ##      ##      ##\n']             
        ]
    banner_N = [
    ['  ##      ##      '],
    ['  ###     ##      '],
    ['  ## ##   ##      '],
    ['  ##  ##  ##      '],
    ['  ##   ## ##      '],
    ['  ##    ####      \n']
        ]   
    banner_O = [
    ['     #######      '],
    ['    ###    ###    '],
    ['  ###       ###   '],
    ['  ###       ###   '],
    ['    ###    ###    '],
    ['     #######      \n']
        ]    
    banner_P = [
    ['   ######         '],
    ['   ##   ###       '],
    ['   ##    ###      '],
    ['   #######        '],
    ['   ##             '],
    ['   ##             \n']
        ]  
    banner_Q = [
    ['    #######       '],
    ['   ###    ###     '],
    ['  ###      ###    '],
    ['   ###    ###     '],
    ['    ###### ###    '],
    ['            ###   \n']
        ]  
    banner_R = [
    ['  ########        '],
    ['  ##     ####     '],  
    ['  ##      ##      '],
    ['  ########        '],
    ['  ##     ###      '],
    ['  ##      #####   \n']
        ]
    banner_S = [
    ['   ############   '],
    ['  ########     ## '],
    ['      #######     '],
    ['          #####   '],
    ['  ##     ######   '],
    ['   #########      \n']
        ]
    banner_T = [
    ['   #############  '],
    ['   #############  '],
    ['        ###       '],
    ['        ###       '],
    ['        ###       '],
    ['        ###       \n']
        ]
    banner_U = [
    ['   ###      ###    '],
    ['   ###      ###    '],
    ['   ###      ###    '],
    ['   ###      ###    '],
    ['    ###   ###      '],
    ['      ######       \n']
        ]
    banner_V = [
    ['  ##         ##    '],
    ['   ##       ##     '],
    ['    ##     ##      '],      
    ['     ##   ##       '],
    ['      ## ##        '],
    ['       ###         \n']
        ]
    banner_W = [
    [' ##     ###      ##'],
    [' ##     ## ##    ##'],
    ['  ##   ##   ##  ## '],
    ['  ##   ##   ##  ## '],
    ['   ## ##     ## ## '],
    ['    ###       ##   \n']
        ]
    banner_X = [
    ['  ####    ####     '],
    ['   ####  ####      '],
    ['     #####         '],
    ['     #####         '],
    ['   ####  ####      '],
    ['  ####    ####     \n']
        ]
    banner_Y = [
    ['   ####     ####   '],
    ['   ####     ####   '],
    ['    ####   ####    '],
    ['      ### ###     '],
    ['       #####       '],
    ['       #####       ']
        ]
    banner_Z = [
    [' #############     '],
    ['    ##########     '],
    ['       #####       '],
    ['     #####         '],
    ['   ###########     '],
    ['  ##############   \n']
        ]
    #Dictionary that is used to match index with banner
    banner_pairs = {"A": banner_A, "B": banner_B, "C": banner_C, "D": banner_D, "E": banner_E, 
                    "F": banner_F, "G": banner_G, "H": banner_H, "I": banner_I, "J": banner_J,
                    "K": banner_K, "L": banner_L, "M": banner_M, "N": banner_N, "O": banner_O,
                    "P": banner_P, "Q": banner_Q, "R": banner_R, "S": banner_S, "T": banner_T, 
                    "U": banner_U, "V": banner_V, "W": banner_W, "X": banner_X, "Y": banner_Y, 
                    "Z": banner_Z} 
    #Prints the banners
    for i in range(len(formatted_message)): 
        key_dictionary = formatted_message[i] 
        for row in banner_pairs.get(key_dictionary):
            for item in row: 
                print(item)  
#Vodoo Magic  
if __name__ == "__main__": 
    main()