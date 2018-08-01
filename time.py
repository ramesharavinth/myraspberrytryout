import datetime as timevar
import array


def getcurrenttime():
    print('Current Time is :' + str(timevar.datetime.now()))
    print('Current date is :' + str(timevar.datetime.today()))



def evaluateinputs():
    print("He said, \nHello there! ")
    print('2' * 3)
    x = '2'
    y = '3'
    z = int(x) + int(y)
    print(z)

def printvariables():
    x = 3+5j
    y = 5j
    z = -5j

    print(type(x))
    print(type(y))
    print(type(z))

def castingvariables():
    x = int(1)
    y = int(1.3)
    z = int('str')

    print((x))
    print((y))
    print((z))



#getcurrenttime()
#evaluateinputs()
#printvariables()
#castingvariables()

