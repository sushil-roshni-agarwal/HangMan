from words import words
import random
import string

def hangMan():
    random_word=random.choice(words)
    while('-' in random_word or " " in random_word):
        random_word=random.choice(words)
    random_word=random_word.upper()
    print(random_word)
    random_word.capitalize()
    letters_in_word=set(random_word)
    life=7

    all_alphabtets=set(string.ascii_uppercase)
    gussed_letters=set()

    while(len(letters_in_word)>0 and life>0):
        print("lives left "+str(life))
        print("Used Letters: "+ " "+" ".join(gussed_letters))
        s=''
        for i in random_word:
            if(i in gussed_letters):
                print(i)
                s+=i
                s.join(i) 
            else:
                s+=' _'
        
        print(s)

        print("Guess a letter")
        gussed_letter= input().upper()
        if gussed_letter in letters_in_word:
            print("You have gussed right letter")
            gussed_letters.add(gussed_letter)
            if gussed_letter in letters_in_word:
                letters_in_word.remove(gussed_letter)
            if gussed_letter in all_alphabtets:
                all_alphabtets.remove(gussed_letter)
        
        elif gussed_letter in gussed_letters:
            print("You have aldready used this letter")
        
        elif gussed_letter in all_alphabtets:
            print("Wrong guess")
            life=life-1
        else:
            print("Invalid character, please try again ")
            
        if(len(letters_in_word)<=0):
            print("CONGRATS! You have gussed the word right")
        
        if(life<=0):
            print("Sorry! You have expired your lives")

while(True):
    print("Do you want to play? type y for yes and n for no")
    answer=input().upper()
    if(answer == 'Y'):
        hangMan()
    else:
        break
    

    