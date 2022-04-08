def printRightTriangle(height: int):
    for y in range(0, height):
        for x in range(0, y + 1):
            print('*', end = '') 
        print()

if __name__ == "__main__":
    while True:
        height = int(input("Type the height of your triangle: "))

        print() 
        printRightTriangle(height)
        print() 
