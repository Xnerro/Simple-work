import os

class math():
    def add(x,y):
        return x+y
    
    def subtrac(x,y):
        return x-y
    
    def divide(x,y):
        return x/y
    
    def multiply(x,y):
        return x*y
    
    def square(x):
        return x**2

class solver():
    
    def add(total,x,y):
        total.append(math.add(x,y))
        x = total[-1]
        res = int(x)
        x = res
        total = []
        return x

    def subtrac(total,x,y):
        total.append(math.subtrac(x,y))
        x = total[-1]
        res = int(x)
        x = res
        total = []
        return x
    
    def devide(total,x,y):
        total.append(math.divide(x,y))
        x = total[-1]
        res = int(x)
        x = res
        total = []
        return x

    def multiply(total,x,y):
        total.append(math.multiply(x,y))
        x = total[-1]
        res = int(x)
        x = res
        total = []
        return x

    def square(total,x):
        total.append(math.square(x))
        x = total[-1]
        res = int(x)
        x = res
        total = []
        return x

def view():
    print('============================')   
    print('\t Calculator ')   
    print('============================')

view()
total = []
x = int(input("num: "))
z = ''
while z != '=':
    z = input("Operator: ")
    if z == '+':
        y = int(input("num: "))
        x = solver.add(total,x,y)
        os.system('clear')
        view()
        print("num: ",x)
    elif z == '-':
        y = int(input("num: "))
        x = solver.subtrac(total,x,y)
        os.system('clear')
        view()
        print("num: ",x)
    elif z == '/' or z ==':':
        y = int(input("num: "))
        x = solver.devide(total,x,y)
        os.system('clear')
        view()
        print("num: ",x)
    elif z == 'x' or z == '*':
        y = int(input("num: "))
        x = solver.multiply(total,x,y)
        os.system('clear')
        view()
        print("num: ",x)
    elif z == 'sqrt' or z == '^2':
        x = solver.square(total,x)
        os.system('clear')
        view()
        print("num: ",x)
    else:
        print('Operator not available')

os.system('clear')

view()
print("num: ",x)
    

    

