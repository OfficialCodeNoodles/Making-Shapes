from math import ceil

def printIsoscelesTriangle(width: int):
    height = ceil(width / 2) 

    for y in range(0, height):
        spaces = height - y 

        for space in range(0, spaces):
            print(' ', end = '') 
        for x in range(0, (y * 2) + 1):
            print('*', end = '')
        print() 

if __name__ == "__main__":
    while True:
        width = int(input("Type the width of your triangle: "))

        print()
        printIsoscelesTriangle(width)
        print()
