# Regular Contest 097 K-thSubstring

s = input()
K = int(input())

all_string = [];
def decom(lst):
    lst_size = len(lst)
    for i in range(lst_size):
        for j in range(i, lst_size):
            all_string.append(lst[i:j+1])
    return all_string

def check(lst):
    lst_size = len(lst)
    if lst_size == 1:
        return lst
    else:
        for i in range(lst_size - 1):
            if lst[i] == lst[i+1]:
                lst.pop(i+1)
                return check(lst)
                break
            if i == lst_size - 1:
                return lst

all_string = decom(s)
all_string.sort(key = len)
all_string.sort()
check(all_string)
ans = all_string[K-1]
print(ans)
