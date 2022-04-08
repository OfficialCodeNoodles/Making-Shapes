def printRectangle(width: int, height: int):
    for y in range(0, height):
        for x in range(0, width):
            print('*', end = '') 
        print() 

if __name__ == "__main__":
    while True:
        width = int(input("Type the width of your rectangle: "))      
        height = int(input("Type the height of your rectangle: "))

        print()
        printRectangle(width, height) 
        print() 
