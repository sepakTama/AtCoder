# Beginner Contest 097 Exponential
from math import sqrt, floor

X = int(input())
root_int = int(floor(sqrt(X)))

list = []

# ある値bに対してaのべき乗の最大のaを求める
def exp(b, a, i):
    if b > a**i:
        return exp(b,a,i+1)
    elif b == a**i:
        return b
    else:
        return a**(i-1)


#list.append([exp(X, k, 0)for k in range(2, root_int+1)])
for k in range(2, root_int+1):
    list.append(exp(X,k,0))
print(max(list))
