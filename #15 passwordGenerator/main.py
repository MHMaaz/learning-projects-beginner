import random as rd
MIN_TO_MAX_PASS_LEN = [6, 8, 10, 12, 14]
symbols = ["!", "@", "#", "$", "%", "&", "*", "^", ">", "<", "~"]
alphabets = ["a","b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_pass(length):
    print(" # Generating Password # ")
    password = str()
    i = 0
    
    for v in range(0, len(alphabets)): # using range, since using for loop was triggering the indexes to be str not int
        bool = rd.choice([True, False]) # chance system
        if bool:
            alphabets[v] = alphabets[v].capitalize()
    
    to_choose = [
        symbols,
        alphabets,
        numbers
    ]
    while i < length:
        rand_list = rd.choice(to_choose)
        rand_item = rd.choice(rand_list)
        password += rand_item
        i += 1
    
    print(f"Your required password is : {password}")
    

def get_pass_len():
    len = rd.choice(MIN_TO_MAX_PASS_LEN)
    return len

def main():
    pass_len = get_pass_len()
    get_pass(pass_len)

if __name__ == "__main__":
    main()