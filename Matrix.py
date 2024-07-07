class Matrix:
    def __init__(self, dim: (int,int), vals = None):
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

    def __str__(self):
        s = '\n'
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                s += str(self.array[i][j]) + ' '
            s += '\n'
        return s

def main():
    m = Matrix((3,3), [[1,2,3],[4,5,6],[7,8,9]])
    print(m)

if __name__ == "__main__":
    main()