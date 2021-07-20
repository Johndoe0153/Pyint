while True:

    print('---------------------------')
    print('*** Welcome to Pyint!!! ***')
    print('===========================')
    print('*** Drawing With Turtle ***')
    print('===========================')
    print('******* ver. 1.1.0 ********')
    print('===========================')
    print('---------------------------')

    import turtle as t

    t.color('white')
    t.bgcolor('black')
    t.speed('fastest')
    t.shape('classic')
    t.pensize(5)
    t.left(90)
    break

def settings():
    
        while True:

            entersettings = str(input('Press Enter for enter settings'))
            chgpencolor = t.color(str(input('Pencolor?:')))
            chgbgcolor = t.bgcolor(str(input('BGcolor?:')))
            savesettings = str(input())
        
            if entersettings == 'es':
                print('*** Entered Settings ***')
            elif savesettings == 'ss':
                print('*** Quit Settings ***')
                break

while True:   
    
    ipt = str(input())
        
    if ipt == 'es':
        settings()
    elif ipt == 'w':
        t.forward(20)
    elif ipt == 'a':
        t.left(90)
        t.forward(20)
    elif ipt == 's':
        t.backward(20)
    elif ipt == 'd':
        t.right(90)
        t.forward(20)
    elif ipt == 'q':
        t.left(45)
    elif ipt == 'e':
        t.right(45)
    elif ipt == 'h':
        t.home()
    elif ipt == 'c':
        t.clear()
    elif ipt == 'z':
        t.undo()
    elif ipt == 'gg':
        break