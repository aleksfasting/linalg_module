class Matrix:
    def __init__(self: 'Matrix', dim: tuple[int], vals: list[list[int]] = None) -> 'Matrix':
        self.dim = dim
        if (vals == None):
            self.array = [0 for i in range(dim[0] * dim[1])]
        elif (type(vals[0]) != int and type(vals[0]) != float):
            if (len(vals) != dim[0]):
                raise Exception("Invalid number of rows")
            if (len(vals[0]) != dim[1]):
                raise Exception("Invalid number of columns")
            self.array = []
            for i in range(dim[0]):
                self.array += [vals[i][j] for j in range(dim[1])]
        else:
            if (len(vals) != dim[0] * dim[1]):
                raise Exception("Dimension not fitting to vals")
            self.array = vals

    def __getitem__(self, coord: tuple['int']) -> 'float':
        if (type(coord) == int):
            if (self.dim[0] == 1):
                coord = (0, coord)
            elif (self.dim[1] == 1):
                coord = (coord, 0)
        elif (len(coord) != 2):
            raise Exception("Invalid tuple")
        i = coord[0]
        j = coord[1]
        if (type(i) == str):
            if (type(j) == str):
                return Matrix(self.dim, self.array)
            return Matrix((self.dim[0],1), self.array[j::self.dim[1]])
        if (type(j) == str):
            return Matrix((1, self.dim[1]), self.array[self.dim[0]*i:self.dim[0]*(i+1)])
        if (i >= self.dim[0]):
            raise Exception("Index i larger than dimension")
        if (j >= self.dim[1]):
            raise Exception("Index j larger than dimension")
        return self.array[i*self.dim[1] + j]
    
    def __setitem__(self, coord: tuple[int], a: 'Matrix') -> None:
        if (len(coord) != 2):
            raise Exception("Invalid tuple")
        i = coord[0]
        j = coord[1]

        if (type(i) == str):
            if (type(a) != Matrix):
                raise Exception("needs matrix input")
            if (a.dim == self.dim and type(j) == str):
                self.array = a.array
            if (type(j) == str):
                raise Exception("Dimension of matrix is wrong")
            if (a.dim != (self.dim[0], 1)):
                raise Exception("Dimension of matrix is wrong")
            for k in range(self.dim[0]):
                self.array[j + self.dim[1] * k] = a[k,0]
            return
        
        if (type(j) == str):
            if (type(a) != Matrix):
                raise Exception("Needs matrix input")
            if (a.dim != (1, self.dim[1])):
                raise Exception("Dimension of mtrix is wrong")
            for k in range(self.dim[0]):
                self.array[i * self.dim[0] + k] = a[0,k]
            return


        if (i >= self.dim[0]):
            raise Exception("Index i larger than dimension")
        if (j >= self.dim[1]):
            raise Exception("Index j larger than dimension")
        self.array[i*self.dim[0] + j] = a

    def __str__(self: 'Matrix') -> str:
        s = '\n'
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                s += str(self[i,j]) + ' '
            s += '\n'
        return s
    
    def __add__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        if (self.dim != other.dim):
            raise Exception("Matrices must have the same dimensions")
        res = Matrix(self.dim)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res[i,j] = self[i,j] + other[i,j]
        return res

    def __sub__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        if (self.dim != other.dim):
            raise Exception("Matrices must have the same dimensions")
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

        if (self.dim[1] != other.dim[0]):
            raise Exception("Invalid matrix dimensions")
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


def main() -> None:
    m = Matrix((3,3), [[1,2,3],[4,5,6],[7,8,9]])
    print(m)
    print(m.extendMatrixByColumnVector(Matrix((3,1), [0,0,0])))
    print(m)
    print(m.extendMatrixByRowVector(Matrix((1,3), [0,0,0])))

if __name__ == "__main__":
    main()