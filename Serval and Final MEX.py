# This is the Question


# You are given an array 𝑎 consisting of 𝑛≥4 non-negative integers.

# You need to perform the following operation on 𝑎
#  until its length becomes 1:

# Select two indices 𝑙
#  and 𝑟
#  (1≤𝑙<𝑟≤|𝑎|
# ), and replace the subarray [𝑎𝑙,𝑎𝑙+1,…,𝑎𝑟]
#  with a single integer mex([𝑎𝑙,𝑎𝑙+1,…,𝑎𝑟])
# , where mex(𝑏)
#  denotes the minimum excluded (MEX)∗
#  of the integers in 𝑏
# . In other words, let 𝑥=mex([𝑎𝑙,𝑎𝑙+1,…,𝑎𝑟])
# , the array 𝑎
#  will become [𝑎1,𝑎2,…,𝑎𝑙−1,𝑥,𝑎𝑟+1,𝑎𝑟+2,…,𝑎|𝑎|]
# . Note that the length of 𝑎
#  decreases by (𝑟−𝑙)
#  after this operation.
# Serval wants the final element in 𝑎
#  to be 0
# . Help him!

# More formally, you have to find a sequence of operations, such that after performing these operations in order, the length of 𝑎
#  becomes 1
# , and the final element in 𝑎
#  is 0
# .

# It can be shown that at least one valid operation sequence exists under the constraints of the problem, and the length of any valid operation sequence does not exceed 𝑛
# .

# Note that you do not need to minimize the number of operations.

# ∗
# The minimum excluded (MEX) of a collection of integers 𝑏1,𝑏2,…,𝑏𝑘
#  is defined as the smallest non-negative integer 𝑥
#  which does not occur in the collection 𝑏
# .

# Input
# Each test contains multiple test cases. The first line contains the number of test cases 𝑡
#  (1≤𝑡≤1000
# ). The description of the test cases follows.

# The first line of each test case contains a single integer 𝑛
#  (4≤𝑛≤5000
# ) — the length of the array 𝑎
# .

# The second line contains 𝑛
#  integers 𝑎1,𝑎2,…,𝑎𝑛
#  (0≤𝑎𝑖≤𝑛
# ) — the elements of the array 𝑎
# .

# It is guaranteed that the sum of 𝑛
#  over all test cases does not exceed 5000
# .

# Output
# For each test case, output a single integer 𝑘
#  (0≤𝑘≤𝑛
# ) in the first line of output — the length of the operation sequence.

# Then, output 𝑘
#  lines, the 𝑖
# -th line containing two integers 𝑙𝑖
#  and 𝑟𝑖
#  (1≤𝑙𝑖<𝑟𝑖≤|𝑎|
# ) — the two indices you choose in the 𝑖
# -th operation, where |𝑎|
#  denotes the length of the array before this operation.

# If there are multiple answers, you may print any of them.

# Example
# InputCopy
# 6
# 4
# 1 2 3 4
# 5
# 0 1 0 0 1
# 6
# 0 0 0 0 0 0
# 6
# 5 4 3 2 1 0
# 4
# 0 0 1 1
# 4
# 1 0 0 0
# OutputCopy
# 1
# 1 4
# 4
# 1 2
# 1 2
# 1 2
# 1 2
# 4
# 5 6
# 3 4
# 1 2
# 1 3
# 3
# 4 5
# 4 5
# 1 4
# 2
# 1 2
# 1 3
# 2
# 2 4
# 1 2
# Note
# In the first test case, since mex([1,2,3,4])=0
# , after the only operation, the array becomes [0]
# .

# In the second test case, the array 𝑎
#  changes as follows:
# [0,1⎯⎯⎯⎯⎯⎯,0,0,1]→[2,0⎯⎯⎯⎯⎯⎯,0,1]→[1,0⎯⎯⎯⎯⎯⎯,1]→[2,1⎯⎯⎯⎯⎯⎯]→[0].

# In the third test case, the array 𝑎
#  changes as follows:
# [0,0,0,0,0,0⎯⎯⎯⎯⎯⎯]→[0,0,0,0⎯⎯⎯⎯⎯⎯,1]→[0,0⎯⎯⎯⎯⎯⎯,1,1]→[1,1,1⎯⎯⎯⎯⎯⎯⎯⎯⎯]→[0].

# This is the code


for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=set()
    a=-1
    for i in range(n):
        if l[i]==0:
            s.add(i)
        else:
            a=i
    if s==set():
        print(1)
        print(1,n)
        continue
    if n-1 not in s:
        print(2)
        print(1,n-1)
        print(1,2)
        continue
    if 0 not in s:
        print(2)
        print(2,n)
        print(1,2)
        continue
    if len(s)==n:
        print(3)
        print(1,(n+1)//2)
        print((n+1)//2+2-(n+1)//2,n-(n+1)//2+1)
        print(1,2)
        continue
    # if len(a)==1:
    if 1 not in s:
        print(3)
        print(3,n)
        print(1,2)
        print(1,2)
        continue
    if n-2 not in s:
        print(3)
        print(1,n-2)
        print(2,3)
        print(1,2)
        continue
    # if len(a)==1:
    print(3)
    print(1,a+1)
    print(2,n-a)
    print(1,2)
    # print()
    # print()
    # print(s)
