class MatrixValidator:
    def validateConstructor(dim: 'tuple[int]', vals: 'list[list[int]]' = None) -> 'None':
        if (vals == None):
            return
        elif (type(vals[0]) != int and type(vals[0]) != float):
            if (len(vals) != dim[0]):
                raise Exception("Invalid number of rows")
            if (len(vals[0]) != dim[1]):
                raise Exception("Invalid number of columns")
        else:
            if (len(vals) != dim[0] * dim[1]):
                raise Exception("Dimension not fitting to vals")

    def validateGetItem(dim: 'tuple[int]', coord: 'tuple[int]'):
        if (type(coord) == int):
            if (dim[0] == 1):
                coord = (0, coord)
            elif (dim[1] == 1):
                coord = (coord, 0)
            else:
                raise Exception("Can't reference element with 1 index")
        elif (len(coord) != 2):
            raise Exception("Invalid tuple")
        i = coord[0]
        j = coord[1]
        if (type(i) != str and (i >= self.dim[0] or j < 0)):
            raise Exception("Index i larger than dimension")
        if (type(j) != str and (j >= self.dim[1] or j < 0)):
            raise Exception("Index j larger than dimension")
        
    def validateSetItem(dim: tuple[int], coord: tuple[int], a):
        if (len(coord) != 2):
            raise Exception("Invalid tuple")
        
        i = coord[0]
        j = coord[1]

        if (type(i) == str):
            if (type(j) == str):
                raise Exception("Dimension of matrix is wrong")
            if (a.dim != (dim[0], 1)):
                raise Exception("Dimension of matrix is wrong")
            
        if (type(j) == str):
            if (a.dim != (1, self.dim[1])):
                raise Exception("Dimension of mtrix is wrong")
            return
        
        if (i >= self.dim[0]):
            raise Exception("Index i larger than dimension")
        if (j >= self.dim[1]):
            raise Exception("Index j larger than dimension")
        
    def validateAdd(dim0, dim1):
        if (dim0 != dim1):
            raise Exception("Matrices must have the same dimensions")
        
    def validateMul(dim0, dim1):
        if (dim0[1] != dim1[0]):
            raise Exception("Invalid matrix dimensions")
        
    def validateExtendByColumnVector(dim0, dim1):
        if (dim1[1] != 1):
            raise Exception("Not a column vector")
        if (dim1[0] != dim0[0]):
            raise Exception("vector and matrix not in same vector space")