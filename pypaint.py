while True:

        
    print('***Drawing With Turtle***')
    print('Type ss for Start!!')
    break

while True:   
    
    ipt = str(input())

    if ipt == 'ss':
        import turtle as t
        t.color('white')
        t.bgcolor('black')
        t.speed('fastest')
        t.shape('classic')
        t.pensize(5)
        t.left(90)

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