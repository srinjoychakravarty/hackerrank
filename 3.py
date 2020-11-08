def countPerms(n):

    h, w = (n + 1), 5
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    
    i = 0
    while (i < 5):
        Matrix[1][i] = 1
        i = (i + 1)
    
    j = 2
    while (j <= n):
        Matrix[j][0] = Matrix[j - 1][1] + Matrix[j - 1][2] + Matrix[j - 1][4]
        Matrix[j][1] = Matrix[j - 1][0] + Matrix[j - 1][2]
        Matrix[j][2] = Matrix[j - 1][1] + Matrix[j - 1][3]
        Matrix[j][3] = Matrix[j - 1][2]
        Matrix[j][4] = Matrix[j - 1][2] + Matrix[j - 1][3]
        
        k = 0
        while (k < 5):
            Matrix[j][k] = (Matrix[j][k] % 1000000007)
            k = (k + 1)

        j = (j + 1)

    res = 0
    
    l = 0
    while (l < 5):
        res = res + Matrix[n][l]
        res = (res % 1000000007)

    return(res)

if __name__ == '__main__':

    countPerms(1)