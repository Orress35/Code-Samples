def catalan(n):
    if n <= 0:
        return 1

    catalan = [0] * (n+1)
    catalan[0] = catalan[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]

    return catalan[n]
 
# driver code
for k in range(25):
    print(catalan(k))