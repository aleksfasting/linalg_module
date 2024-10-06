from MatrixValidator import MatrixValidator

class Matrix:
    def __init__(self: 'Matrix', dim: tuple[int], vals: list[list[int]] = None) -> 'Matrix':
        self.dim = dim
        MatrixValidator.validateConstructor(dim, vals)
        if (vals == None):
            self.array = [0 for i in range(dim[0] * dim[1])]
        elif (type(vals[0]) != int and type(vals[0]) != float):
            self.array = []
            for i in range(dim[0]):
                self.array += [vals[i][j] for j in range(dim[1])]
        else:
            self.array = vals

    def __getitem__(self, coord: tuple['int']) -> 'float':
        if (type(coord) == int):
            if (self.dim[0] == 1):
                coord = (0, coord)
            elif (self.dim[1] == 1):
                coord = (coord, 0)
        i = coord[0]
        j = coord[1]
        if (type(i) == str):
            if (type(j) == str):
                return Matrix(self.dim, self.array)
            return Matrix((self.dim[0],1), self.array[j::self.dim[1]])
        if (type(j) == str):
            return Matrix((1, self.dim[1]), self.array[self.dim[0]*i:self.dim[0]*(i+1)])
        return self.array[i*self.dim[1] + j]
    
    def __setitem__(self, coord: tuple[int], a: 'Matrix') -> None:
        if (type(a) != Matrix):
            raise Exception("Needs matrix input")
        MatrixValidator.validateSetItem(self.dim, coord, a)
        i = coord[0]
        j = coord[1]

        if (type(i) == str):
            if (a.dim == self.dim and type(j) == str):
                self.array = a.array
            for k in range(self.dim[0]):
                self.array[j + self.dim[1] * k] = a[k,0]
            return
        
        if (type(j) == str):
            for k in range(self.dim[0]):
                self.array[i * self.dim[0] + k] = a[0,k]
            return

        self.array[i*self.dim[0] + j] = a

    def __str__(self: 'Matrix') -> str:
        s = '\n'
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                s += str(self[i,j]) + ' '
            s += '\n'
        return s
    
    def __add__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        MatrixValidator.validateAdd(self.dim, other.dim)
        res = Matrix(self.dim)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res[i,j] = self[i,j] + other[i,j]
        return res

    def __sub__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        MatrixValidator.validateAdd(self.dim, other.dim)
        res = Matrix(self.dim)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res[i,j] = self[i,j] - other[i,j]
        return res
    
    def __mul__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        if (type(other) != Matrix):
            res = Matrix(self.dim, self.array)
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    res[i,j] *= other
            return res

        MatrixValidator.validateMul(self.dim, other.dim)
        res = Matrix((self.dim[0], other.dim[1]))

        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                for k in range(self.dim[1]):
                    res[i,j] += self[i,k] * other[k,j]
        return res

    def rref(self: 'Matrix') -> 'Matrix':
        res = Matrix(self.dim, self.array)

        const = res[0,0]
        if const != 0:
            for j in range(self.dim[1]):
                res[0,j] = res[0,j] / const

        for i in range(1,self.dim[0]):
            for j in range(i):
                const = res[i,j]
                for k in range(self.dim[1]):
                    res[i,k] = res[i,k] - res[j,k] * const
            
            const = res[i,i]
            if const == 0: continue
            for j in range(i, self.dim[0]):
                res[i,j] = res[i,j] / const
        
        return res
    
    def invert(self) -> 'Matrix':
        res = Matrix((self.dim[1], self.dim[1]))

        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res[j,i] = self[i,j]

        return res
    
    def extendMatrixByColumnVector(self: 'Matrix', vec: 'Matrix') -> 'Matrix':
        if (vec.dim[1] != 1):
            raise Exception("Not a column vector")
        if (vec.dim[0] != self.dim[0]):
            raise Exception("vector and matrix not in same vector space")
        res = Matrix((self.dim[0], self.dim[1] + 1))

        res_array = self.array.copy()
        for i in range(self.dim[0]):
            res_array.insert((i+1)*self.dim[1]+i, vec[i])
        
        res.array = res_array
        return res
    
    def extendMatrixByRowVector(self: 'Matrix', vec: 'Matrix') -> 'Matrix':
        if (vec.dim[0] != 1):
            raise Exception("Not a column vector")
        if (vec.dim[1] != self.dim[1]):
            raise Exception("vector and matrix not in same vector space")
        res = Matrix((self.dim[0] + 1, self.dim[1]))

        res_array = self.array.copy()
        for i in range(self.dim[1]):
            res_array.append(vec[i])
        
        res.array = res_array
        return res

    def extendMatrixRows(self: 'Matrix', extendBy: 'Matrix') -> 'Matrix':
        if (extendBy.dim[0] != self.dim[0]):
            raise Exception("matrices not in same vector space")
        
        res = Matrix(self.dim, self.array.copy())
        for i in range(extendBy.dim[1]):
            res = res.extendMatrixByColumnVector(extendBy['i', i])

        return res

    def extendMatrixCols(self: 'Matrix', extendBy: 'Matrix') -> 'Matrix':
        if (extendBy.dim[1] != self.dim[1]):
            raise Exception("matrices not in same vector space")
        
        res = Matrix(self.dim, self.array.copy())
        for i in range(extendBy.dim[0]):
            res = res.extendMatrixByRowVector(extendBy[i, 'j'])

        return res


def main() -> None:
    m = Matrix((3,3), [[1,2,3],[4,5,6],[7,8,9]])
    print(m)
    print(m.extendMatrixByColumnVector(Matrix((3,1), [[1],[2],[3]])))
    print(m.extendMatrixRows(Matrix((3,2), [[1,2],[3,4],[5,6]])))
    print(m)

if __name__ == "__main__":
    main()