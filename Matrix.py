

class Matrix:
    array = []
    
    def __init__(self, dim: (int,int), vals = None):
        if (vals == None):
            for i in range(dim):
                self.array.append(0)
        else:
            for i in range(dim[0]):
                for j in range(dim[1]):
                    self.array.append(vals[i][j])