# *
# **
# ***
# ****
# *****
menu = 1
while menu != 0 :
    print('1. default\n2.reverse\n3.diagonal\n4.diagonal reverse\n0.exit\n')
    menu = int(input('select > '))
    if menu == 1 :
        for i in range(5) :
            for j in range(i+1) :
                print('*',end = '')
            print()














            
    elif menu == 2 :
        for i in range(5) :
            for j in range(4-i) :
                print(' ',end = '')
            for j in range(i+1) :
                print('*',end = '')
            print()
    elif menu == 3 :
        for i in range(5) :
            for j in range(i+1) :
                if i == j :
                    print('*',end = '')
                else :
                    print(' ',end = '')
            print()
    elif menu == 4 :
        for i in range(5) :
            for j in range(5) :
                if i == 4-j :
                    print('*',end = '')
                else :
                    print(' ',end = '')
            print()
    elif menu == 0:
            break
