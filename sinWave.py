from math import sin 

def printSinWave(frequency: float, amplitude: float, width: int = 50):
    for x in range(0, width):
        height = amplitude * sin(x * frequency) + amplitude 
        height = int(height)

        for space in range(0, height):
            print(' ', end = '')
        print('*')

if __name__ == "__main__":
    while True:
        frequency = float(input("Type the frequency of the sin wave: "))
        amplitude = float(input("Type the amplitude of the sin wave: "))

        print()
        printSinWave(frequency, amplitude) 
        print() 
