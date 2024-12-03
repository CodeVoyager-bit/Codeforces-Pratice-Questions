# You're given a string 𝑠
#  of length 𝑛
# , consisting of only lowercase English letters.

# You must do the following operation exactly once:

# Choose any two indices 𝑖
#  and 𝑗
#  (1≤𝑖,𝑗≤𝑛
# ). You can choose 𝑖=𝑗
# .
# Set 𝑠𝑖:=𝑠𝑗
# .
# You need to minimize the number of distinct permutations†
#  of 𝑠
# . Output any string with the smallest number of distinct permutations after performing exactly one operation.

# †
#  A permutation of the string is an arrangement of its characters into any order. For example, "bac" is a permutation of "abc" but "bcc" is not.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases 𝑡
#  (1≤𝑡≤500
# ). The description of the test cases follows.

# The first line of each test case contains 𝑛
#  (1≤𝑛≤10
# ) — the length of string 𝑠
# .

# The second line of each test case contains 𝑠
#  of length 𝑛
# . The string contains only lowercase English letters.

# Output
# For each test case, output the required 𝑠
#  after applying exactly one operation. If there are multiple solutions, print any of them.


# Example
# InputCopy
# 6
# 3
# abc
# 4
# xyyx
# 8
# alphabet
# 1
# k
# 10
# aabbccddee
# 6
# ttbddq
      
# OutputCopy
# cbc
# yyyx
# alphaaet
# k
# eabbccddee
# tttddq

# this is the code


for i in range(int(input())):
    n=int(input())
    s=input()
    if s.count(s[0])==n:
        print(s)
        continue
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    # print(d)
    d2={}
    for i in d:
        if d[i] in d2:
            d2[d[i]]+=[i]
        else:
            d2[d[i]]=[i]
    
    if len(d2)==1:
        l=list(s)
        a=d2[max(d2.keys())][0]
        b=d2[min(d2.keys())][1]
        l[l.index(b)]=a
        print(''.join(l))
        continue
    # print(d2)
    l=list(s)
    a=d2[max(d2.keys())][0]
    b=d2[min(d2.keys())][0]
    l[l.index(b)]=a
    print(''.join(l))
