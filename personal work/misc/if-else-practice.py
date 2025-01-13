# Arden Boettcher
# 9/10
# if-else practice

please = 'I would really like to have python installed on my computer for CTC.'
reasons = 'Without python I cannot debug/run any code using visual studio which would make it impossible to do check my work.'
extra_reasons = 'I am caught up with all of my work and I want it for purely school related reasons.'
# I don't have Python installed on my school computer and I am not able to install it myself because I need permission

while True:
    print(please)
    print('Do I have your permission Y/N?')
    check1 = input()

    if check1 == 'no': # edit: It works! When it gets an input that isn't yes or no then it goes back to the beginning 
        print(reasons) # But I would like it to go back to the last question (I have no idea how to do that)
        print('Please say yes')
        check2 = input()

        if check2 == 'no':
            print(extra_reasons)
            print('Please :(')
            check3 = input()
                
            if check3 == 'no':
                print(':(')
                break
            elif check3 == 'yes':
                print('THANK YOU SO MUCH')
                break
            else:
                print('Yes or no')
        elif check2 == 'yes':
            print('Thank you')
            break
        else:
            print('Yes or no')
    elif check1 == 'yes':
        print('Thank you')
        break
    else:
        print('Yes or no')
