# Regular Contest 097 Equals

N, M = (int(i) for i in input().split())
p = list(map(int, input().split()))
x_y = [list(map(int, input().split())) for i in range(M)]


def check(lst):
    count = 0
    for i in range(len(lst)):
        if i+1 == lst[i]:
            count+=1
    return count


"""
def check1(lst):
    count = 0
    count = [count + 1 for i in range(len(lst)) if i+1 == lst[i]]
    return count
"""

def swap(lst, mat, row):
    index1 = lst.index(mat[row][0])
    index2 = lst.index(mat[row][1])
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

num_lst = []
def loop(p, x_y):
    for i in range(M):
        if check(p) < check(swap(p,x_y,i)):
            return loop(swap(p,x_y, i), x_y)
        elif i == M-1:
            num_lst.append(check(p))
loop(p, x_y)
print(num_lst)
