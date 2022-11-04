from fractions import Fraction
import numpy as np

def p(M, msg):
    print(f'{msg}\n{M}\ndeterminant is {np.linalg.det(M):.3f}')


class Determinant:
    def __init__(self, matrix: np.array, factor=1):
        self._matrix = matrix
        self._dim = len(matrix)
        self._values = matrix.copy()
        self._factor = Fraction(factor)
    @property
    def values(self):
        return np.array(self._values)
    @property 
    def dim(self):
        return self._dim

    @property
    def det(self):
        return self._factor * np.linalg.det(self.values)
    def print_det(self, msg):
        print(msg)
        if self._factor != 1:
            print(f'factor: {self._factor}')
        print(f'{self.values}\ndeterminant is {self.det:.3f}')        

    def add_row(self, source_row, source_factor, dest_row):
        for col in range(self.dim):
            self._values[dest_row][col] = self._values[dest_row][col] + source_factor * self._values[source_row][col]
    def add_col(self, source_col, source_factor, dest_col):
        for row in range(self.dim):
            self._values[row][dest_col] = self._values[row][dest_col] + source_factor * self._values[row][source_col]
    def mul_row(self, row, factor):
        for col in range(self.dim):
            self._values[row][col] = self._values[row][col] * factor
        self._factor = Fraction(factor, self._factor)
    def mul_col(self, col, factor):
        for row in range(self.dim):
            self._values[row][col] = self._values[row][col] * factor
        self._factor = Fraction(self._factor,factor)#self._factor/factor
    def sub_det(self, matrix_row, matrix_col):
        rows = []
        for r in range(self.dim):
            if r == matrix_row:
                continue
            row = []
            for c in range(self.dim):
                if c == matrix_col:
                    continue
                row.append(self.values[r][c])
            rows.append(row)
        return Determinant(rows, self._factor)

D = Determinant([[-8,-5,4,5],[4,2,-2,-6],[-3,7,2,-3],[-2,-4,1,3]])
D.print_det('initial')
D.add_row(3, 1, 2)
D.print_det('rij 4 bij rij 3 optellen')
D.add_col(1, -1, 2)
D.print_det('kolom 2 van kolom 3 aftrekken')
D.mul_col(0, Fraction(-1,5))
D.print_det('delen van kolom 1 door -5 (dat betekent dat de determinant ook door -5 wordt gedeeld, dat moet je compenseren door daarna met -5 te vermenigvuldigen)')
D.add_col(0, -3, 1)
D.print_det('trek 3 maal kolom 2 van kolom 1 af')
print('Nu kan je de determinant ontwikkelen vanuit rij drie')
D2 = D.sub_det(2,0)
D2.print_det('subdeterminant')
D2.mul_col(0,-1/9.8)
D2.print_det('deel eerste kolom door -9.8')
D2.add_col(0,-9,1)
D2.print_det('tel -9 maal eerste kolom op bij tweede kolom')
D2.add_col(0,-5,2)
D2.print_det('tel -5 maal eerste kolom op bij derde kolom')
print('Nu kan je de determinant ontwikkelen vanuit rij een')
D3 = D2.sub_det(0,0)
D3.print_det('Dit is de vereenvoudigste vorm')
D3.mul_col(0,49)
D3.mul_col(1,49)
D3.print_det('Dit is de vereenvoudigste vorm')


# A = np.array([[-8,-5,4,5],[4,2,-2,-6],[-3,7,2,-3],[-2,-4,1,3]])

# p(A, 'oorspronkelijk')

# A1=np.array([[-8,-5,4,5],[4,2,-2,-6],[-5,3,3,0],[-2,-4,1,3]])
# p(A1, 'r3 = r3+r4')

# A2=np.array([[-8,-5,9,5],[4,2,-2,-6],[-5,3,3,0],[-2,-4,1,3]])
# p(A1, 'r3 = r3+r4')
