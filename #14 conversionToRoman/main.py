OUT_OF_BOUND_LENGTH = 4

roman_nums = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
roman_first_digits = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # first number initializer
roman_3_digits = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # first number initializer for 3 digit numerals

def get_process_3_roman(number):
    roman_number = str()
    number = str(number)
    initial = str()
    middle_dig = str()
    other_dig = str()
    initial += number[0]
    middle_dig += number[1]
    other_dig += number[2] # breaking down the number into multiple codeable parts
    initial = int(initial)
    middle_dig = int(middle_dig)
    other_dig = int(other_dig)
    
    if roman_3_digits[initial - 1]:
        roman_number += roman_3_digits[initial - 1]
    if roman_first_digits[middle_dig - 1] and middle_dig != 0:
        roman_number += roman_first_digits[middle_dig - 1]
    if roman_nums[other_dig - 1] and other_dig != 0:
        roman_number += roman_nums[other_dig - 1]
    return roman_number

def get_from_ten_roman_no(number):
    roman_no = str()
    number = str(number)
    num_length = len(number)
    first_dig = number[0:(num_length - 1)] # seperated the first digit
    other_dig = number[1:len(number)] # and whatever coming after upto its length
    first_dig = int(first_dig)
    other_dig = int(other_dig)
    print(first_dig, other_dig) # debug
    if roman_first_digits[first_dig - 1] in roman_first_digits:
       roman_no += roman_first_digits[first_dig - 1]
    
    if other_dig <= 10 and other_dig != 0: # to avoid any extra numerals, making sure its not equal to zero
        roman_no += roman_nums[other_dig - 1]
    
    return roman_no

def get_upto_ten_roman_no(number):
    place_in_roman_nums = number - 1 # "- 1" since indexing starts from 0, to get exact value, have to decrement "1"
    return roman_nums[place_in_roman_nums]

def decide_len(number):
    length = len(str(number))
    if length == 1 or number == 10: 
        return True
    elif length >> 1:
        return False

def get_num():
    while True:
        num = input("Enter a number to convert it to Roman Number : ")
        if num.isdigit():
            if len(num) < OUT_OF_BOUND_LENGTH:
                num = int(num)
                if num > 0:
                    return num
                else:
                    print("Enter a valid natural number.")
            else:
                print("Enter a valid number.  \"1 to 999\"")
        else:
            print("Enter a valid number.")

def main():
    process_3 = False
    num_to_convert = get_num()
    num_is_upto_ten = decide_len(num_to_convert) # either true of false
    num_to_convert = str(num_to_convert)
    num_length = len(num_to_convert)
    if num_length == 3:
        process_3 = True # permission for third function to run 
    
    num_to_convert = int(num_to_convert)
    if num_is_upto_ten and not process_3:
        result = get_upto_ten_roman_no(num_to_convert)
        print(f"\n\t# \'{num_to_convert}\' = {result}\a")
    elif not num_is_upto_ten and not process_3:
        result = get_from_ten_roman_no(num_to_convert)
        print(f"\n\t# \'{num_to_convert}\' = {result}\a")
        
    if process_3: # process 3 means a computation regarding 3 digits
        result = get_process_3_roman(num_to_convert)
        print(f"\n\t# \'{num_to_convert}\' = {result}\a")
    
if __name__ == "__main__":
    main()