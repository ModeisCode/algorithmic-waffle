
def binomialCoefficientDP(n_:int,k_:int) -> list[list]:
    C = [[-1 for j in range(n_)] for i in range(k_)]
    for n in range(n_):
        
        for k in range(k_):
            if k == 0 or n == k:
                C[n][k] = 1
            elif n > 0 and k > 0:
                C[n][k] = C[n-1][k-1] + C[n-1][k]
    return C

C = binomialCoefficientDP(7,7)
