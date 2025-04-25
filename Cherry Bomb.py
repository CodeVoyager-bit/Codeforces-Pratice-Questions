# This is the question  


# Two integer arrays 𝑎
#  and 𝑏
#  of size 𝑛
#  are complementary if there exists an integer 𝑥
#  such that 𝑎𝑖+𝑏𝑖=𝑥
#  over all 1≤𝑖≤𝑛
# . For example, the arrays 𝑎=[2,1,4]
#  and 𝑏=[3,4,1]
#  are complementary, since 𝑎𝑖+𝑏𝑖=5
#  over all 1≤𝑖≤3
# . However, the arrays 𝑎=[1,3]
#  and 𝑏=[2,1]
#  are not complementary.

# Cow the Nerd thinks everybody is interested in math, so he gave Cherry Bomb two integer arrays 𝑎
#  and 𝑏
# . It is known that 𝑎
#  and 𝑏
#  both contain 𝑛
#  non-negative integers not greater than 𝑘
# .

# Unfortunately, Cherry Bomb has lost some elements in 𝑏
# . Lost elements in 𝑏
#  are denoted with −1
# . Help Cherry Bomb count the number of possible arrays 𝑏
#  such that:

# 𝑎
#  and 𝑏
#  are complementary.
# All lost elements are replaced with non-negative integers no more than 𝑘
# .
# Input
# The first line of the input contains a single integer 𝑡
#  (1≤𝑡≤104
# ) — the number of test cases.

# The first line of each test case contains two integers 𝑛
#  and 𝑘
#  (1≤𝑛≤2⋅105
# , 0≤𝑘≤109
# ) — the size of the arrays and the maximum possible value of their elements.

# The second line contains 𝑛
#  integers 𝑎1,𝑎2,...,𝑎𝑛
#  (0≤𝑎𝑖≤𝑘
# ).

# The third line contains 𝑛
#  integers 𝑏1,𝑏2,...,𝑏𝑛
#  (−1≤𝑏𝑖≤𝑘
# ). If 𝑏𝑖=−1
# , then this element is missing.

# It is guaranteed that the sum of 𝑛
#  over all test cases does not exceed 2⋅105
# .

# Output
# Output exactly one integer, the number of ways Cherry Bomb can fill in the missing elements from 𝑏
#  such that 𝑎
#  and 𝑏
#  are complementary.

# Example
# InputCopy
# 7
# 3 10
# 1 3 2
# -1 -1 1
# 5 1
# 0 1 0 0 1
# -1 0 1 0 -1
# 5 1
# 0 1 0 0 1
# -1 1 -1 1 -1
# 5 10
# 1 3 2 5 4
# -1 -1 -1 -1 -1
# 5 4
# 1 3 2 1 3
# 1 -1 -1 1 -1
# 5 4
# 1 3 2 1 3
# 2 -1 -1 2 0
# 5 5
# 5 0 5 4 3
# 5 -1 -1 -1 -1
# OutputCopy
# 1
# 0
# 0
# 7
# 0
# 1
# 0
# Note
# In the first example, the only way to fill in the missing elements in 𝑏
#  such that 𝑎
#  and 𝑏
#  are complementary is if 𝑏=[2,0,1]
# .

# In the second example, there is no way to fill in the missing elements of 𝑏
#  such that 𝑎
#  and 𝑏
#  are complementary.

# In the fourth example, some 𝑏
#  arrays that are complementary to 𝑎
#  are: [4,2,3,0,1],[7,5,6,3,4],
#  and [9,7,8,5,6]
# .

# this is the code

for  i in range(int(input())):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    count1=0
    a=-1
    ans=False
    for i in range(n):
        if l2[i]==-1:
            count1+=1
        else:
            if a==-1:
                a=l1[i]+l2[i]
            else:
                if l1[i]+l2[i]!=a:
                    ans=True
                    break
    if ans:
        print(0)
    elif count1!=n:
        if a>min(l1)+m or a<max(l1):
            print(0)
        else:
            print(1)
    else:
        print(m+min(l1)-max(l1)+1)
