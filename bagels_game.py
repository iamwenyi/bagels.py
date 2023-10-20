import random

win_status = "Lose"

def code_generator():
    code_comp = []
    while len(code_comp) < 3:
        int_digit = random.randint(0,9)
        digit = str(int_digit)
        if digit not in code_comp:
            code_comp.append(digit)
            
    return code_comp

def correct_digit_checker(code_comp,code_user):
    correct_digits = 0
    
    for x in range(len(code_comp)):
        digit_user = code_user[x]
        
        if digit_user in code_comp:
            correct_digits += 1
            
    return correct_digits

def results(attempts,code_comp,code_user):
    correct_digits = correct_digit_checker(code_comp,code_user)
    
    if correct_digits != 0:
        position_correct_digits = 0
        for x in range(len(code_comp)):
            digit_user = code_user[x]
        
            if digit_user in code_comp:
                pos_digit_codeuser = code_user.index(digit_user)
                pos_digit_codecomp = code_comp.index(digit_user)
            
                if pos_digit_codeuser == pos_digit_codecomp:
                    position_correct_digits += 1
                else:
                    if attempts > 1:
                        print("Pico ", end = "")
                    win_status = "Lose"
                
        if position_correct_digits == 3:
            win_status = "Win"
        else:
            if attempts > 1:
                for x in range(position_correct_digits):
                    print("Fermi ", end = "")
                            
            win_status = "Lose"
    else:
        if attempts > 1:
            print("Bagels ", end = "")
        win_status = "Lose"
          
    return win_status

def answer_display(code_comp):
    for digit in code_comp:
        print("".join(digit))
    
def menu_display():
    print("")
    print("Welcome to Bagels!")
    print("I have thought of a 3-digit code. Try to guess what it is in 10 guesses.")
    print("")
    print("When I say:    That means:")
    print("Pico           One digit is correct but in the wrong position.")
    print("Fermi          One digit is correct and in the right position.")
    print("Bagels         No digit is correct.")
    print("")
    print("Good luck!")

def main():
    try_again = True
    
    while try_again == True:
        attempts = 10
        menu_display()
        code_comp = code_generator()
        print(code_comp)
        
        while attempts > 0:
            print("","\n")
            print(f"You have {attempts} attempt(s)")
            code_user = input("Enter your guess: ") 
            win_status = results(attempts,code_comp,code_user)
            
            if win_status == "Win":
                attempts = 0
                print("\nYou got it!")
            else:
                attempts -= 1
                
            if attempts == 0 and win_status == "Lose":
                print("")
                print("The answer was ", end = "")
                for digit in code_comp:
                    print("".join(digit),end = "")
                
        if attempts == 0:
            ask_tryagain = input("\nTry again?: ").lower()
            if ask_tryagain == "yes":
                try_again = True
            else:
                print("Thanks for playing!")
                try_again = False
            
main()
