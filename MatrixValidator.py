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