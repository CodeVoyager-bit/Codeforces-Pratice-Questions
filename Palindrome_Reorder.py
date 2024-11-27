# This is the Question


Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input
The only input line has a string of length n consisting of characters A–Z.

Output
Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".


Example
Input:
AAAACACBA

Output:
AACABACAA

# This is the Code


s=input()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
count=0
l=[]
for i in d:
    if d[i]%2==1:
        count+=1
        a=i
        d[i]-=1
        for j in range(d[i]//2):
            l.append(i)
    else:
        for j in range(d[i]//2):
            l.append(i)
if count>1:
    print('NO SOLUTION')
elif count==1:
    l=l+[a]+l[::-1]
    print(''.join(l))
else:
    l=l+l[::-1]
    print(''.join(l))
