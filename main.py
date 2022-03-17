import random

word_list = ["rants", "mopey", "lucid", "crane", "light", "frown", "choke", "wheat", "audio", "fakes"]
list_of_list = []
print("Hi there! Welcome to Wordle! \n"
      "The objective of the game is to guess a secret 5-letter word in six tries, using a series of hints to figure it out. \n"
      "If any of your letters have a '<<' in front and a '>>' behind, \n"
      "that means that you've got the right letter in the right place. \n"
      "If any of your letters have a '!!' in front and behind, \n"
      "that means that you've got the right letter but in the wrong place. \n"
      "Otherwise, if nothing in front or behind the letter, the letter is not in the word. \n"
      "GLHF! \n"
      "~~~~~~~~~~~~ \n"
      "~~~~~~~~~~~~")
def user_guesses(word_list):
    word = random.choice(word_list)
    word = word.upper()
    print(word)
    con = True
    times = 1
    while con is True:
        guessed_word = []
        list_guessed_words = []
        guess = input("Guess a five letter word:")
        guess = guess.upper()
        if len(guess) > 5 or len(guess) < 5:
            guess = input("You MUST enter a 5 letter word:")
        list_guessed_words.append(guess)
        print(*list_guessed_words, sep='\n')
        #This checks wheather the word is eligible
        guess = list(guess)
        word = list(word)
        correct = []
        for i in range(5):
            if guess[i] == word[i]:
                wordle = "<<" + guess[i] + ">>"
                guessed_word.append(wordle)
                correct.append(guess[i])
                continue
            letter_in_word = False
            for v in range(5):
                if guess[i] == word[v]:
                    wordle = "!!"+guess[i]+"!!"
                    guessed_word.append(wordle)
                    letter_in_word = True
                    break
            if letter_in_word == False:
                guessed_word.append(guess[i])
        list_of_list.append(guessed_word)
        for guessed_word in list_of_list:
            print(guessed_word)
        if len(correct) == 5:
            print("Correct!")
            con = False
            exit()
        else:
            con = True
        times = times + 1


user_guesses(word_list)



#def main(word_list, guessed_letters):
