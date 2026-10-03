def passwordchecker(password):
    numbercount = 0
    alphabetcount = 0
    specialchcount = 0
    uppercount = 0
    lowercount = 0

    for char in password:
        if char.isdigit():
            numbercount += 1
        elif char.isalpha():
            alphabetcount += 1
            if char.isupper():
                uppercount += 1
            else:
                lowercount += 1
        else:
            specialchcount += 1

    print('NO. OF NUMERIC VALUES FOUND:', numbercount)
    print('NO. OF ALPHABETIC VALUES FOUND:', alphabetcount)
    print('NO. OF SPECIAL CHARACTERS FOUND:', specialchcount)

    if len(password) < 8:
        print("Password too short!!! Minimum 8 characters required.")
        print("WEAK PASSWORD!")
    elif numbercount > 0 and alphabetcount > 0 and specialchcount > 0 and uppercount > 0 and lowercount > 0:
        print('STRONG PASSWORD')
    else:
        print('Password should contain numbers, alphabets (both cases), and special characters.')
        print('WEAK PASSWORD!')


# Main program
print('>>> WELCOME TO PASSWORD CHECKER <<<')
passinput = input("ENTER A PASSWORD: ")

if not passinput:
    print('Password cannot be empty!')
else:
    passwordchecker(passinput)
