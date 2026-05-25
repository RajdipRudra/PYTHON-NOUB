import random as rn
from hangman_word import WOrdS,words_hints
import hangman_art
import os

print(hangman_art.logo)


GenWord = rn.choice(WOrdS).lower()
Hint = words_hints[GenWord]
HangStage = hangman_art.stages
LifeLine = len(HangStage)-1

print(GenWord)


def dash(word):
    word_list = []
    for i in word:
        word_list.append(" _")
    return word_list

# dash(GenWord)

def dashReplace(dash,word,user_input):
    for j in range(len(word)):
        if word[j]==user_input:
            dash[j] = user_input
    return dash



is_gameon = LifeLine
Dashe = dash(GenWord)
while is_gameon >= 0:

    if "".join(Dashe)!=GenWord:
        os.system("clear") 
        print(hangman_art.logo)
        if is_gameon<LifeLine:
            print(HangStage[is_gameon])
        print(f"YOU HAVE ({(" ❤️ ")*is_gameon}) lifes left")
        print("Hint-> "+Hint)
        user_input = input(f"{"".join(Dashe)} Guess a letter --> ").lower()
        if user_input in GenWord:
            Dashe = dashReplace(Dashe,GenWord,user_input)
        else:
            is_gameon-= 1
            if is_gameon==0:
                os.system("clear") 
                print(HangStage[is_gameon])
                print("GAME OVER")
                print(f"The Word Was {GenWord}")
                break
            
    else:
        print("YOU WON")
        break




