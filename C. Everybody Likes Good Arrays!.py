# this is the question
# An array 𝑎
#  is good if for all pairs of adjacent elements, 𝑎𝑖
#  and 𝑎𝑖+1(1≤𝑖<𝑛
# ) are of different parity. Note that an array of size 1 is trivially good.
# You are given an array of size 𝑛.
# In one operation you can select any pair of adjacent elements in which both elements are of the same parity, delete them, and insert their product in the same position.
# Find the minimum number of operations to form a good array.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases 𝑡
#  (1≤𝑡≤500). The description of the test cases follows.

# The first line of each test case contains an integer 𝑛(1≤𝑛≤100).

# The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤10^9).

# Output
# For each test case print an integer, the minimum number of operations required to form a good array.

# Example
# InputCopy
# 3
# 5
# 1 7 11 2 13
# 4
# 1 2 3 4
# 6
# 1 1 1 2 2 3
# OutputCopy
# 2
# 0
# 3
# Note
# Consider the first test case. Select the 2
# -nd and the 3
# -rd integers and apply the operation on them. The array changes from [1,7,11,2,13]
#  to [1,77,2,13]
# . Next, select the 1
# -st and the 2
# -nd integers, array changes from [1,77,2,13]
#  to [77,2,13]
# . Thus we require 2
#  operations. It can be proved that this is the minimum number of operations.

# In the second test case, the given array is already good. So we require 0
#  operations.


# this is the solution

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    if n==1:
        print(0)
        continue
    count=0
    for i in range(1,n):
        if l[i-1]%2==l[i]%2:
            count+=1
    print(count)

