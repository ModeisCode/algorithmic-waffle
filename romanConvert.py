class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        f = {'I':0, 'V':0, 'X':0, 'L':0, 'C':0, 'D':0, 'M':0}
        total = 0
        s += '$'
        r = len(s)
        for i in range(r):
            c = s[i]
            if c == '$':
                break
            a = s[i+1]
            if c == 'I' and (a in ('V','X')):
                f[c] += 1
                f[c] = f[c] * (-1)
                #f[a] += 1
                total += m[c] * f[c] 
                print("add:",m[c] * f[c])
                f[c] = 0
            elif c == 'I' and (a == 'I' or a not in ('V','X')):
                f[c] += 1
            elif c == 'X' and (a == 'X' or a not in ('L','C')):
                f[c] += 1
            elif c == 'C' and (a == 'C' or a not in ('D','M')):
                f[c] += 1
            elif c in ('V','L','D','M'):
                f[c] += 1
            elif c == 'X' and (a in ('L','C')):
                f[c] += 1
                f[c] = f[c] * (-1)
                #f[a] += 1
                total += m[c] * f[c]
                print("add:",m[c] * f[c])
                f[c] = 0
            elif c == 'C' and (a in ('D','M')):
                f[c] += 1
                f[c] = f[c] * (-1)
                #f[a] += 1
                total += m[c] * f[c]
                print("add:",m[c] * f[c])
                f[c] = 0

        print(f)
        for key,value in f.items():
            total += value * m[key]

        return total


s = Solution()
print(s.romanToInt("MCMXCIV"))
