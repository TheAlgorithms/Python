def moveTower(height, fromPole, toPole, withPole):  
    '''
    >>> moveTower(3, 'A', 'B', 'C')
    moving disk from A to B
    moving disk from A to C
    moving disk from B to C
    moving disk from A to B
    moving disk from C to A
    moving disk from C to B
    moving disk from A to B
    '''
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp,tp):
    print('moving disk from', fp, 'to', tp)

def main():
    height = int(input('Height of hanoi: '))
    moveTower(height, 'A', 'B', 'C')

if __name__ == '__main__':
    main()
