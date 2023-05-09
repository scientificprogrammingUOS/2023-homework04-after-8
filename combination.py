import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1: np.array, array2: np.array, axis = 0):
    a1 = np.squeeze(array1)
    a2 = np.squeeze(array2)
    try:
        return np.concatenate((a1, a2), axis = axis)
    except ValueError:
        raise ValueError("The arrays cannot be combined because they have different shapes or different datatypes")

if __name__ == "__main__":
    a1 = np.array([1,2,3])
    a2 = np.array([1,2,3])
    print(combination(a1, a2))
