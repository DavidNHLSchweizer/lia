from __future__ import annotations
import numpy as np
from fractions import Fraction
from lia import PRECISION, is_one, is_zero

def _get_fac_str(factor):
    return f'{factor} keer ' if not is_one(factor) else ""


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
        if not is_one(self._factor):
            print(f'{msg}    factor: {self._factor:.3f}')
        else:
            print(msg)
        print(f'{self.values}\ndeterminant is {self.det:.3f}')        
    def report(self, msg):
        self.print_det(msg)
    def add_row(self, source_row, source_factor, dest_row):
        for col in range(self.dim):
            self._values[dest_row][col] = self._values[dest_row][col] + source_factor * self._values[source_row][col]       
        self.report(f'{_get_fac_str(source_factor)}rij {source_row+1} opgeteld bij rij {dest_row+1}')
    def add_col(self, source_col, source_factor, dest_col):
        for row in range(self.dim):
            self._values[row][dest_col] = self._values[row][dest_col] + source_factor * self._values[row][source_col]
        self.report(f'{_get_fac_str(source_factor)}kolom {source_col+1} opgeteld bij kolom {dest_col+1}')
    def mul_row(self, row, factor):
        for col in range(self.dim):
            self._values[row][col] = self._values[row][col] * factor
        self._factor = self._factor/factor #Fraction(self._factor,factor)#
        self.report(f'rij {row+1} vermenigvuldigd met {factor}')
    def mul_col(self, col, factor):
        for row in range(self.dim):
            self._values[row][col] = self._values[row][col] * factor
        self._factor = self._factor/factor #Fraction(self._factor,factor)#
        self.report(f'kolom {col+1} vermenigvuldigd met {factor}')
    def simplify_determinant(self)->Determinant:
        if self.dim > 2 and self._simplify_determinant():
            print('VEREENVOUDIGING:')
            return self.sub_determinant(0,0,self.values[0][0]).simplify_determinant()
        else:
            if is_zero(self._values[1][0]):
                self.mul_col(0,self._factor)
            else:
                self.mul_row(0,self._factor)
            return self
    def _simplify_determinant(self, target:int = 0, is_row = True)->bool:
        if is_row:
            return self._simplify_row(target)
        else:
            return self._simplify_col(target)
    def _simplify_row(self, target_row: int)->bool:
        c = 0
        while c < self.dim and round(self.values[target_row][c],PRECISION) == 0:
            c+=1
        if c >= self.dim:
            return False
        factor = 1/self.values[target_row][c]
        self.mul_row(target_row, factor)
        for c2 in range(c+1,self.dim):
            self.add_col(c, -self.values[target_row][c2], c2)
        self.mul_row(target_row, self._factor)
        return True
    def _simplify_col(self, target_col: int)->bool:
        r = 0
        while r < self.dim and round(self.values[r][target_col],PRECISION) == 0:
            r+=1
        if r >= self.dim:
            return False
        factor = 1/self.values[r][target_col]
        self.mul_col(target_col, factor)
        for r2 in range(r+1,self.dim):
            self.add_row(r, -self.values[r2][target_col], r2)
        self.mul_col(target_col,1/factor)
        return True
    def sub_determinant(self, matrix_row, matrix_col, factor = 1):
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
        result = Determinant(rows, factor * self._factor)
        result.report(f'subdeterminant vanuit {matrix_row+1},{matrix_col+1}')
        return result

def simplify_determinant(D: Determinant):
    D.print_det('initial')
    DE = D.simplify_determinant()
    DE.print_det('simpled')

# simplify_determinant(Determinant([[-8,-5,4,5],[4,2,-2,-6],[-3,7,2,-3],[-2,-4,1,3]]))
simplify_determinant(Determinant([[3,7,-1],[4,2,0],[0,1,-2]]))


