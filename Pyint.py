while True:

    print('===========================')
    print('*** Welcome to Pyint!!! ***')
    print('___________________________')
    print('*** Drawing With Turtle ***')
    print('___________________________')
    print('******* ver. 1.2.0 ********')
    print('___________________________')
    print('===========================')

    import turtle as t

    t.color('white')
    t.bgcolor('black')
    t.speed(0)
    t.shape('classic')
    t.pensize(4)
    t.left(90)
    break


def settings():
        
        while True:

            print('------------------------')
            print('*** Entered Settings ***')
            print('------------------------')

            chgpencolor = t.color(str(input('Pencolor?:')))
            chgbgcolor = t.bgcolor(str(input('BGcolor?:')))
            savesettings = str(input())

            if savesettings == 'ss':
                print('-----------------------')
                print('**** Quit Settings ****')
                print('-----------------------')
                break

while True:
    
    ipt = str(input())

    if ipt == 'es':
        settings()
    elif ipt == 'w':
        t.forward(10)
    elif ipt == 'a':
        t.left(90)
        t.forward(10)
    elif ipt == 's':
        t.backward(10)
    elif ipt == 'd':
        t.right(90)
        t.forward(10)
    elif ipt == 'q':
        t.left(45)
    elif ipt == 'e':
        t.right(45)
    elif ipt == 'h':
        t.goto(0,0)
    elif ipt == 'c':
        t.clear()
    elif ipt == 'z':
        t.undo()
    elif ipt =='pu':
        t.penup()
    elif ipt =='pd':
        t.pendown()
    if ipt == 'gg':
        print('Are you really want to close the program? [y/n]')
    if ipt == 'n':
        continue
    elif ipt == 'y':
        break