def check_valid_input(letter_guessed, old_letters_guessed):
    """
    returns if letter_guessed is already in old_letters_guessed and if its a valid guess
    :param letter_guessed: letter guessed
    :type letter_guessed: string
    :param old_letters_guessed: all the guesses the user did
    :type old_letters_guessed: list
    :rtype: bool
    """
    
    return (not (letter_guessed in old_letters_guessed) and is_valid_input(letter_guessed) ) 


def is_valid_input(letter_guessed):
    """
    returns if the input is valid or not
    :param letter_guessed: letter guessed
    :type letter_guessed: string
    :rtype: bool
    """
    
    if(len(letter_guessed)>1):
        return False
    elif(len(letter_guessed)==1):
        if not(letter_guessed.isalpha()):
            return False
        return True

    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    returns if letter_guessed is valid and if valid adds it to old_letters_guessed
    :param letter_guessed: letter guessed
    :type letter_guessed: string
    :param old_letters_guessed: all the guesses the user did
    :type old_letters_guessed: list
    :rtype: bool
    """    
    
    if check_valid_input(letter_guessed, old_letters_guessed):        
        old_letters_guessed.append(letter_guessed)    
        return True
    else:
        if(is_valid_input(letter_guessed)):
            old_letters_guessed.append(letter_guessed)               
        print_all_tries(letter_guessed, old_letters_guessed)
        return False        
    
    
def print_all_tries(letter_guessed, old_letters_guessed):
    """
    Prints all of the tries of the user.
    :param letter_guessed: user's guess.
    :param old_letters_guessed: letters that have been guessed.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :returns: None
    """
    
    old_letters_guessed.sort()
    x = ""    
    print("X")
    for i in old_letters_guessed:
        x += i
        if not i is old_letters_guessed[-1]:
            x += " -> "
    print(x)            

    
def show_hidden_word(secret_word, old_letters_guessed):
    """
    returns a string representing the letters from the secret word the user discoverd
    :param secret_word: the word the user need to discover
    :type secret_word: string
    :param old_letters_guessed: all the guesses the user did
    :type old_letters_guessed: list
    :rtype: string
    """
    
    x = list()
    start = 0
    mystring = ""
    
    for letter in secret_word:
        x.append(" _ ")
    for letter in old_letters_guessed:       
        for i in range(len(secret_word)):           
            if(letter == secret_word[i]):
                x[i] = letter+" "
                                       
    return mystring.join(x)    


def check_win(secret_word, old_letters_guessed):
    """
    return if user discovered the whole word or not
    :param secret_word: the word the user need to discover
    :type secret_word: string
    :param old_letters_guessed: all the guesses the user did
    :type old_letters_guessed: list
    :rtype: bool
    """
    
    count = 0
    
    while(count<len(secret_word)):
        if not(secret_word[count] in old_letters_guessed):
            return False
        count+=1
    return True  
    
    
def print_hangman(num_of_tries, HANGMAN_PHOTOS):
    """
    Prints the hangman.
    :param num_of_tries: number of tries that the user used.
    :param HANGMAN_PHOTOS: the dict that stores all of the possible hangman positions.
    :type num_of_tries: int
    :type HANGMAN_PHOTOS: dict
    :returns: None
    """
    
    print(HANGMAN_PHOTOS["pic"+str(num_of_tries)])
        
        
def choose_word(file_path, index):
    """
    return how much words there are in the file and return the count of them+the word at the index place
    :param file_path: represents a file path
    :type file_path: string
    :param index: represents the place of the chosen word
    :type index: int
    :rtype: string   
    """
    
    my_file = open(file_path, 'r')
    for i in my_file:
        words_list=i.split(" ")    
    new_words_list = list()
    exists = False
    count = 0
    new_words_list.append(words_list[0])
    for word in words_list:
        for new_word in new_words_list:
            if word == new_word:
                exists = True
                count += 1
                break
        if exists == False:
            new_words_list.append(word)
        exists = False    
    my_file.close()    
    if index > len(words_list):
        return (len(new_words_list), words_list[index%(len(words_list))-1])  
    return words_list[index-1]


def print_headline(num_of_tries):
    """
    Prints the hadline of the game.
    :param num_of_tries: number of tries that the user used.
    :type num_of_tries: int
    :returns: None
    """
    
    print(""" 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
        """)
    print(num_of_tries)    
    
    
def main():      
    picture1 = " x-------x "
    picture2 = picture1 + " \n |\n |\n |\n |\n | "
    picture3 = picture1 + " \n | \t | \n | \t 0 \n | \t \n |\n |"
    picture4 = picture1 + " \n | \t | \n | \t 0 \n | \t | \n |\n |"
    picture5 = picture1 + " \n | \t | \n | \t 0 \n | \t/| \n |\n |"
    picture6 = picture1 + " \n | \t | \n | \t 0 \n | \t/|\ \n | \t/ \n | "
    picture7 = picture1 + " \n | \t | \n | \t 0 \n | \t/|\ \n | \t/ \ \n | "
    
    MAX_TRIES = 6
    num_of_tries = 0
    
    HANGMAN_PHOTOS = {"pic1": picture1,"pic2": picture2,"pic3": picture3,"pic4": picture4,"pic5": picture5,"pic6": picture6,"pic7": picture7}
    
    print_headline(MAX_TRIES) 
    
    
    file_path = input("please enter the file path ")
    
    index = int(input("please enter the index "))
    
    print("let's start")
    
    end = False
    won = False 
    mistake = True
    old_letters_guessed = []    
    secret_word = choose_word(file_path, index)    
    while not end:
        if mistake:
            print(HANGMAN_PHOTOS["pic"+str(num_of_tries+1)])
            
        print(show_hidden_word(secret_word, old_letters_guessed))
        guess_letter = input("guess letter: ")         
        if guess_letter == "-1":
            end = True
            break 
                     
        if (guess_letter in secret_word) and try_update_letter_guessed(guess_letter, old_letters_guessed):
            won = check_win(secret_word, old_letters_guessed)            
            mistake = False
            if won:
                end = True
                
        else:  
            print(":(")
            old_letters_guessed.append(guess_letter)
            print_all_tries(guess_letter, old_letters_guessed)
            mistake = True
            if(num_of_tries == 6):
                end = True
                won = False
                break
            num_of_tries += 1 
            
            
                
    if won:
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("WIN")
    else:
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("LOSE")

        
if __name__ == "__main__":
    main()      
