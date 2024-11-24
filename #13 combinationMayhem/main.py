import random as rd
EASY = 4
EASY_MULTIPLIER = 1
EASY_LIVES = 6
MEDIUM = 6
MEDIUM_MULTIPLIER = 2
MEDIUM_LIVES = 8
HARD = 8
HARD_MULTIPLIER = 3
HARD_LIVES = 10

def display_altered_combo(hidden_combo):
    print(f"\n\t|| {(" ").join(hidden_combo)} ||")

def get_input(num_to_guess, combination):
    while True:
        user_input = input(f"(starting from \"1\" upto last position \"{len(combination)}\")\n\t* Enter which position does \"{num_to_guess}\" belong to : ")
        
        if user_input.isdigit():
            user_input = int(user_input)
            user_input -= 1
            if user_input <= (len(combination) - 1) and user_input >= 0:
                return user_input
            else:
                print("\t*Enter a valid number")
        else:
            print("\t*Enter a valid number")
            continue

def display_n_switches(switches):
    hidden_symbol = ["#"]
    hidden_combo = hidden_symbol * len(switches)
    print(f"\n\t|| {(" ").join(hidden_combo)} ||") # joining for a neat look
    return hidden_combo

def get_combination(amnt_of_switches):
    picked_switches = []
    
    for _ in range(amnt_of_switches): # run as long as the amount is for (if 8 then will run 8 times)
        while True: # to prevent picking the already existing selected switch and skipping, made the code look for the item
            selection = rd.choice(range(1, amnt_of_switches + 1))
            if selection not in picked_switches:
                picked_switches.append(selection)
                break # breaking from the WHILE loop
            else:
                continue
    
    return picked_switches # returning a list

def get_difficulty():
    print("\t # CHOOSE your DIFFICULTY")
    while True:
        diff = input("\t # (easy, medium, hard) : ").lower()
        
        if diff == "easy":
            return EASY
        elif diff == "medium":
            return MEDIUM
        elif diff == "hard":
            return HARD
        else:
            print("Enter valid difficulty")
            continue

def main():
    no_of_switches = get_difficulty()
    combination = get_combination(no_of_switches)
    score = int()
    mistake = False
    loose_counter = int()
    continue_game = True
    hidden_combo_altered = False
    lost = False
    hidden_combo = display_n_switches(combination)
    while continue_game:
        for i in range(1, len(combination) + 1):
            not_guessed = True
            while not_guessed:
                if no_of_switches == EASY:
                    print(f"\n\t# TOTAL LIVES : {EASY_LIVES - loose_counter}")
                elif no_of_switches == MEDIUM:
                    print(f"\n\t# TOTAL LIVES : {MEDIUM_LIVES - loose_counter}")
                else:
                    print(f"\n\t# TOTAL LIVES : {HARD_LIVES - loose_counter}")
                guess = get_input(i, combination)
                if combination[guess] == i: # if place inputted of combination is pre much equal to the ordered number
                    hidden_combo[guess] = "O"
                    hidden_combo_altered = True
                    print(f"You guessed the right order of \"{i}\"")
                    not_guessed = False
                    score += 1
                    mistake = False
                    if hidden_combo_altered:
                        display_altered_combo(hidden_combo)
                    else:
                        display_n_switches(combination)
                else:
                    loose_counter += 1
                    for i in range(0, len(hidden_combo)):
                        hidden_combo[i] = "#" # flipping all answers back to normal
                    
                    print("\n\t# Try again")
                    if hidden_combo_altered:# just displaying
                        display_altered_combo(hidden_combo)
                    else:
                        display_n_switches(combination)
                    
                    if no_of_switches == EASY and loose_counter == EASY_LIVES:
                        print("\n\t# You lost")
                        continue_game = False
                        lost = True
                    elif no_of_switches == MEDIUM and loose_counter == MEDIUM_LIVES:
                        print("\n\t# You lost")
                        continue_game = False
                        lost = True
                    elif no_of_switches == HARD and loose_counter == HARD_LIVES:
                        print("\n\t# You lost")
                        continue_game = False
                        lost = True
                    mistake = True
                    break
            if "#" not in hidden_combo:
                continue_game = False
                break
            
            if mistake:
                break
    
    if not lost:
        if no_of_switches == MEDIUM:
            print(f"\n\t* Your score would be : {score * MEDIUM_MULTIPLIER}")
        elif no_of_switches == HARD:
            print(f"\n\t* Your score would be : {score * HARD_MULTIPLIER}")
        else:
            print(f"\n\t* Your score would be : {score * EASY_MULTIPLIER}")
if __name__ == "__main__":
    main()