# decrease and conquer approach
s1 = [2,5,5,5]
s2 = [2, 2, 3, 5, 5, 7]
s3 = []

# if len(s1) < len(s2) 
def commonArray(s1: list , s2:list , s3:list , i:int , j:int) -> list:
    
    print("S1:",s1)
    print("S2:",s2)
    print("S3:",s3)
    print("----------")

    if len(s1) == 0 or len(s2) == 0 or i == (len(s1)-1):
        return s3

    if s1[i] == s2[j]:
        s3.append(s1[i])
        del s1[i]
        del s2[j]
        return commonArray(s1,s2,s3,i,j)


    if j == (len(s2) - 1):
        j = 0
        i+=1
    else:
        j+=1

    return commonArray(s1,s2,s3,i,j)

print(commonArray(s1,s2,s3,0,0))
