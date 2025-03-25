# This is the Question 

# Raj goes to propose Simran on the special occasion of Propose Day but he fears of being rejected. So, he made a plan and needs your help as he is busy selecting a ring.

# Raj writes a love letter and want you to modify it as following:

# a) Remove all alphabets of word "REJECTED" from the letter, both in uppercase and lowercase that is you need to remove all letters among {'r','e','j','c','t','d','R','E','J','C','T','D'}.

# b) Change all uppercase to lowercase.

# c) Change all lowercase to uppercase.

# Print the modified letter of Raj.

# Input
# First line of input contains a single integer t, denoting number of test cases. Each testcase consist of two lines. First line of each test case is an integer N, denoting length of string and second line contains a String of upper- and lower-case English alphabets (1≤𝑡≤100
#  and 1≤𝑁≤1000).

# Output
# For each testcase, output two lines. First line contains size of modified letter and second line contains modified letter of Raj in new line.

# Example
# InputCopy
# 3
# 4
# ReaT
# 15
# AreNjeSHctIKedA
# 16
# AreSjeHUTctreedt
# OutputCopy
# 1
# A
# 7
# anshika
# 4
# ashu
# Note
# In first example, original letter is "ReaT" delete 'R', 'e' and 'T'. Remaining answer is "a" then change "a" to "A", which is final answer.

# This is the Code

for i in range(int(input())):
    n=int(input())
    s=input()
    a=['r','e','j','c','t','d','R','E','J','C','T','D']
    s1=''
    for i in s:
        if i in a:
            n-=1
            continue
        if i.isupper():
            s1+=i.lower()
        else:
            s1+=i.upper()
    print(n)
    print(s1)
