from math import ceil 

def printTrapezoid(height: int, top: int):
    for y in range(0, height):
        spaces = height - y 

        for space in range(0, spaces):
            print(' ', end = '')
        for x in range(0, (y * 2) + top):
            print('*', end = '')
        print()

if __name__ == "__main__":
    while True:
        height = int(input("Type the height of your trapezoid: "))
        top = int(input("Type the top size of your trapezoid: "))
        
        print()
        printTrapezoid(height, top) 
        print() 
