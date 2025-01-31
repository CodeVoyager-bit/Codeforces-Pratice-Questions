# This is the Question


# Toofan loves white walls! He recently painted a wall with some colors: Red (R), Green (G), and Blue (B). However, he realized that the wall doesn't look as bright and white as he imagined.

# Toofan's wall has length N, meaning it has N positions placed in a line, and each position can be painted in one color — either red, blue, or green.
# You are given a string 
# S
# S of length 
# N
# N, denoting the initial coloring of the wall.

# A white wall is defined as a wall where every consecutive set of positions with length divisible by 
# 3
# 3 contains equal numbers of R, G, and B.
# Formally, for every pair of indices 
# (
# L
# ,
# R
# )
# (L,R) such that 
# 1
# ≤
# L
# ≤
# R
# ≤
# N
# 1≤L≤R≤N and 
# (
# R
# −
# L
# +
# 1
# )
# (R−L+1) is divisible by 
# 3
# 3, there must be an equal amount of R, G, and B in the substring 
# S
# L
# S
# L
# +
# 1
# S
# L
# +
# 2
# …
# S
# R
# S 
# L
# ​
#  S 
# L+1
# ​
#  S 
# L+2
# ​
#  …S 
# R
# ​
#  .

# For instance,

# S
# =
# S= RGBR is an example of a white wall - the only substrings with length divisible by 
# 3
# 3 are RGB (with 
# L
# =
# 1
# L=1 and 
# R
# =
# 3
# R=3) and GBR (
# L
# =
# 2
# L=2 and 
# R
# =
# 4
# R=4), which both have an equal number of each color.
# S
# =
# S= RGBRGG is an example of a wall that's not white: choosing 
# L
# =
# 1
# L=1 and 
# R
# =
# 6
# R=6 gives us a segment with length 
# 6
# 6 (which is a multiple of 
# 3
# 3), which has three positions painted green but only one painted blue, which aren't equal.
# Toofan can repaint a single position on the wall to any other color (R, G, or B) in one operation.
# Your task is to determine the minimum number of operations required to transform the given wall into a white wall.

# Input Format
# The first line contains a single integer 
# T
# T — the number of test cases.
# Each test case consists of two lines of input.
# The first line contains an integer 
# N
# N — the length of the wall.
# The second line contains a string 
# S
# S of length 
# N
# N, where each character is either R, G, or B, denoting the initial coloring of the wall.
# Output Format
# For each test case, print a single integer — the minimum number of operations needed to make the wall white.
# Constraints
# 1
# ≤
# T
# ≤
# 1
# 0
# 5
# 1≤T≤10 
# 5
 
# 3
# ≤
# N
# ≤
# 3
# ×
# 1
# 0
# 5
# 3≤N≤3×10 
# 5
 
# S
# i
# ∈
# {
# R
# ,
# G
# ,
# B
# }
# S 
# i
# ​
#  ∈{R,G,B} for all 
# 1
# ≤
# i
# ≤
# N
# 1≤i≤N
# It is guaranteed that the sum of all 
# N
# N across all test cases does not exceed 
# 3
# ×
# 1
# 0
# 5
# 3×10 
# 5
#  .
# Sample 1:
# Input
# Output
# 2
# 6
# RGBRGG
# 3
# RRR
# 1
# 2
# Explanation:
# Test case 
# 1
# 1:

# Initial coloring: RGBRGG
# This is not a white wall: as noted in the statement, choosing 
# L
# =
# 1
# L=1 and 
# R
# =
# 6
# R=6 gives us a substring of length 
# 6
# 6 with different numbers of red/blue/green parts.
# Paint the 
# 6
# 6-th position to B, to make the wall RGBRGB.
# This can be verified to be a white wall.
# The pairs 
# (
# L
# ,
# R
# )
# (L,R) that must be checked are: 
# (
# 1
# ,
# 3
# )
# ,
# (
# 2
# ,
# 4
# )
# ,
# (
# 3
# ,
# 5
# )
# ,
# (
# 4
# ,
# 6
# )
# ,
# (
# 1
# ,
# 6
# )
# (1,3),(2,4),(3,5),(4,6),(1,6).
# Total changes: 
# 1
# 1.
# Test case 
# 2
# 2:

# Initial coloring: RRR
# Paint the 
# 2
# 2-nd position to G, and the 
# 3
# 3-rd block to B, to obtain RGB.
# Total changes: 
# 2

# This is the Code

t=int(input())
for i in range(t):
    nigga=int(input())
    s=input()
    count_min=[]
    l=['BGR','RBG','GBR','GRB','BRG','RGB']
    for i in l:
        count=0
        for j in range(nigga):
            if s[j]!=i[j%3]:
                count+=1
        count_min.append(count)
    print(min(count_min))
# 2.
# It can be proved that less than 
# 2
# 2 changes cannot result in a white wall.
