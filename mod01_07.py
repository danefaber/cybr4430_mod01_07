import numpy
#  function that takes a well-formed matrix with real/complex entries as its input and outputs true if the input matrix is Hermitian and outputs false if the matrix is not Hermitian.
def isHermitian(m):
    rows = len(m)
    cols = len(m[0])

    if rows != cols:
        return False

    for i in range(rows):
        for j in range(cols):
            if m[i][j] != m[j][i].conjugate():
                return False

    return True
    
#  function takes a well-formed matrix with real/complex entries as its input and outputs true if the input matrix is unitary and outputs false if the input matrix is not unitary.
def isUnitary(m):
    rows = len(m)
    cols = len(m[0])

    if rows != cols:
        return False

    for i in range(rows):
        for j in range(rows):
            total = 0

            for k in range(cols):
                total += m[k][i].conjugate() * m[k][j]

            if i == j:
                if abs(total - 1) > 0.000001:
                    return False
            else:
                if abs(total) > 0.000001:
                    return False

    return True
