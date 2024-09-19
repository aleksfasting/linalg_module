class MatrixValidator:
    def validateConstructor(dim: tuple[int], vals: list[list[int]] = None) -> None:
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
