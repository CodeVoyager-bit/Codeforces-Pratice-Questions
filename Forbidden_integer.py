# This is the question

# You are given an integer 𝑛
# , which you want to obtain. You have an unlimited supply of every integer from 1
#  to 𝑘
# , except integer 𝑥
#  (there are no integer 𝑥
#  at all).

# You are allowed to take an arbitrary amount of each of these integers (possibly, zero). Can you make the sum of taken integers equal to 𝑛
# ?

# If there are multiple answers, print any of them.

# Input
# The first line contains a single integer 𝑡
#  (1≤𝑡≤100
# ) — the number of testcases.

# The only line of each testcase contains three integers 𝑛,𝑘
#  and 𝑥
#  (1≤𝑥≤𝑘≤𝑛≤100
# ).

# Output
# For each test case, in the first line, print "YES" or "NO" — whether you can take an arbitrary amount of each integer from 1
#  to 𝑘
# , except integer 𝑥
# , so that their sum is equal to 𝑛
# .

# If you can, the second line should contain a single integer 𝑚
#  — the total amount of taken integers. The third line should contain 𝑚
#  integers — each of them from 1
#  to 𝑘
# , not equal to 𝑥
# , and their sum is 𝑛
# .

# If there are multiple answers, print any of them.


# Input
# 5
# 10 3 2
# 5 2 1
# 4 2 1
# 7 7 3
# 6 1 1

# Output
# YES
# 6
# 3 1 1 1 1 3
# NO
# YES
# 2
# 2 2
# YES
# 1
# 7
# NO


for i in range(int(input())):
    n,m,x=map(int,input().split())
    if x==1:
        if m==1:
            print('NO')
            
        elif n%2==0:
            print('YES')
            print(n//2)
            print('2 '*(n//2))
        elif m>2:
            print('YES')
            print(n//2)
            print('2 '*(n//2 -1)+'3')
        else:
            print('NO')
    else:
        print('YES')
        print(n)
        print('1 '*n)
