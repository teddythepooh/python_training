#A function that extracts all the digits from a string:
def extract_num(string):
    num_only = ""
    for i in string:
        if i in "0123456789":
            num_only+=i
    return num_only

#A function that returns true if there are duplicate numbers in a string:
def duplicate_num(string):
    string_of_num = extract_num(string)
    length = len(string_of_num)
    for i in range(length):
        for j in range(i + 1, length):
            if string_of_num[i] == string_of_num[j]:
                return True
      
def position(guess, key):
    guess_as_str = str(guess)
    key_as_str = str(key)
    position = 0
    for i in range(len(key_as_str)):
        if guess_as_str[i] == key_as_str[i]:
            position+=1
    return position

def exist(guess, key):
    guess_as_str = str(guess)
    key_as_str = str(key)
    exist = 0
    for i in range(len(key_as_str)):
        if guess_as_str[i] in key_as_str and guess_as_str[i] != key_as_str[i]:
            exist+=1
    return exist
        
key = input("Enter the key:") 
num_guesses_remaining = 12
guesses = 0

while num_guesses_remaining > 0 and guesses <= 12:
    guess = input("Guess:")
    
    #ERROR CHECKING
    tallies = [0,0,0]

        #Is the guess 4 in length?
    if len(str(guess)) != 4:
        tallies[0]+=1
    
        #Is the guess comprised of all numbers?
    for i in str(guess):
        if i not in "0123456789":
            tallies[1]+=1
        
        #Does the guess contain duplicate numbers?
    if duplicate_num(str(guess)):
        tallies[2]+=1
    
    errors = ""
    if tallies[0] > 0:
        errors+="The guess must be 4 in length."
    if tallies[1] > 0:
        errors+="It must consist of all numbers."
    if tallies[2] > 0:
        errors+="No duplicate numbers are allowed."
    
    #CROSS-REFERENCING BETWEEN KEY and GUESSES
    if guess == key: #CORRECT GUESS AND VALID INPUT
        guesses+=1
        num_guesses_remaining-=12 #immediately ends the program       
        print("You guessed the key:", key)
        print("It took you", guesses, "guess(es)!")
    elif sum(tallies) == 0: #WRONG GUESS, BUT VALID INPUT
        guesses+=1
        num_guesses_remaining-=1 #valid inputs count against the 12 guesses
        print(guess, 
              ", exist: ", exist(guess, key),
              ", position: ", position(guess, key),
              sep = "")
    elif sum(tallies) > 0: #WRONG GUESS AND INVALID INPUT
        print(errors, "Try again!") #invalid inputs don't count against the 12 guesses
    
    if num_guesses_remaining == 0: #When there are no more remaining guesses
        if guess != key: #and the user does not input the correct key in the last guess,
            print("YOU LOST!!!")
            print("Correct Key:", key)




