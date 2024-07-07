class Matrix:
    def __init__(self, dim: (int,int), vals = None):
        self.dim = dim
        if (vals == None):
            for i in range(dim):
                self.array.append(0)
        else:
            for i in range(dim[0]):
                for j in range(dim[1]):
                    self.array.append(vals[i][j])

    def __str__(self):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                print(self.array[i][j], end = " ")
            print()