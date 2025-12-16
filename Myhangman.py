'''This code is for hangman game with Random word'''
import random #to get random word
play_again="y"

hangman_list=[f" "+"_"* 14+"\n|    |  |  |"+"\n|    |__O__|"+"\n|"+" "*6+"/|\\"+"\n|"+" "*7+"|"+"\n|"+"_"*6+"/|\\"+"_"*5,
              f" "+"_"* 14+"\n|"+" "*7+"|"+"\n|"+" "*7+"O"+"\n|"+" "*6+"/|\\"+"\n|"+" "*7+"|"+"\n|"+"_"*6+"/|"+"_"*6,
              f" "+"_"* 14+"\n|"+" "*7+"|"+"\n|"+" "*7+"O"+"\n|"+" "*6+"/|\\"+"\n|"+" "*7+"|"+"\n|"+"_"*7+"|"+"_"*6,
              #f" "+"_"* 14+"\n|"+" "*7+"|"+"\n|"+" "*7+"O"+"\n|"+" "*6+"/|"+"\n|"+" "*7+"|"+"\n|"+"_"*7+"|"+"_"*6,
              f" "+"_"* 14+"\n|"+" "*7+"|"+"\n|"+" "*7+"O"+"\n|"+" "*7+"|"+"\n|"+" "*7+"|"+"\n|"+"_"*7+"|"+"_"*6,
              f" "+"_"* 14+"\n|"+" "*7+"|"+"\n|"+" "*7+"O"+"\n|"*4+"_"* 15,
              f" "+"_"* 14+"\n|"+" "*7+"|"+"\n|"*5+"_"* 15,
              f" "+"_"* 15+"\n|"*5+"_"* 15,
              f" "+"_"* 14+"\n|"+" "*14+"\n|"+"    \\  O  /"+"\n|"+" "*5+"\\/|\\/"+"\n|"+" "*7+"|"+"\n|"+"_"*6+"/|\\"+"_"*6]

def print_hangman(position):
    for img in hangman_list[position].split("\n"):
        print(f"\033[1m{" "*70+img}\033[0m")
        
def choose_random_word(Hint=""):
    guess_list={"Programming Language":["python","recursion","algorithm","inheritance","compiler"],
                "AI Tools":["midJourney","gemini","canva","gitHubcopilot","perplexity"],
                "Roles":["Tester","Support","developer","architecture","analyst"]}
    hint_list=list(guess_list.keys())
    if len(Hint)==0:
        Hint=0
        random.shuffle(hint_list)
        return hint_list[0]
    else:
        random.shuffle(guess_list[Hint])
        return guess_list[Hint][0]


print(f"\033[1;36m{"*"*96}\033[0m")
print(f"\033[1;36m{" "*30}Welcome{" "*10}to{" "*10}Hangman\033[0m")
print(f"\033[1;36m{"*"*96}\033[0m")
while(play_again=="y"):
    play_again="n" 
    Hint=choose_random_word() #to get the hint   #Hint=choose_random_word(hint_list) #to get the hint
    s_word=choose_random_word(Hint=Hint) #to select the secrete word  #s_word=choose_random_word(guess_list,Hint=Hint) #to select the secrete word
    incorrect_guess=[]
    num_of_wrong_guess=6
    b_list=["-" for i in range(len(s_word))] #setting blank list with "_"
    print(f"\n\033[1;44;37m {Hint} \033[0m\n\033[1mGuess the word:\033[33m{''.join(b_list)}\033[0m")
    print_hangman(6) # function call to print the hangman : Initial hangman
    while(num_of_wrong_guess>0): # to check the no.of guess are there
        guess=input("Guess your word:(If you want to quit, enter digit 0)")
        if(guess==str(0)):              #If user want to quit in between of tthe game
            print("\033[1mThank you for playing the game!!!\033[0m")
            break
        else:
            if((guess in b_list) or (guess in incorrect_guess)): #if the same word(correct/incorrect) already predicted,dont do anything and continue to next occurance
                print(f"\n\033[1;33mYou already gussed '{guess}',Try a different letter!\033[0m")
                continue
            if(guess in s_word.lower()):            #If the letter predicted by user is in secrete word
                num_of_wrong_guess=num_of_wrong_guess    #keep the no.of lives count as is   
                if(s_word.lower().count(guess)>1):          #to check if s_word has many occurances of guess'ed letter
                    for j in range(len(s_word)):
                        if(guess==s_word[j]):
                            b_list[j]=guess
                else:                                       #else s_word has 1 occurances of guess'ed letter
                    b_list[s_word.lower().find(guess)]=guess
                if(b_list.count("-")!=0):               #To print the message till (n-1) of correct guess and no.of live remain 
                    print(f"\n\033[1;44;37m {Hint} \033[0m\n\033[1mGuess the word:\033[33m{''.join(b_list)}\033[0m")
                    print(f"\033[1;32mCorrect Guess!!Number of lives remaining:{num_of_wrong_guess}\033[0m")
                else:                                   #To print the congrats message for nth correct guess and winner hangman
                    print(f"\033[1;35m********** Congratulations, You won! **********\nThe word was: {s_word.lower()}\033[0m")
                    print_hangman(7)
                    break                               #for win case:Break the while(num_of_wrong_guess>0) and go to play again section
            else:                                   #If the letter predicted by user is not in secrete word
                num_of_wrong_guess=num_of_wrong_guess-1  #reduce the no.of lives count by 1
                incorrect_guess.append(guess)               #add the wrong guessed letter in incorrect list
                if(num_of_wrong_guess!=0):              #To print the message till (n-1) of incorrect guess and no.of live remain 
                    print(f"\n\033[1;44;37m {Hint} \033[0m\n\033[1mGuess the word:\033[33m{''.join(b_list)}\033[0m")
                    print(f"\033[1;31mWrong Guess!!Number of lives remaining: {num_of_wrong_guess}\033[0m")
                    print(f"\033[1;31mIncorrect guessed word: {incorrect_guess}\033[0m")
                else:                                   #To print the sprry message for nth incorrect guess and sad hangman
                    print(f"\033[1;35m********** Sorry, you died! **********\nThe word was: {s_word.lower()}\033[0m")
                    print_hangman(0)
                    break                               #for loss case:Break the while(num_of_wrong_guess>0) and go to play again section
            print_hangman(num_of_wrong_guess)
    if(guess!=str(0)):          #play again section
        play_again=input("Would you like to play again? (y/n):")
        if(play_again=="y"):
            print("\033[1m-------------Let's Play Again-------------\033[0m")
        else:
            print("\033[1mThank you for playing the game!!!\033[0m") #user dont want to continue or play the game again
            break               #Break the while(play_again=="y") and come out of the game

