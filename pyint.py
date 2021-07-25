from turtle import Screen, st

screen = Screen()
import turtle as t

print('===========================')
print('*** Welcome to Pyint!!! ***')
print('___________________________')
print('*** Drawing With Turtle ***')
print('___________________________')
print('******* ver. 2.1.0 ********')
print('___________________________')
print('===========================')

t.color('white')
t.bgcolor('black')
t.speed(0)
t.shape('circle')
t.pensize(5)
t.shapesize(2,2,2)

def pencolorsettings():

    while True:

        print('--------------------------')
        print('*** Pen Color Settings ***')
        print('--------------------------')

        chgpencolor = t.color(str(input('Pen Color?:')))
        savepencolorsettings = str(input('Save the settings? [y/n]:'))

        if savepencolorsettings == 'n':
            continue
        elif savepencolorsettings == 'y':
            print('-------------')
            print('*** Saved ***')
            print('-------------')
            break

def bgcolorsettings():

    while True:

        print('--------------------------------')
        print('*** Background Color Setting ***')
        print('--------------------------------')

        chgbgcolor = t.bgcolor(int(input('Background Color?:')))
        savebgcolorsettings = str(input('Save the settings? [y/n]:'))

        if savebgcolorsettings =='n':
            continue
        elif savebgcolorsettings == 'y':
            print('-------------')
            print('*** Saved ***')
            print('-------------')
            break

def penthicknesssettings():
        
        while True:

            print('------------------------------')
            print('*** Pen Thickness Settings ***')
            print('------------------------------')

            chgpenthickness = t.pensize(int(input('Thickness?:')))
            savepenthicknesssettings = str(input('Save the settings? [y/n]:'))

            if savepenthicknesssettings == 'n':
                continue
            elif savepenthicknesssettings == 'y':
                print('-------------')
                print('*** Saved ***')
                print('-------------')
                break

def move_pen(x, y):

    t.ondrag(None)
    t.penup()
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(move_pen)

def draw_pen(x, y):

    t.ondrag(None)
    t.pendown()
    t.setheading(t.towards(x, y))
    t.goto(x,y)
    t.ondrag(draw_pen)

t.onscreenclick(draw_pen, 1)
t.onscreenclick(move_pen, 3)

while True:
    
    ipt = str(input())

    if ipt == 'pencolor':
        pencolorsettings()
    elif ipt == 'penthickness':
        penthicknesssettings()
    elif ipt =='bgcolor':
        bgcolorsettings
    elif ipt == 'h':
        t.goto(0,0)
    elif ipt == 'c':
        t.clear()
    elif ipt == 'z':
        t.undo()
    elif ipt == 'gg':
        print('Are you really want to close the program? [y/n]')
    elif ipt == 'n':
        continue
    elif ipt == 'y':
        break
