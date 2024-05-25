
def longestCommonSubsequence(text1:str , text2:str):
    l1 = len(text1)
    l2 = len(text2)
    C = [[j for j in range(l2)] for i in range(l1)]

    for i in range(l1):
        for j in range(l2):
            if i == 0 or j == 0:
                C[i][j] = 0
            elif text1[i] == text2[j]:
                C[i][j] = (C[i-1][j-1] + 1)
            elif text1[i] != text2[j]:
                C[i][j] = max(C[i-1][j] , C[i][j-1])
    return C


text1 = "abcdcba"
text2 = "dcbaabc"
lcs = longestCommonSubsequence(text1 , text2)
print("LCS:" , lcs[-1])
