# input---
# 2
# 1 2

n = int(input())
integer_list = map(int, input().split())
tup = ()
for x in integer_list:
    tup+=(x,)
    
print(hash(tup))