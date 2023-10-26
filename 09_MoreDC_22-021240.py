def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

def mult(A, B):
    product = []
    if len(A[0]) == len(B):
        for i in range(len(A)):
            temp = []
            for k in range(len(B[0])):
                sum = 0
                for j in range(len(A[0])):
                    sum += A[i][j] * B[j][k]
                temp.append(sum)
            product.append(temp)

        return product
    return -1

exec(input().strip())
