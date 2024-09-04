class Matrix:
    def __init__(self: 'Matrix', dim: tuple[int], vals: list[list[int]] = None) -> 'Matrix':
        self.dim = dim
        if (vals == None):
            self.array = [[0 for i in range(dim[1])] for j in range(dim[0])]
        else:
            if (len(vals) != dim[0]):
                raise Exception("Invalid number of rows")
            if (len(vals[0]) != dim[1]):
                raise Exception("Invalid number of columns")
            for i in range(dim[0]):
                for j in range(dim[1]):
                    self.array = vals

    def __str__(self: 'Matrix') -> str:
        s = '\n'
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                s += str(self.array[i][j]) + ' '
            s += '\n'
        return s
    
    def __add__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        if (self.dim != other.dim):
            raise Exception("Matrices must have the same dimensions")
        res = Matrix(self.dim)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res.array[i][j] = self.array[i][j] + other.array[i][j]
        return res

    def __sub__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        if (self.dim != other.dim):
            raise Exception("Matrices must have the same dimensions")
        res = Matrix(self.dim)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res.array[i][j] = self.array[i][j] - other.array[i][j]
        return res
    
    def __mul__(self: 'Matrix', other: 'Matrix') -> 'Matrix':
        if (self.dim[1] != other.dim[0]):
            raise Exception("Invalid matrix dimensions")
        res = Matrix((self.dim[0], other.dim[1]))
        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                for k in range(self.dim[1]):
                    res.array[i][j] += self.array[i][k] * other.array[k][j]
        return res
    
    def __mul__(self: 'Matrix', a: 'int') -> 'Matrix':
        res = Matrix(self.dim, self.array)

        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res.array[i][j] *= a

        return res

    def rref(self: 'Matrix') -> 'Matrix':
        res = Matrix(self.dim, self.array)

        const = res.array[0][0]
        for j in range(self.dim[1]):
            if const == 0: break
            res.array[0][j] = res.array[0][j] / const

        for i in range(1,self.dim[0]):
            for j in range(i):
                const = res.array[i][j]
                for k in range(self.dim[1]):
                    res.array[i][k] = res.array[i][k] - res.array[j][k] * const
            
            const = res.array[i][i]
            if const == 0: continue
            for j in range(i, self.dim[0]):
                res.array[i][j] = res.array[i][j] / const
        
        return res

def main() -> None:
    m = Matrix((3,3), [[1,2,3],[4,5,6],[7,8,9]])
    print(m.rref())

if __name__ == "__main__":
    main()