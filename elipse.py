from math import sqrt   

class Grid(object):
    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height
        self.grid = [[False for x in range(0, width)] 
            for y in range(0, height)]
        self.center = ( self.width // 2, self.height // 2 )  
    def generateElipse(self, xRadius: int, yRadius: int):
        xRadius *= xRadius
        yRadius *= yRadius 

        for y in range(0, self.height):
            for x in range(0, self.width):
                deltaX = float(self.center[0] - x) 
                deltaY = float(self.center[1] - y) * (5 / 3)
                distance = (pow(deltaX, 2) / xRadius) + (pow(deltaY, 2) / yRadius)

                self.grid[y][x] = distance <= 1
    def __str__(self):
        string = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                string += '*' if self.grid[y][x] else ' ' 
            string += '\n' 
        return string 

if __name__ == "__main__":
    while True:
        xRadius = int(input("Type the x-radius of your elipse: "))
        yRadius = int(input("Type the y-radius of your elipse: ")) 

        circle = Grid((xRadius * 2) + 1, (yRadius * 2) + 1)
        circle.generateElipse(xRadius, yRadius)

        print('\n', circle, '\n')  
