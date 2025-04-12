# This is the question

# Luke likes to eat. There are 𝑛
#  piles of food aligned in a straight line in front of him. The 𝑖
# -th pile contains 𝑎𝑖
#  units of food.

# Luke will walk from the 1
# -st pile towards the 𝑛
# -th pile, and he wants to eat every pile of food without walking back. When Luke reaches the 𝑖
# -th pile, he can eat that pile if and only if |𝑣−𝑎𝑖|≤𝑥
# , where 𝑥
#  is a fixed integer, and 𝑣
#  is Luke's food affinity.

# Before Luke starts to walk, he can set 𝑣
#  to any integer. Also, for each 𝑖
#  (1≤𝑖≤𝑛
# ), Luke can change his food affinity to any integer before he eats the 𝑖
# -th pile.

# Find the minimum number of changes needed to eat every pile of food.

# Note that the initial choice for 𝑣
#  is not considered as a change.

# Input
# The input consists of multiple test cases. The first line contains a single integer 𝑡
#  (1≤𝑡≤104
# ) — the number of test cases. The description of test cases follows.

# For each test case, the first line contains two integers, 𝑛,𝑥
#  (1≤𝑛≤2⋅105
# , 1≤𝑥≤109
# ) — the number of piles, and the maximum difference between the size of a pile and Luke's food affinity, such that Luke can eat the pile.

# The second line contains 𝑛
#  integers 𝑎1,𝑎2,…,𝑎𝑛
#  (1≤𝑎𝑖≤109
# ).

# It is guaranteed that the sum of 𝑛
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output an integer on a separate line, which is the minimum number of changes needed.

# Example
# InputCopy
# 7
# 5 3
# 3 8 5 6 7
# 5 3
# 3 10 9 8 7
# 12 8
# 25 3 3 17 8 6 1 16 15 25 17 23
# 10 2
# 1 2 3 4 5 6 7 8 9 10
# 8 2
# 2 4 6 8 6 4 12 14
# 8 2
# 2 7 8 9 6 13 21 28
# 15 5
# 11 4 13 23 7 10 5 21 20 11 17 5 29 16 11
# OutputCopy
# 0
# 1
# 2
# 1
# 2
# 4
# 6
# Note
# In the first test case, Luke can set 𝑣
#  to 5
#  before he starts to walk. And he can walk straight to eat every piles of food without changing 𝑣
# .

# In the second test case, Luke can set 𝑣
#  to 3
#  before he starts to walk. And he could change 𝑣
#  to 10
#  before he eats the second pile. After that, he can walk straight to eat remaining food without changing 𝑣
# .

# In the fourth test case, Luke can set 𝑣
#  to 3
#  before he starts to walk. And he could change 𝑣
#  to 8
#  before he eats the sixth pile. After that, he can walk straight to eat remaining food without changing 𝑣
# .

# In the fifth test case, Luke can set 𝑣
#  to 4
#  before he starts to walk. And he could change 𝑣
#  to 6
#  before he eats the fourth pile. Then he could change 𝑣
#  to 12
#  before he eats the seventh pile. After that, he can walk straight to eat remaining food without changing 𝑣
# .

# This is the code

for i in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    lower,higher=l[0]-m,l[0]+m
    count=0
    for i in range(1,n):
        if lower<=l[i]-m<=higher or lower<=l[i]+m<=higher or l[i]-m<=lower<=l[i]+m or l[i]-m<=higher<=l[i]+m:
            lower=max(lower,l[i]-m)
            higher=min(higher,l[i]+m)
        else:
            # print(lower,higher)
            # print(l[i],i)
            count+=1
            lower,higher=l[i]-m,l[i]+m
    print(count)

