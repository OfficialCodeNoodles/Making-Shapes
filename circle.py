from math import sqrt   

class Grid(object):
    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height
        self.grid = [[False for x in range(0, width)] 
            for y in range(0, height)]
        self.center = ( self.width // 2, self.height // 2 )  
    def generateCircle(self, radius: int):
        for y in range(0, self.height):
            for x in range(0, self.width):
                deltaX = float(self.center[0] - x) 
                deltaY = float(self.center[1] - y) * (5 / 3)
                distance = sqrt(pow(deltaX, 2) + pow(deltaY, 2))

                self.grid[y][x] = distance <= radius 
    def __str__(self) -> str:
        string = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                string += '*' if self.grid[y][x] else ' ' 
            string += '\n' 
        return string 

if __name__ == "__main__":
    while True:
        radius = int(input("Type the radius of your circle: ")) 

        circle = Grid((radius * 2) + 1, (radius * 2) + 1)
        circle.generateCircle(radius)

        print('\n', circle, '\n') 
