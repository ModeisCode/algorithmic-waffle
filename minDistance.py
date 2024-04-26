
A = [0,5,12,28,45,38,15,49]

#divide and conquer approach

def minDistance(A:list,dmin:int) -> int:
    
    d = abs(A[0] - A[1])
    if d < dmin:
        dmin = d
    
    print(dmin)
    
def divide(A:list,dmin:int):

    if (len(A) < 2):
        return


    if (len(A) == 2):
        minDistance(A,dmin)

    
    x = (len(A) - 1) // 2
    divide(A[:x],dmin)
    divide(A[x:],dmin)

divide(A,999999)
