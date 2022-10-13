import numpy as np

def _print_determinant(msg, M):
    print(f'{msg}:\nmatrix =\n{M}\ndeterminant = {round(np.linalg.det(M),4)}')

def opgaven_hfst5():
    _print_determinant('A', np.array([[1,-1],[2,3]]))
    _print_determinant('B', np.array([[2,0,4],[1,1,2],[4,-1,8]]))
    _print_determinant('C', np.array([[3,-1,0],[2,1,4],[5,0,4]]))
    _print_determinant('D', np.array([[-1,0,6],[1,4,3],[2,1,4]]))
    _print_determinant('E', np.array([[-1,0,0,6],[-1,6,-1,4],[1,4,0,3],[2,1,0,4]]))
    _print_determinant('F', np.array([[-1,2,5,3],[6,4,1,0],[1,0,2,-4],[5,6,6,3]]))
    _print_determinant('G', np.array([[-1,0,-2,1],[3,6,-1,0],[4,6,5,1],[1,8,3,4]]))
    _print_determinant('H', np.array([[7,3,1,4],[5,1,2,-3],[1,3,0,7],[8,2,1,0]]))

def extra_opgaven_hfst5():
    _print_determinant('A', np.array([[1,-2],[-3,6]]))
    _print_determinant('B', np.array([[3,2],[1,4]]))
    _print_determinant('C', np.array([[2,0,1],[-1,2,7],[3,0,2]]))
    _print_determinant('D', np.array([[2,0,3],[5,2,6],[-1,4,3]]))
    _print_determinant('E', np.array([[3,9,-6],[-1,4,2],[2,0,-4]]))
    _print_determinant('F', np.array([[-2,2,0,3],[-7,5,2,6],[-1,4,0,3],[5,-2,-2,-1]]))
    _print_determinant('G', np.array([[7,2,11,4],[0,1,0,2],[5,-3,8,-6],[9,2,7,5]]))

def hfst5():
    print('HOOFDSTUK 5\n')
    print('OPGAVEN')
    opgaven_hfst5()
    print('EXTRA OPGAVEN')
    extra_opgaven_hfst5()
    print('*** EINDE ***')

if __name__ == '__main__':
    hfst5()

