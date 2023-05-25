def swap_case(s):
    new_word = ''
    for letter in s:
        if letter.isupper():
           new_word += letter.lower()
        elif letter.islower():
            new_word += letter.upper() 
        else:
           new_word += letter    
    return new_word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
