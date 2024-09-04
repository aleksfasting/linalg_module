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

    def __getitem__(self, coord: tuple[int]) -> float:
        if (len(coord) != 2):
            raise Exception("Invalid tuple")
        i = coord[0]
        j = coord[1]
        if (i >= self.dim[0]):
            raise Exception("Index i larger than dimension")
        if (j >= self.dim[1]):
            raise Exception("Index j larger than dimension")
        return self.array[i*self.dim[0] + j]
    
    def __setitem__(self, coord: tuple[int], a: int) -> None:
        if (len(coord) != 2):
            raise Exception("Invalid tuple")
        i = coord[0]
        j = coord[1]
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
        if (self.dim[1] != other.dim[0]):
            raise Exception("Invalid matrix dimensions")
        res = Matrix((self.dim[0], other.dim[1]))
        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                for k in range(self.dim[1]):
                    res[i,j] += self[i,k] * other[k,j]
        return res
    
    def __mul__(self: 'Matrix', a: 'int') -> 'Matrix':
        res = Matrix(self.dim, self.array)

        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                res[i,j] *= a

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

def main() -> None:
    m = Matrix((3,3), [[1,2,3],[4,5,6],[7,8,9]])
    print(m.rref())

if __name__ == "__main__":
    main()