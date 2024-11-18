# This is the Question
# You are given a binary array 𝑎 of 𝑛 elements, a binary array is an array consisting only of 0s and 1s.

# A blank space is a segment of consecutive elements consisting of only 0s.

# Your task is to find the length of the longest blank space.

# Input
# The first line contains a single integer 𝑡 (1≤𝑡≤1000) — the number of test cases.

# The first line of each test case contains a single integer 𝑛 (1≤𝑛≤100) — the length of the array.

# The second line of each test case contains 𝑛 space-separated integers 𝑎𝑖 (0≤𝑎𝑖≤1) — the elements of the array.

# Output
# For each test case, output a single integer — the length of the longest blank space.

# sample input :
# 5
# 5
# 1 0 0 1 0
# 4
# 0 1 1 1
# 1
# 0
# 3
# 1 1 1
# 9
# 1 0 0 0 1 0 0 0 1


# sample output
# 2
# 1
# 1
# 0
# 3



# This is the code

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    maxi=0
    count=0
    for i in l:
        if i==1:
            count=0
        else:
            count+=1
            if count>maxi:
                maxi=count
    print(maxi)
