import numpy as np

def _opgave1(M, msg):
    print(f'{msg}\ntransposed:\n{np.transpose(M)}')

def opgave1():
    _opgave1(np.array([[3,4,0,3],[2,0,7,-4],[-1,9,2,0]]),'opgave 1')

def _opgave2(M1, M2, M3, msg):
    print(f'{msg}\nproduct= \n{np.dot(np.dot(M1,M2), M3)}')

def opgave2():
    _opgave2(np.array([[3,0,2],[4,-1,1]]), np.array([[2,-1,-2],[1,3,1],[0,5,6]]), np.array([[1,2],[2,4],[-1,2]]), 'opgave 2')

def opgave1_extra():
    _opgave1(np.array([[2,5,-3,5],[1,0,4,0],[4,9,6,-1]]), 'extra opgave 1')

def opgave2_extra():
    _opgave2(np.array([[1,2],[2,4],[-1,2]]), np.array([[3,0,2],[4,-1,1]]), np.array([[2,-1,-2],[1,3,1],[0,5,6]]), 'extra opgave 2')


def hfst3():
    print('HOOFDSTUK 3\n')
    print('OPGAVEN')
    opgave1()
    opgave2()
    print('EXTRA OPGAVEN')
    opgave1_extra()
    opgave2_extra()
    print('*** EINDE ***')
    
if __name__ == '__main__':
    hfst3()