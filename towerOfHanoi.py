"""Tower of Hanoi"""

def moveDisk(n, source, destination, temp):
    if n == 1:
        print(f'Move from {source} to {destination}')
    else:
        moveDisk(n - 1, source, temp, destination)
        moveDisk(1, source, destination, temp)
        moveDisk(n - 1, temp, destination, source)

def main():
    n = int(input('Enter the number of disks: '))
    moveDisk(n, 'A', 'C', 'B')

if __name__ == '__main__':
    main()