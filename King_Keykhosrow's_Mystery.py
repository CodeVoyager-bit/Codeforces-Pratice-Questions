# This is the question

# time limit per test1 second
# memory limit per test256 megabytes
# There is a tale about the wise King Keykhosrow who owned a grand treasury filled with treasures from across the Persian Empire. However, to prevent theft and ensure the safety of his wealth, King Keykhosrow's vault was sealed with a magical lock that could only be opened by solving a riddle.


# The riddle involves two sacred numbers 𝑎
#  and 𝑏
# . To unlock the vault, the challenger must determine the smallest key number 𝑚
#  that satisfies two conditions:

# 𝑚
#  must be greater than or equal to at least one of 𝑎
#  and 𝑏
# .
# The remainder when 𝑚
#  is divided by 𝑎
#  must be equal to the remainder when 𝑚
#  is divided by 𝑏
# .
# Only by finding the smallest correct value of 𝑚
#  can one unlock the vault and access the legendary treasures!

# Input
# The first line of the input contains an integer 𝑡
#  (1≤𝑡≤100
# ), the number of test cases.

# Each test case consists of a single line containing two integers 𝑎
#  and 𝑏
#  (1≤𝑎,𝑏≤1000
# )
# Output
# For each test case, print the smallest integer 𝑚
#  that satisfies the conditions above.

# Input
# 2
# 4 6
# 472 896

# Output
# 12
# 52864

# Note
# In the first test case, you can see that:

# 4mod4=0
#  but 4mod6=4
# 5mod4=1
#  but 5mod6=5
# 6mod4=2
#  but 6mod6=0
# 7mod4=3
#  but 7mod6=1
# 8mod4=0
#  but 8mod6=2
# 9mod4=1
#  but 9mod6=3
# 10mod4=2
#  but 10mod6=4
# 11mod4=3
#  but 11mod6=5
# so no integer less than 12
#  satisfies the desired properties.

# This is the Code

import math
for i in range(int(input())):
    a,b=map(int,input().split())
    print(math.lcm(a,b))
