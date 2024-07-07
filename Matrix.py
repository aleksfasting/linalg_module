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

def main() -> None:
    m = Matrix((3,3), [[1,2,3],[4,5,6],[7,8,9]])
    n = Matrix((3,2), [[9,7],[6,4],[3,1]])
    o = m*n
    print(o)

if __name__ == "__main__":
    main()