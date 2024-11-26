# This is the question

# You are given three integers 𝑛
# , 𝑎
# , and 𝑏
# . Determine if there exist two permutations 𝑝
#  and 𝑞
#  of length 𝑛
# , for which the following conditions hold:

# The length of the longest common prefix of 𝑝
#  and 𝑞
#  is 𝑎
# .
# The length of the longest common suffix of 𝑝
#  and 𝑞
#  is 𝑏
# .
# A permutation of length 𝑛
#  is an array containing each integer from 1
#  to 𝑛
#  exactly once. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (𝑛=3
#  but there is 4
#  in the array).

# Input
# Each test contains multiple test cases. The first line contains a single integer 𝑡
#  (1≤𝑡≤104
# ) — the number of test cases. The description of test cases follows.

# The only line of each test case contains three integers 𝑛
# , 𝑎
# , and 𝑏
#  (1≤𝑎,𝑏≤𝑛≤100
# ).

# Output
# For each test case, if such a pair of permutations exists, output "Yes"; otherwise, output "No". You can output each letter in any case (upper or lower).

# Input
# 4
# 1 1 1
# 2 1 2
# 3 1 1
# 4 1 1

# Output
# Yes
# No
# No
# Yes


# This is the code

for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a==b and b==c and c==a:
        print('YES')
    elif a-(b+c)<=1:
        print('NO')
    else:
        print('YES')
