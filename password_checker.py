p = input("Enter your password: ")
string = []
is_strong = True

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.' , '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '\\', '^', '_', '`', '{', '}', '|', '~']
common = ['admin1234', 'password', '12345678', '123456789', '1234567890', 'qwerty123', 'password1','iloveyou', 'hello123', 'hello1234']

if len(p) < 8:
    print("Your password needs to have a minimum of 8 characters.")
    is_strong = False

else:
    for char in p:
        string.append(char)
        
    if not set(string) & set(upper_case):
        print("Your password needs at least one uppercase letter.")
        is_strong = False
            
    if not set(string) & set(lower_case):
        print("Your password needs at least one lowercase letter.")
        is_strong = False
        
    if not set(string) & set(digit):
        print("Your paswword needs at least one digit.")
        is_strong = False
    
    if not set(string) & set(special_char):
        print("Your password needs at least one special character.")
        is_strong = False
        
    if p in common:
        print("Your password is too guessable. Try a new one.")
        is_strong = False
        
    if is_strong: 
        print("Your password is strong.")
