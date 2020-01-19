'''
The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2. (Please note that the palindromic number,
in either base, may not include leading zeros.)

ans = 872187
'''
ans = 0
for i in range(1,1000000):
    s = str(i)
    s1 = s[::-1]
    if s == s1:
        bs = str(bin(i))[2:]
        bs1 = bs[::-1]
        if bs1 == bs:
            ans = ans + i
print(ans)
        





