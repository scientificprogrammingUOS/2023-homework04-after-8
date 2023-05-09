import numpy as np

# implement the function strange pattern

def strange_pattern(that_tuple = ()):
    columns = that_tuple[0] 
    rows = that_tuple[1]
    if (isinstance(columns, int) and isinstance(rows, int)):
        my_array = np.full((columns, rows), False, dtype = bool)
        for column in range(columns):
            for row in range(rows):
                if (column%3 == 0):
                    if (row%3 == 0):
                        my_array[column,row] = True
                if (column%3 == 1):
                    if (row%3 == 2):
                        my_array[column, row] = True
                if (column%3 == 2):
                    if (row%3 == 1):
                        my_array[column, row] = True
        return my_array
    else:
        return "Please enter integer values"



if __name__ == "__main__":
    print(strange_pattern((3,4)))
