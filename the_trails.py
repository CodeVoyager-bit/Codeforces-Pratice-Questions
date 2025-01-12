# Solved 3rd Question of div 2 in Codeforces.../

# This is the Question

# In the wilderness lies a region of mountainous terrain represented as a rectangular grid with 𝑛
#  rows and 𝑚
#  columns. Each cell in the grid is identified by its position (𝑖,𝑗)
# , where 𝑖
#  is the row index and 𝑗
#  is the column index. The altitude of cell (𝑖,𝑗)
#  is denoted by 𝑎𝑖,𝑗
# .

# However, this region has been tampered with. A path consisting of 𝑛+𝑚−1
#  cells, starting from the top-left corner (1,1)
#  and ending at the bottom-right corner (𝑛,𝑚)
# , has been cleared. For every cell (𝑖,𝑗)
#  along this path, the altitude 𝑎𝑖,𝑗
#  has been set to 0
# . The path moves strictly via downward (𝙳
# ) or rightward (𝚁
# ) steps.

# To restore the terrain to its original state, it is known that the region possessed a magical property before it was tampered with: all rows and all columns shared the same sum of altitudes. More formally, there exists an integer 𝑥
#  such that ∑𝑚𝑗=1𝑎𝑖,𝑗=𝑥
#  for all 1≤𝑖≤𝑛
# , and ∑𝑛𝑖=1𝑎𝑖,𝑗=𝑥
#  for all 1≤𝑗≤𝑚
# .

# Your task is to assign new altitudes to the cells on the path such that the above magical property is restored. It can be proven that a solution always exists. If there are multiple solutions that satisfy the property, any one of them may be provided.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases 𝑡
#  (1≤𝑡≤104
# ). The description of the test cases follows.

# The first line of each test case contains two integers 𝑛
#  and 𝑚
#  (2≤𝑛,𝑚≤1000
# ) — the number of rows and columns in the grid.

# The second line of each test case contains a string 𝑠
#  of length 𝑛+𝑚−2
#  (𝑠𝑖=𝙳
#  or 𝑠𝑖=𝚁
# ) — the steps the path makes from (1,1)
#  to (𝑛,𝑚)
# . The character 𝙳
#  represents a downward step, and 𝚁
#  represents a rightward step.

# The 𝑖
# -th of the next 𝑛
#  lines each contain 𝑚
#  integers 𝑎𝑖,1,𝑎𝑖,2,…,𝑎𝑖,𝑚
#  (−106≤𝑎𝑖,𝑗≤106
# ) — the altitude of each cell in the grid. It is guaranteed that if a cell (𝑖,𝑗)
#  lies on the path, then 𝑎𝑖,𝑗=0
# .

# It is guaranteed that the sum of 𝑛⋅𝑚
#  over all test cases does not exceed 106
# .

# Output
# For each test case, output 𝑛 lines of 𝑚integers representing the restored grid of altitudes 𝑏𝑖,𝑗. The altitudes must satisfy −10^15≤𝑏𝑖,𝑗≤10^15, and additionally 𝑎𝑖,𝑗=𝑏𝑖,𝑗 if (𝑖,𝑗) is not on the path. If multiple solutions exist, output any of them.

# Example
# Input
# 4
# 3 3
# DRRD
# 0 2 3
# 0 0 0
# 3 1 0
# 4 5
# DRRRRDD
# 0 1 0 2 3
# 0 0 0 0 0
# -1 0 -3 -3 0
# 0 0 0 -1 0
# 2 3
# RRD
# 0 0 0
# 0 1 0
# 5 5
# DDDDRRRR
# 0 25 2 9 11
# 0 6 13 20 22
# 0 17 24 1 8
# 0 3 10 12 19
# 0 0 0 0 0

# Output
# 1 2 3
# 2 3 1
# 3 1 2
# -6 1 0 2 3
# 7 -1 3 2 -11
# -1 0 -3 -3 7
# 0 0 0 -1 1
# 0 -1 1
# 0 1 -1
# 18 25 2 9 11
# 4 6 13 20 22
# 15 17 24 1 8
# 21 3 10 12 19
# 7 14 16 23 5

# Note
# In the first test case, the grid has been filled such that every row and column contains the numbers 1,2,3
#  in some order, resulting in a common sum of 6
# .

# In the second test case, the grid has been filled such that all rows and columns sum to 0
# .

# This is the Code


for i in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    l=[]
    row=[]
    coloum=[]
    for i in range(n):
        l1=list(map(int,input().split()))
        row+=[sum(l1)]
        l.append(l1)
    for i in range(m):
        count=0
        for j in range(n):
            count+=l[j][i]
        coloum+=[count]
    i=j=0
    for k in s:
        if k=='R':
            l[i][j]=-coloum[j]
            j+=1
            row[i]+=l[i][j-1]
        else:
            l[i][j]=-row[i]
            i+=1
            coloum[j]+=l[i-1][j]
    l[i][j]=-coloum[j]
    for i in l:
        print(*i)
