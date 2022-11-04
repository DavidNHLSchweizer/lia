import numpy as np
from fractions import Fraction
from lia import PRECISION

class Determinant:
    def __init__(self, matrix: np.array, factor=1):
        self._matrix = matrix
        self._dim = len(matrix)
        self._values = matrix.copy()
        self._factor = factor
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
    def simplify_determinant(self, target = 0, is_row = True):
        if is_row:
            self._simplify_row(target)
        else:
            self._simplify_col(target)
    def _simplify_row(self, target_row):
        c = 0
        while c < self.dim and round(self.values[target_row][c],PRECISION) == 0:
            c+=1
        if c >= self.dim:
            return
        self.mul_row(target_row, 1/self.values[c])
        for c2 in range(c+1,self.dim):
            self.add_col(c, -self.values[target_row][c2], c2)
    def _simplify_col(self, target_col):
        pass
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
D.simplify_determinant()
D.print_det('simpled')
